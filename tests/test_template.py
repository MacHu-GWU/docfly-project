# -*- coding: utf-8 -*-

import textwrap
from docfly.template import (
    TemplateEnum,
    render_module,
    PackageTemplateParams,
    render_package,
)
from docfly.vendor.picage import Package, Module

# from docfly.template import T
# from docfly.api_reference_doc import is_ignored


def test_render_module():
    module = Module("docfly.paths")
    content = render_module(params=module)
    # print(content)  # for debug only
    expected_content = textwrap.dedent(
        """
        paths
        =====
        
        .. automodule:: docfly.paths
            :members:
        """
    ).strip()
    # print([content])  # for debug only
    # print([expected_content])  # for debug only
    assert content.strip() == expected_content


def test_render_package():
    package = Package("docfly")
    sub_packages = [
        Package("docfly.directives"),
        Package("docfly.template"),
    ]
    sub_modules = [
        Module("docfly.auto_api_doc"),
        Module("docfly.autotoctree"),
    ]
    params = PackageTemplateParams(
        package=package,
        sub_packages=sub_packages,
        sub_modules=sub_modules,
    )
    content = render_package(params)
    print(content)  # for debug only
    expected_content = textwrap.dedent(
        """
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
            auto_api_doc <auto_api_doc>
            autotoctree <autotoctree>
    """
    ).strip()
    print([content])  # for debug only
    print([expected_content])  # for debug only
    assert content.strip() == expected_content

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
