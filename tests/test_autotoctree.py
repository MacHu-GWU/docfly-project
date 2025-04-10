# -*- coding: utf-8 -*-

from pathlib import Path

from docfly.autotoctree import PageFolder

dir_here = Path(__file__).absolute().parent
dir_documents = dir_here.joinpath("documents")


class TestPageFolder(object):
    def test_title(self):
        pf = PageFolder.new(dir=dir_documents)
        assert pf.title == "Welcome to the Document"

        pf = PageFolder.new(dir=dir_documents, index_filename="index_cn")
        assert pf.title == "欢迎来到此文档"

        pf = PageFolder.new(dir=dir_documents.joinpath("Section1"))
        assert pf.title == "Section1"

        pf = PageFolder.new(
            dir=dir_documents.joinpath("Section1"), index_filename="index_cn"
        )
        assert pf.title == "第1章"

    def test_sub_article_folders(self):
        pf = PageFolder.new(dir=dir_documents)
        assert len(pf.child_page_folders) == 3
        for ind, child_pdf in enumerate(pf.child_page_folders, start=1):
            assert child_pdf.title == f"Section{ind}"

        pf = PageFolder.new(dir=dir_documents, index_filename="index_cn")
        assert len(pf.child_page_folders) == 3
        for ind, child_pdf in enumerate(pf.child_page_folders, start=1):
            assert child_pdf.title == f"第{ind}章"

    def test_toc_directive(self):
        pf = PageFolder.new(dir=dir_documents)
        rst = pf.toc_directive().strip()

        lines = [
            ".. toctree::",
            "    :maxdepth: 1",
            "",
            "    Section1 <Section1/index>",
            "    Section2 <Section2/index>",
            "    Section3 <Section3/index>",
        ]
        expected = "\n".join(lines)
        assert rst == expected

        pf = PageFolder.new(dir=dir_documents, index_filename="index_cn")
        rst = pf.toc_directive().strip()

        lines = [
            ".. toctree::",
            "    :maxdepth: 1",
            "",
            "    第1章 <Section1/index_cn>",
            "    第2章 <Section2/index_cn>",
            "    第3章 <Section3/index_cn>",
        ]
        expected = "\n".join(lines)
        assert rst == expected


if __name__ == "__main__":
    from docfly.tests import run_cov_test

    run_cov_test(
        __file__,
        "docfly.autotoctree",
        preview=False,
    )
