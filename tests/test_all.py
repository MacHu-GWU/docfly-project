#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test_import():
    from docfly import ApiReferenceDoc
    from docfly import DocTree

if __name__ == "__main__":
    import py
    py.test.cmdline.main("--tb=native -s")