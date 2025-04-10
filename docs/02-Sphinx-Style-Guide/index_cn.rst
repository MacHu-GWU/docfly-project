.. _cn_sphinx_doc_style_guide:

Sphinx 文档项目规范
==============================================================================

- :ref:`English <en_sphinx_doc_style_guide>`
- :ref:`中文 <cn_sphinx_doc_style_guide>`

每一个大型项目, 或是某一类的项目通常都有自己的项目规范. 这些规范都是从大量的实际项目经验中总结而来. 遵循一定的规范可以让你的代码更易读; 而前人的经验往往能帮助你避免很多你所没考虑到的问题.

本规范是 ``docfly`` 在多年开发 sphinx-doc 插件, 以及建立 复杂的, 包含源代码 API 文档, 复杂树形结构, 多语言支持 等各种各样的文档项目总结的一套规范. 遵守该规范定义的一些模式可以大量的减少重复工作, 使你专注于文档本身.


命名空间
------------------------------------------------------------------------------
1. 文件名中不要出现空格.
2. 使用 ``-`` 连接所有的单词, 而不是 ``_``, 这是因为 ``-`` 在Url中是合法字符, 而 ``_`` 不是.
3. 标题避免使用形如 ``ThisDocument`` 这样的多个单词不分隔, 因为这样命名可读性较差. 推荐使用而用首字母大写的方式..
4. 尽量使用全英文数字, 不要使用非英语字符, 但如果你必须要这么做, 也并没有问题.


.. _cn_sphinx_doc_style_guide_page:

页面
------------------------------------------------------------------------------
每一个 ``.rst`` 文件在文档网站中代表的是一个页面. 笔者推荐, 为你的每一个页面的文档文件, 创建一个 **独立的目录**. 其中包含 ``index.rst``. 假设你本来想创建一个文件叫 ``learn-sphinx-doc.rst``, 你应该这样做::

    source
    |--- learn-sphinx-doc # this is a directory
        |--- index.rst # this is the equivalent of learn-sphinx-doc.rst
    |--- index.rst # root

而不是::

    source
    |--- learn-sphinx-doc.rst
    |--- index.rst # root

这是因为, **你的文件中很可能包含有多个图片, 而你需要在你的文件中引用它们**. 为每一个页面创建一个文件夹能够让你每个文件所引用的图片与其他文件的图片分开, 不至于混淆.


图片
------------------------------------------------------------------------------

如果你使用 :ref:`cn_sphinx_doc_style_guide_page` 一节中的规范, 那么每一个 ``.rst`` 文件中所要引用的图片就应该跟 ``index.rst`` 保持在同一个目录下. 如果你没有使用前面所说的规范, 那么建议你创建一个和你的 ``document-title.rst`` 文件同名的文件夹, 并加上 ``images`` 前缀, 例如 ``images-document-title``, 然后将图片放在这一目录内.

例如你有一个文档 ``example/index.rst``, 里面有多个图片 ``chart1.png``, ``chart2.png``. 你的文件目录看起来应该是这样::

    example
    |--- images
        |--- chart1.png
        |--- chart2.png
    |--- index.rst

这样做有以下几点好处:

1. 你展开 example 文件时, 要被引用的图片和文档本身分开, 清晰明了. 免除了在图片很多时找不到文档本身的麻烦. 同时也能用关键字 ``images`` 来定位图片目录.
2. 在文档中引用图片用的是 ``.. image:: ./images/chart1.png`` 这样的相对路径. 有清晰的模式能快速区分跟本文档密切相关的图片, 和其他文档中的图片.


多语言支持
------------------------------------------------------------------------------

如果你想要你的每一篇文档 (每一个 html 页面) 都支持多语言, sphinx 官方的方法很复杂. 有以下两种, 都不太推荐:

1. 用 ``gentext`` 来为你的文档自动生成目标语言的翻译, 翻译质量很差.
2. 用 readthedocs.org 中的多文档功能, 为你的文档维护多个 repo, 维护成本非常高.

我建议在遵守 :ref:`cn_sphinx_doc_style_guide_page` 中的规范的同时, 用 ``_es.rst``, ``_cn.rst`` 这样的后缀标识同一份文档的不同语言, 就像这样::

    tutorial
    |--- index.rst # english (default)
    |--- index_es.rst # spanish (default)
    |--- index_cn.rst # chinese (default)

然后在每篇文档的顶部使用形如 ``.. _en_tutorial:``, ``.. _es_tutorial:``, ``.. _cn_tutorial:`` 来为每篇文档做索引 (ref). 然后再在每篇文档的一级 header 后面添加如下链接, 允许用户在不同语言版本之间切换::

    - :ref:`English <en_tutorial>`
    - :ref:`española <es_tutorial>`
    - :ref:`中文 <cn_tutorial>`

当你要使用 ``.. autotoctree::`` 时, 你可以用 ``:index_file: index_cn.rst`` 来只定位同属于一种语言的子文档. 就像这样::

    .. autotoctree::
        :maxdepth: 1
        :index_file: index_cn.rst
