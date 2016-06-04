#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

package = __import__("toppackage")

setup(
    name = "toppackage",
    packages = find_packages(),
    version = package.__version__,
    license = package.__license__,
    description = "An example project for docfly demonstration.",
    author = "Sanhe Hu",
    author_email = "husanhe@gmail.com",
    url = "https://github.com/MacHu-GWU/docfly-project/tree/master/toppackage-project",
)