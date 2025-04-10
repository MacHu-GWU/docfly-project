# -*- coding: utf-8 -*-

from docfly import api


def test():
    _ = api
    _ = api.ApiDocGenerator
    _ = api.PageFolder
    _ = api.IndexFileNotFoundError
    _ = api.AutoTocTree
    _ = api.directives


if __name__ == "__main__":
    from docfly.tests import run_cov_test

    run_cov_test(
        __file__,
        "docfly.api",
        preview=False,
    )
