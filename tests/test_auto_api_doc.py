# -*- coding: utf-8 -*-

import shutil
from pathlib import Path

import docfly
from docfly.vendor.picage import Package, Module
from docfly.auto_api_doc import (
    normalize_ignore_patterns,
    should_ignore,
    render_package,
    ApiReferenceDoc,
)

package_name = docfly.__name__
dir_here = Path(__file__).absolute().parent


def test_normalize_ignore_patterns():
    assert normalize_ignore_patterns(["jinja2"]) == ["jinja2"]
    assert normalize_ignore_patterns(["jinja2.py"]) == ["jinja2"]


def test_should_ignore():
    assert should_ignore("jinja2", ["jinja2"]) is True
    assert should_ignore("jinja2.filters", ["jinja2.filters"]) is True
    assert should_ignore("jinja2.filters", ["jinja2.not_exists"]) is False

#
# def test_render_package():
#     text = render_package(package=Package("jinja2"), ignore_patterns=[])
#     # print(text)  # for debug only
#
#
# class TestApiReferenceDoc(object):
#     def test_fly(self):
#         # clean up existing API document files generated this test case
#         dir_source_package = dir_here.joinpath(package_name)
#         shutil.rmtree(dir_source_package, ignore_errors=True)
#
#         doc = ApiReferenceDoc(
#             conf_py_file=str(dir_here.joinpath("conf.py")),
#             package_name=package_name,
#             ignore_patterns=[
#                 f"{package_name}.vendor",
#                 f"{package_name}.paths.py",
#             ],
#         )
#         doc.fly()
#
#         assert dir_source_package.joinpath("api_reference_doc.rst").exists() is True
#         assert dir_source_package.joinpath("doctree.rst").exists() is True
#         assert dir_source_package.joinpath("vendor").exists() is False
#         assert dir_source_package.joinpath("paths.rst").exists() is False


if __name__ == "__main__":
    from docfly.tests import run_cov_test

    run_cov_test(
        __file__,
        "docfly.auto_api_doc",
        preview=False,
    )
