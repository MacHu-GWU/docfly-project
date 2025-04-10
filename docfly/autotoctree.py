# -*- coding: utf-8 -*-

"""

`toctree <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree>`_ [explain the purpose here]

This module provide utility to generate toctree directive base on your current folder structure

:ref:`Sanhe Sphinx standard <en_sphinx_doc_style_guide>`.
"""

import typing as T
import json
import dataclasses
from pathlib import Path
from functools import cached_property

from .template import TemplateEnum

T_INDEX_FILE_TYPE = T.Literal["rst", "md", "nb"]


@dataclasses.dataclass
class PageFolder:
    """
    Represent an ``index.rst`` or ``index.ipynb`` file with a Title in a directory.

    :param index_file: the index file name (no file extension)
    :param dir_path: A folder contains single rst file. The rst file path

    ::

        /current_folder
        /current_folder/index.rst
        /current_folder/subfolder_1/index.rst
        /current_folder/subfolder_2/index.ipynb
        /current_folder/subfolder_3/...


    content of ``/current_folder/index.rst``

    .. code-block:: rest

        .. autotoctree::
            :maxdepth: 1

    will generate the following toctree directive

    .. code-block:: rest

        .. toctree::
            :maxdepth: 1

            Section1 <Section1/index>
            Section2 <Section2/index>
            Section3 <Section3/index>

    **中文文档**

    一篇 Article 代表着文件夹中有一个 ``index.rst`` 或 ``index.ipynb`` 文件的文件夹.
    其中必然有至少一个标题元素.
    """

    dir: Path = dataclasses.field()
    index_filename: str = dataclasses.field()
    path_index_file: Path = dataclasses.field(init=False)
    index_file_type: T_INDEX_FILE_TYPE = dataclasses.field(init=False)

    @classmethod
    def new(
        cls,
        dir: Path,
        index_filename: str = "index",
    ):
        child_page_folder = cls(dir=dir, index_filename=index_filename)
        if child_page_folder.path_index_rst.exists():
            child_page_folder.path_index_file = child_page_folder.path_index_rst
            child_page_folder.index_file_type = "rst"
        # We check notebook before markdown, because sometime people have
        # converted markdown (from notebook) at the same location.
        elif child_page_folder.path_index_ipynb.exists():
            child_page_folder.path_index_file = child_page_folder.path_index_ipynb
            child_page_folder.index_file_type = "nb"
        elif child_page_folder.path_index_md.exists():
            child_page_folder.path_index_file = child_page_folder.path_index_md
            child_page_folder.index_file_type = "md"
        else:  # pragma: no cover
            raise FileNotFoundError(
                f"Cannot find index file in {child_page_folder.dir}"
            )
        return child_page_folder

    @property
    def path_index_rst(self) -> Path:
        """
        The actual RestructuredText file absolute path.
        """
        return self.dir.joinpath(f"{self.index_filename}.rst")

    @property
    def path_index_md(self) -> Path:
        """
        The actual markdown file absolute path.
        """
        return self.dir.joinpath(f"{self.index_filename}.md")

    @property
    def path_index_ipynb(self) -> Path:
        """
        The actual Jupyter Notebook file absolute path.
        """
        return self.dir.joinpath(f"{self.index_filename}.ipynb")

    @property
    def path_str(self):
        """
        File relative path from the folder.
        """
        return f"{self.dir.name}/{self.index_filename}"

    def get_title_from_rst(self) -> T.Optional[str]:
        """
        Get title line from .rst file.

        **中文文档**

        从一个 ``_filename`` 所指定的 .rst 文件中, 找到顶级标题.
        也就是第一个 ``====`` 或 ``----`` 或 ``~~~~`` 上面一行.
        """

        # replace ``.. include::`` with the content of the included file
        lines = list()
        with self.path_index_file.open("r", encoding="utf-8") as f:
            for cursor_line in f.readlines():
                cursor_line = cursor_line.strip()
                if cursor_line.startswith(".. include::"):
                    relpath_parts = cursor_line.split("::")[-1].strip().split("/")
                    path_included = self.path_index_file.parent.joinpath(*relpath_parts)
                    if path_included.exists():
                        cursor_line = path_included.read_text(encoding="utf-8")
                lines.append(cursor_line)
        rst_content = "\n".join(lines)

        # Identify the title line
        header_bar_char_list = "=-~+*#^"

        # please add more comments here
        cursor_previous_line = None
        for cursor_line in rst_content.split("\n"):
            for header_bar_char in header_bar_char_list:
                if cursor_line.startswith(header_bar_char):
                    flag_full_bar_char = cursor_line == header_bar_char * len(
                        cursor_line
                    )
                    flag_line_length_greather_than_1 = len(cursor_line) >= 1
                    flag_previous_line_not_empty = bool(cursor_previous_line)
                    if (
                        flag_full_bar_char
                        and flag_line_length_greather_than_1
                        and flag_previous_line_not_empty
                    ):
                        return cursor_previous_line.strip()
            cursor_previous_line = cursor_line

        msg = (
            "Warning, this document doesn't have any %s header!" % header_bar_char_list
        )
        print(msg)
        return None

    def get_title_from_md(self) -> T.Optional[str]:
        raise NotImplementedError

    def get_title_from_ipynb(self) -> T.Optional[str]:
        """
        Get title line from .ipynb file.

        **中文文档**

        从一个 ``_filename`` 所指定的 .ipynb 文件中, 找到顶级标题.
        也就是第一个 ``#`` 后面的部分.

        有的时候我们会用 raw RestructuredText 来做顶级标题.
        """
        header_bar_char_list = "=-~+*#^"

        data = json.loads(self.path_index_ipynb.read_text(encoding="utf-8"))
        for row in data["cells"]:
            if len(row["source"]):
                cell_type: str = row.get("cell_type", "unknown")
                raw_mimetype: str = row.get("metadata", {}).get(
                    "raw_mimetype", "unknown"
                )
                rst_mimetype = [
                    "text/restructuredtext",
                    "text/x-rst",
                ]
                if cell_type == "markdown":
                    content = row["source"][0]
                    line = content.split("\n")[0]
                    if "# " in line:
                        return line[2:].strip()
                elif cell_type == "raw" and raw_mimetype in rst_mimetype:
                    try:
                        line = row["source"][3].strip()
                    except IndexError:
                        continue
                    try:
                        title_line = row["source"][2].strip()
                    except IndexError:
                        continue
                    for header_bar_char in header_bar_char_list:
                        if line.startswith(header_bar_char):
                            flag_full_bar_char = line == header_bar_char * len(line)
                            flag_line_length_greather_than_1 = len(line) >= 1
                            flag_previous_line_not_empty = bool(title_line)
                            if (
                                flag_full_bar_char
                                and flag_line_length_greather_than_1
                                and flag_previous_line_not_empty
                            ):
                                return title_line
                else:
                    pass

        msg = "Warning, this document doesn't have any level 1 header!"
        print(msg)
        return None

    @cached_property
    def title(self) -> T.Optional[str]:
        """
        Title for the first header in the index file
        """
        if self.index_file_type == "rst":
            return self.get_title_from_rst()
        elif self.index_file_type == "nb":
            return self.get_title_from_ipynb()
        elif self.index_file_type == "md":
            return self.get_title_from_md()
        else:  # pragma: no cover
            print("never gonna reach here")

    @cached_property
    def child_page_folders(self) -> T.List["PageFolder"]:
        """
        Returns all valid ArticleFolder sitting inside of
        :attr:`ArticleFolder.dir_path`.
        """
        child_page_folders = list()
        dir_list = [path for path in self.dir.iterdir() if path.is_dir()]
        dir_list.sort()

        for dir in dir_list:
            child_page_folder = self.__class__.new(dir=dir, index_filename=self.index_filename)
            try:
                if child_page_folder.title is not None:
                    child_page_folders.append(child_page_folder)
            # skip folders that is failed to extract title
            except:
                pass
        return child_page_folders

    def toc_directive(self, maxdepth=1):
        """
        Generate toctree directive text.

        :param table_of_content_header:
        :param header_bar_char:
        :param header_line_length:
        :param maxdepth:
        :return:
        """
        articles_directive_content = TemplateEnum.toc.render(
            maxdepth=maxdepth,
            child_page_folders=self.child_page_folders,
        )
        return articles_directive_content
