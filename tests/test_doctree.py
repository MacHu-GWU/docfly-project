#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import pytest
from docfly.doctree import ArticleFolder
from pathlib_mate import PathCls as Path

docs_source_dir = Path(__file__).change(new_basename="test_source")


class TestArticleFolder(object):
    def test_title(self):
        af = ArticleFolder(dir_path=docs_source_dir.abspath)
        assert af.title == "Welcome to the Document"

        af = ArticleFolder(dir_path=docs_source_dir.append_parts("Section1").abspath)
        assert af.title == "Section1"

    def test_sub_article_folders(self):
        af = ArticleFolder(dir_path=docs_source_dir.abspath)
        assert len(af.sub_article_folders) == 3
        for ind, sub_af in enumerate(af.sub_article_folders):
            assert sub_af.title == "Section{}".format(ind + 1)

    def test_toc_directive(self):
        af = ArticleFolder(dir_path=docs_source_dir.abspath)
        rst_directive = af.toc_directive()
        print(rst_directive)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
