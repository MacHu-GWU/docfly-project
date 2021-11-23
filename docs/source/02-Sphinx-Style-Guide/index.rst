.. _en_sphinx_doc_style_guide:

Sphinx Style Guide
==============================================================================

- :ref:`English <en_sphinx_doc_style_guide>`
- :ref:`中文 <cn_sphinx_doc_style_guide>`

每一个大型项目, 或是某一类的项目通常都有自己的项目规范. 这些规范都是从大量的实际项目经验中总结而来. 遵循一定的规范可以让你的代码更易读; 而前人的经验往往能帮助你避免很多你所没考虑到的问题.

本规范是 ``docfly`` 在多年开发 sphinx-doc 插件, 以及建立 复杂的, 包含源代码 API 文档, 复杂树形结构, 多语言支持 等各种各样的文档项目总结的一套规范. 遵守该规范定义的一些模式可以大量的减少重复工作, 使你专注于文档本身.


Naming Convention
------------------------------------------------------------------------------
1. Don't use " " (space) in file name or directory name
2. Use ``-`` as much as possible. Because ``-`` is a valid character in URL, but ``_`` is not.
3. Don't use Camel Case because it is not Python style.
4. Use english character and digits, try to avoid using non ascii characters.


.. _en_sphinx_doc_style_guide_page:

Page
------------------------------------------------------------------------------
Each ``.rst`` file represent a html page in your document website. I recommend using a folder instead of a file for each page. For example, suppose you want to create a ``learn-sphinx-doc.rst`` file, you should do this::

    source
    |--- learn-sphinx-doc # this is a directory
        |--- index.rst # this is the equivalent of learn-sphinx-doc.rst
    |--- index.rst # root

and NOT do this::

    source
    |--- learn-sphinx-doc.rst
    |--- index.rst # root


Image
------------------------------------------------------------------------------

If you follow the style defined in :ref:`en_sphinx_doc_style_guide_page`, Then you should put images related to a ``index.rst`` file in the same folder.

Let's say you have a document ``example/index.rst``, there are lots of images ``chart1.png``, ``chart2.png``. Your file structure should look like this::

    example
    |--- images
        |--- chart1.png
        |--- chart2.png
    |--- index.rst

Advantages:

1. images are isolated from the main document.
2. in your rst code, you use this relative syntax to include a image ``.. image:: ./images/chart1.png``. It helps you to locate those images belongs to this specific ``index.rst`` file.


Multi Language Support
------------------------------------------------------------------------------

If you want every html page to support multi language, the official method is very complicate. The official methods are (NOT RECOMMENDED):

1. use ``gentext`` plugin to translate the doc to target language, very poor translation quality.
2. use the multi lang feature in ``readthedocs.org``, but you need to maintain multi git repo, it is very hard to keep them up-to-date.

I recommend to follow the style defined in :ref:`en_sphinx_doc_style_guide_page`, and use ``_es.rst``, ``_cn.rst`` surfix to indicate the different lang version for the same document. It looks like this in your file system::

    tutorial
    |--- index.rst # english (default)
    |--- index_es.rst # spanish (default)
    |--- index_cn.rst # chinese (default)

Then you can use the reference link, such as ``.. _en_tutorial:``, ``.. _es_tutorial:``, ``.. _cn_tutorial:`` at the begin of your each ``.rst`` file. Then put this rst snippet right under your top header. It serves as a nagivator allow user to switch language::

    - :ref:`English <en_tutorial>`
    - :ref:`española <es_tutorial>`
    - :ref:`中文 <cn_tutorial>`

 When you need ``.. autotoctree::`` for non-default (english) sub documents, you can use this option ``:index_file: index_cn.rst`` to locate sub documents that is in specific language::

    .. autotoctree::
        :maxdepth: 1
        :index_file: index_es.rst
