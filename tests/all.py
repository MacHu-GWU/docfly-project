# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from docfly.tests import run_cov_test

    run_cov_test(
        __file__,
        "docfly",
        is_folder=True,
        preview=False,
    )
