#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import docfly
from pathlib_mate import Path


def test():
    package_name = docfly.__name__
    source_dir = Path(__file__).absolute().\
        parent.parent.\
        append_parts("docs", "source").abspath
    doc = docfly.ApiReferenceDoc(
        package_name,
        dst=source_dir,
        ignored_package=[
            "%s.pkg" % package_name,
            "%s.zzz_ezinstall.py" % package_name,
        ]
    )
    doc.fly()


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
