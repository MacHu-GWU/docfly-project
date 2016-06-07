.. image:: https://img.shields.io/badge/Last_Update-2016--06--01-brightgreen.svg


.. _Sanhe_sphinx_doc_project_style_guide:

Sanhe's Sphinx文档项目规范
==========================
每一个大型项目, 或是某一类的项目通常都有自己的项目规范。这些规范都是从大量的实际项目经验中总结而来。遵循一定的规范可以让你的代码更易读; 而前人的经验往往能帮助你避免很多你所没考虑到的问题。


命名空间
--------
1. 文件名中不要出现空格。
2. 使用 ``-`` 连接所有的单词, 而不是 ``_``, 这是因为 ``-`` 在Url中是合法字符, 而 ``_`` 不是。
3. 避免使用形如 ``ThisDocument`` 这样的多个单词不分隔, 而用首字母大写的方式。因为这样命名可读性较差。
4. 尽量使用全英文数字, 不要使用非英语字符, 但如果你必须要这么做, 也并没有问题


.. _page:

页面
----
每一个 ``.rst`` 文件在文档网站中代表的是一个页面。笔者推荐, 为你的每一个页面的文档文件, 创建一个独立的目录。其中包含 ``content.rst`` 以及 ``index.rst``。假设你本来想创建一个文件叫 ``learn-sphinx-doc.rst``, 你应该这样做::

	source
	|--- learn-sphinx-doc # this is a directory
	    |--- content.rst
	    |--- index.rst
	|--- index.rst # root

而不是::

	source
	|--- learn-sphinx-doc.rst
	|--- index.rst # root

这是因为, **你的文件中很可能包含有多个图片, 而你需要在你的文件中引用它们**。为每一个页面创建一个文件夹能够让你每个文件所引用的图片与其他文件的图片分开, 不至于混淆。而你的其他。

``content.rst`` 文件是你的正文文件, 你需要将你所需要写的所有内容都放在此文件中。而 ``index.rst`` 则使用 ``.. include:: content.rst`` 来包含 ``content.rst`` 文件中的内容。而 ``index.rst`` 中的内容则使用 `docfly <https://github.com/MacHu-GWU/docfly-project>`_ 自动生成。**为什么不直接在index.rst中写呢**? 这是因为我们可以通过自动化脚本, 自动根据 ``content.rst`` 为 ``index.rst`` 生成许多其他内容, 例如 Table of Content。而你可以专注于在 ``content.rst`` 文件中写内容部分。而其他部分, 可以交给程序自动生成。这样做可以避免错误以及提升工作效率。


图片
----
如果你使用 `页面 <page_>`_ 一节中的规范, 那么每一个 ``.rst`` 文件中所要引用的图片就应该跟 ``index.rst`` 保持在同一个目录下。如果你没有使用前面所说的规范, 那么建议你创建一个和你的 ``document-title.rst`` 文件同名的文件夹, 并加上 ``images`` 前缀, 例如 ``images-document-title``, 然后将图片放在这一目录内。
这样可以区分开每个文件所使用的图片。