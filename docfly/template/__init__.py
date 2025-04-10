#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jinja2 Template rendering module for Sphinx documentation generation.
"""

import typing as T
import dataclasses
from jinja2 import Template

from ..paths import dir_package
from ..vendor.picage import Package, Module

if T.TYPE_CHECKING:
    from ..autotoctree import PageFolder


def get_template(name: str) -> Template:
    """
    Load a Jinja2 template by name from the template directory.
    """
    path = dir_package.joinpath("template", f"{name}.tpl")
    return Template(path.read_text(encoding="utf-8"))


class TemplateEnum:
    toc = get_template("toc")
    module = get_template("module")
    package = get_template("package")


ModuleTemplateParams = Module


def render_module(params: ModuleTemplateParams) -> str:
    """
    Render `module template <https://github.com/MacHu-GWU/docfly-project/blob/main/docfly/template/module.tpl>`_
    for Sphinx documentation.

    Example module ``docfly.auto_api_doc``:

    Example rendered sphinx doc:

    .. code-block::

        auto_api_doc
        ============

        .. automodule:: docfly.auto_api_doc
            :members:

    """
    return TemplateEnum.module.render(params=params)


@dataclasses.dataclass
class PackageTemplateParams:
    package: Package = dataclasses.field()
    sub_packages: list[Package] = dataclasses.field()
    sub_modules: list[Module] = dataclasses.field()


def render_package(params: PackageTemplateParams) -> str:
    """
    Render `package template <https://github.com/MacHu-GWU/docfly-project/blob/main/docfly/template/package.tpl>`_
    for Sphinx documentation.

    Example package ``docfly``:

    Example rendered sphinx doc:

    .. code-block::

        docfly
        ======

        .. automodule:: docfly
            :members:

        sub packages and modules
        ------------------------

        .. toctree::
            :maxdepth: 1

            directives <directives/__init__>
            template <template/__init__>
            tests <tests/__init__>
            auto_api_doc <auto_api_doc>
            autotoctree <autotoctree>

    See:
    """
    return TemplateEnum.package.render(params=params)


@dataclasses.dataclass
class TocTemplateParams:
    page_folders: list["PageFolder"] = dataclasses.field()
    maxdepth: T.Optional[int] = dataclasses.field(default=None)


def render_toc(params: TocTemplateParams) -> str:
    """
    Render `toctree template <https://github.com/MacHu-GWU/docfly-project/blob/main/docfly/template/toc.tpl>`_
    for Sphinx documentation.

    Example table of content tree
    `docfly project docs/sources <https://github.com/MacHu-GWU/docfly-project/tree/main/docs/source>`_:

    Example rendered sphinx doc:

    .. code-block::

    See:
    """
    return TemplateEnum.toc.render(params=params)