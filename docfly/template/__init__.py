#!/usr/bin/env python
# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from jinja2 import Template

from ..paths import dir_package
from ..vendor.picage import Package, Module

if T.TYPE_CHECKING:
    pass


def get_template(name: str) -> Template:
    path = dir_package.joinpath("template", f"{name}.tpl")
    return Template(path.read_text(encoding="utf-8"))


class TemplateEnum:
    toc = get_template("toc")
    module = get_template("module")
    package = get_template("package")


ModuleTemplateParams = Module


def render_module(params: ModuleTemplateParams) -> str:
    """
    Render module template.

    Example module ``docfly.auto_api_doc``:

    Example rendered sphinx doc:

    .. code-block::

        auto_api_doc
        ============

        .. automodule:: docfly.auto_api_doc
            :members:

    See: https://github.com/MacHu-GWU/docfly-project/blob/main/docfly/template/module.tpl
    """
    return TemplateEnum.module.render(params=params)


@dataclasses.dataclass
class PackageTemplateParams:
    package: Package = dataclasses.field()
    sub_modules: list[Module] = dataclasses.field()


def render_package(params: PackageTemplateParams) -> str:
    """
    Render package template.

    Example package ``docfly``:

    Example rendered sphinx doc:

    .. code-block::

        auto_api_doc
        ============

        .. automodule:: docfly.auto_api_doc
            :members:

    See: https://github.com/MacHu-GWU/docfly-project/blob/main/docfly/template/module.tpl
    """
    return TemplateEnum.module.render(params=params)