#!/usr/bin/env python
# -*- coding: utf-8 -*-

import docfly

package_name = "docfly"

doc = docfly.ApiReferenceDoc(
    package_name,
    dst="source",
    ignore=[
        "%s.packages" % package_name,
        "%s.zzz_manual_install.py" % package_name,
    ]
)
doc.fly()