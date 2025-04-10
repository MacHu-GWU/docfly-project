# -*- coding: utf-8 -*-

import shutil
from pathlib import Path

import docfly
from docfly.auto_api_doc import (
    normalize_ignore_patterns,
    should_ignore,
    ApiDocGenerator,
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


class TestApiDocGenerator(object):
    def test_fly(self):
        # clean up existing API document files generated this test case
        dir_output = dir_here.joinpath("api")
        shutil.rmtree(dir_output, ignore_errors=True)

        # run docfly to generate API document files
        doc = ApiDocGenerator(
            dir_output=dir_output,
            package_name="docfly",
            ignore_patterns=[
                f"docfly.vendor",
                f"docfly._version.py",
                f"docfly.paths.py",
            ],
        )
        doc.fly()

        # check the generated API document files
        dir_docfly = dir_output.joinpath("docfly")

        assert dir_docfly.joinpath("directives", "__init__.rst").exists() is True
        assert dir_docfly.joinpath("directives", "autotoctree.rst").exists() is True
        assert dir_docfly.joinpath("auto_api_doc.rst").exists() is True
        assert dir_docfly.joinpath("autotoctree.rst").exists() is True

        assert dir_docfly.joinpath("vendor").exists() is False
        assert dir_docfly.joinpath("paths.rst").exists() is False


if __name__ == "__main__":
    from docfly.tests import run_cov_test

    run_cov_test(
        __file__,
        "docfly.auto_api_doc",
        preview=False,
    )
