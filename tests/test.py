#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docfly import Docfly

if __name__ == "__main__":
    docfly = Docfly("toppackage", dst="_source", 
        ignore=["toppackage.subpackage1", 
                "toppackage.module2.py", 
                "toppackage.subpackage2.module22.py"])
    docfly.fly()