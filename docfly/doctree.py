#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""

from __future__ import print_function
import os
import jinja2
try:
    from .packages.dataIO import textfile
    from .template import template_collection as tc
except:
    from docfly.packages.dataIO import textfile
    from docfly.template import template_collection as tc


class Article(object):
    def __init__(self, title, path):
        self.title = title
        self.path = path


class DocTree(object):
    def __init__(self, dir_path):
        if self.is_doc_dir(dir_path) is False:
            raise Exception
        self.dir_path = dir_path

    @staticmethod
    def is_doc_dir(dir_path):
        if os.path.exists(os.path.join(dir_path, "content.rst")):
            return True
        else:
            return False

    @staticmethod
    def get_doc_dir_list(dir_path):
        dir_list = list()
        for path in os.listdir(dir_path):
            abspath = os.path.join(dir_path, path)
            if DocTree.is_doc_dir(abspath):
                dir_list.append(abspath)
        return dir_list

    @staticmethod
    def process(dir_path):
        def get_title(abspath):
            lastline = None
            for line in textfile.readlines(abspath, strip="both"):
                if line == "=" * len(line):
                    return lastline.strip()
                else:
                    lastline = line
            return None

        article_list = list()

        for sub_dir_path in DocTree.get_doc_dir_list(dir_path):
            abspath = os.path.join(sub_dir_path, "content.rst")
            title = get_title(abspath)
            path = os.path.basename(sub_dir_path) + "/index.rst"
            article = Article(title=title, path=path)
            article_list.append(article)

        content = jinja2.Template(tc.index).\
            render(article_list=article_list, has_toc=len(article_list) >= 1)
        
        abspath = os.path.join(dir_path, "index.rst")
        textfile.write(content, abspath)
        print("Made: %s" % abspath)
        
    def fly(self):
        for current_dir, dir_list, file_list in os.walk(self.dir_path):
            if self.is_doc_dir(current_dir):
                self.process(current_dir)

#--- Unittest ---
if __name__ == "__main__":
    dir_path = r"C:\HSH\Workspace\py33\py33_projects\docfly-project\learn_python-project\source"
    doc = DocTree(dir_path)
    doc.fly()

    DocTree.process(dir_path)
