#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import pytest
import docfly
from pathlib_mate import Path


def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    with open("a.rst", "wb") as f:
        content = "Header\n=========="
        f.write(content.encode("utf-8"))

    with open("b.rst", "wb") as f:
        content = "Header\n----------"
        f.write(content.encode("utf-8"))


def teardown_module(module):
    """ teardown any state that was previously setup with a setup_module
    method.
    """
    import os
    for file in ["a.rst", "b.rst"]:
        try:
            os.remove(file)
        except:
            pass


def test():
    source_dir = Path(__file__).absolute().\
        parent.parent.\
        append_parts("docs", "source").abspath
    doc = docfly.DocTree(source_dir)
    doc.fly(table_of_content_header="Table of Content")


def test_get_title():
    assert docfly.DocTree.get_title("a.rst") == "Header"
    assert docfly.DocTree.get_title("b.rst") == "Header"


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
