# -*- coding: utf-8 -*-

from docfly.template import TemplateEnum, render_module
from docfly.vendor.picage import Package, Module

# from docfly.template import T
# from docfly.api_reference_doc import is_ignored


def test_render_module():
    module = Module("docfly.paths")
    text = render_module(params=module)
    # print(text)  # for debug only
    expected_lines = [
        "paths",
        "=====",
        "",
        ".. automodule:: docfly.paths",
        "    :members:",
    ]
    assert text.strip() == "\n".join(expected_lines)


def _test():
    pkg = Package("docfly")
    text = TemplateEnum.package.render(
        package=pkg,
        ignored_packages=[],
        is_ignored=is_ignored,
    )
    # print(text)  # for debug only

    # article = ArticleFolder(title="Hello World", path="hello-world/index.rst")
    # text = TC.toc.render(
    #     header="Table of Content",
    #     article_list=[
    #         article,
    #     ],
    # )
    # print(text)


if __name__ == "__main__":
    from docfly.tests import run_cov_test

    run_cov_test(
        __file__,
        "docfly.template",
        preview=False,
    )
