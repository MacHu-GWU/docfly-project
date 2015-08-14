#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open("README.md", "rb") as f:
    LONG_DESCRIPTION = f.read().decode("utf-8")
    
VERSION = __import__("docfly").__version__

setup(
    name = "docfly",
    packages = ["docfly"],
    version = VERSION,
    description = "A Python project standard doc site doc file builder (build based on sphinx)",
    long_description=LONG_DESCRIPTION,
    author = "Sanhe Hu",
    author_email = "husanhe@gmail.com",
    url = "https://github.com/MacHu-GWU/docfly-project",
    keywords = ["documentation", "tool"],
)