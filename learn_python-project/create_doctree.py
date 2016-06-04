#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script can create pure words doc tree.
"""

import docfly

doc = docfly.DocTree(
    "source",
)
doc.fly()