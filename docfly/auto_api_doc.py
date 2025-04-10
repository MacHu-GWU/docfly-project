# -*- coding: utf-8 -*-

"""
Create api reference doc.
"""

import typing as T
import shutil
import dataclasses
from pathlib import Path
from functools import cached_property

from .template import (
    TemplateEnum,
    render_module,
    PackageTemplateParams,
    render_package,
)
from .vendor.picage import Package, Module


def normalize_ignore_patterns(patterns: list[str]) -> list[str]:
    """
    Normalize ignore patterns to be used for ignoring modules/packages.
    """
    normalized = []
    for pattern in patterns:
        if pattern.endswith(".py"):
            pattern = pattern[:-3]
        normalized.append(pattern)
    return normalized


def should_ignore(
    fullname: str,
    normalized_patterns: list[str],
) -> bool:
    """
    Test, if this :class:`docfly.pkg.picage.Module`
    or :class:`docfly.pkg.picage.Package` should be included to generate
    API reference document.

    **中文文档**

    根据全名判断一个包或者模块是否要被包含到自动生成的 API 文档中。
    """
    for pattern in normalized_patterns:
        if fullname.startswith(pattern):
            return True
    return False


# def render_package(package: Package, ignore_patterns: list[str]) -> str:
#     """
#     .. code-block::
#
#         {{ package_name }}
#         ==================
#
#         .. automodule:: {{ package_name }}
#             :members:
#
#         sub packages and modules
#         ------------------------
#
#         .. toctree::
#            :maxdepth: 1
#
#             {{ sub_package_name1 }} <{{ sub_package_name1 }}/__init__>
#             {{ sub_package_name2 }} <{{ sub_package_name2 }}/__init__>
#             {{ sub_module_name1}} <{{ sub_module_name1}}>
#             {{ sub_module_name2}} <{{ sub_module_name2}}>
#     """
#     return TemplateEnum.package.render(
#         package=package,
#         ignore_patterns=ignore_patterns,
#         is_ignored=is_ignored,
#     )


def write_file(path: Path, text: str):
    try:
        path.write_text(text, encoding="utf-8")
    except FileNotFoundError:
        path.parent.mkdir(parents=True)
        path.write_text(text, encoding="utf-8")


@dataclasses.dataclass
class ApiDocGenerator:
    """
    A class to generate sphinx-doc api reference part.

    Example::

        package
        |--- subpackage1
            |--- __init__.rst
            |--- module.rst
        |--- subpackage2
            |--- __init__.rst
            |--- module.rst
        |--- __init__.rst
        |--- module1.rst
        |--- module2.rst

    :param dir_output: the output of the autodoc code. Usually it next to the
        sphinx doc ``conf.py`` file. For example if your ``conf.py`` file is
        at ``docs/source/conf.py``, and your package name is ``docfly``, then
        the autodoc code should locate at::

        /docs/source/docfly
        /docs/source/docfly/__init__.rst
        /docs/source/docfly/module1.rst
        /docs/source/docfly/module2.rst
        /docs/source/docfly/...

    :param package_name: the importable package name
    :param ignore_patterns: default empty list, package, module relative
        prefix you want to ignored

    **中文文档**

    如果你需要忽略一个包: 请使用 ``docfly.packages``
    如果你需要忽略一个模块: 请使用 ``docfly.zzz_manual_install`` 或
    ``docfly.zzz_manual_install.py``
    """

    dir_output: Path = dataclasses.field()
    package_name: str = dataclasses.field()
    ignore_patterns: list[str] = dataclasses.field(default_factory=list)

    def __post_init__(self):
        self.ignore_patterns = normalize_ignore_patterns(self.ignore_patterns)

    @cached_property
    def package(self) -> Package:
        """
        The package object.
        """
        return Package(self.package_name)

    def fly(
        self,
        cleanup_before_fly: bool = True,
    ):
        """
        Generate doc tree.
        """
        # clearn up existing api document
        if cleanup_before_fly:
            shutil.rmtree(self.dir_output, ignore_errors=True)

        # create .rst files
        for package, parent, sub_packages, sub_modules in self.package.walk():
            if should_ignore(package.fullname, self.ignore_patterns):
                continue
            filtered_sub_packages = [
                sub_package
                for sub_package in sub_packages
                if should_ignore(sub_package.fullname, self.ignore_patterns) is False
            ]
            filtered_sub_modules = [
                sub_module
                for sub_module in sub_modules
                if should_ignore(sub_module.fullname, self.ignore_patterns) is False
            ]
            package_template_params = PackageTemplateParams(
                package=package,
                sub_packages=filtered_sub_packages,
                sub_modules=filtered_sub_modules,
            )

            dir_package = self.dir_output.joinpath(*package.fullname.split("."))
            path_init_rst = dir_package.joinpath("__init__.rst")
            content = render_package(package_template_params)
            write_file(path_init_rst, content)

            for module in filtered_sub_modules:
                path_module = dir_package.joinpath(f"{module.shortname}.rst")
                content = render_module(module)
                write_file(path_module, content)
