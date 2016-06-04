#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script can create python module doc tree.
"""

import docfly

doc = docfly.DocTree("source")
doc.fly()

package_name = "toppackage"

doc = docfly.ApiReferenceDoc(
    package_name,
    dst="source",
    ignore=[
        "%s.packages" % package_name,
        "%s.zzz_manual_install.py" % package_name,
    ]
)
doc.fly()