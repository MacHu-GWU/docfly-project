#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import shutil
import docfly
from pathlib_mate import Path

package_name = docfly.__name__


def setup_module(module):
    print(Path(__file__).change(new_basename=package_name).abspath)
    try:
        shutil.rmtree(Path(__file__).change(new_basename=package_name).abspath)
    except:
        pass


def teardown_module(module):
    setup_module(module)


def test():
    doc = docfly.ApiReferenceDoc(
        conf_file=Path(__file__).change(new_basename="conf.py").abspath,
        package_name=package_name,
        ignored_package=[
            "%s.pkg" % package_name,
            "zzz_manual_install.py",
        ]
    )
    doc.fly()


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
