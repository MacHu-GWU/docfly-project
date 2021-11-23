.. _cn_docfly_quick_start:

docfly 快速开始
==============================================================================

- :ref:`English <en_docfly_quick_start>`
- :ref:`中文 <cn_docfly_quick_start>`

docfly 是一个帮助你更容易地使用 `sphinx-doc <http://www.sphinx-doc.org/en/stable/index.html>`_ 来构建你的文档网站的工具. 目前有两大杀手级功能:

- 自动生成 API 文档.
- 自动生成 目录.


自动生成 API 文档
------------------------------------------------------------------------------

如果你在为你的Python代码写文档, Sphinx有一个杀手级的功能: 自动从源代码中摘取docstring, 生成API文档. 然后你就可以使用在你的文档中使用 ``:ref:`modindex``` 引用之. 但是, 你需要手动编写大量代码, 告诉Sphinx哪些模块你想要自动为它生成文档. 具体做法请参考 `这篇说明 <http://www.sphinx-doc.org/en/stable/ext/autodoc.html>`_. 也就是说, 你还是需要手动为你的每一个 ``.py`` 文件创建 ``.rst`` 文件, 然后手动告诉 sphinx 哪些模块和函数需要自动文档.

**docfly** 的 **杀手级功能** 是, 只要你指定包的名称, 就能自动分析你的源代码, 然后自动为每一个 ``.py`` 文件, 每一个类, 每一个函数, 生成 ``:ref:`modindex``` 所需的一切文件. 并且在你的源代码结构发生变化之后, 自动更新. 下面我们就以 docfly 项目本身为例进行说明。你可以在 `这里 <https://github.com/MacHu-GWU/docfly-project>`_ 找到本文档中的示例代码.

使用的方法很简单, 在你的 ``conf.py`` 文件中添加如下代码::

    import docfly

    #--- Api Reference Doc ---
    package_name = docfly.__name__

    docfly.ApiReferenceDoc(
        conf_file=__file__, # 指定 conf.py 文件路径
        package_name=package_name, # 指定你要为其自动生成文档的包的名称
        ignored_package=[ # 指定你不想为哪些子模块和子包生成文档
            "%s.pkg" % package_name,
        ]
    ).fly()

简单来说上面这段代码做了三件事:

1. 告诉 docfly conf.py 文件在哪. 我们好在该目录下创建 .rst 文件.
2. 告诉 docfly 我们要为哪个包生成自动 API 文档.
3. 告诉 docfly 我们要排除掉哪些模块.


自动生成 目录
------------------------------------------------------------------------------

写一个文档网站就像写一本书. 分Chapter, Section, ... 一级一级的往下延伸。而我们希望能自动地从上往下, 为每一章生成它下面每一节的链接, 同理一级一级的传递下去.

根据 sphinx-doc 的 `官方文档 <http://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#toctree-directive>`_, 你需要在你要生成目录的地方, 放置如下 Directive::

    .. toctree::
        :maxdepth: 1

        Title of your sub document <path-to-the-rst-file>
        ...

也就是说, 你仍然要手动的指定你要在目录中包括哪些子文档. 当你创建了新的 ``.rst`` 文件时, 你需要手动将其添加到 Directive 中去.

而 docfly 的另一个重要功能就是: 只要你按照 :ref:`Sphinx 文档项目规范 <cn_sphinx_doc_style_guide>`, 那么仅仅使用 ``.. autotoctree::`` 标记, 就能自动发现当前目录下的子目录中的 ``index.rst`` 文档, 并在该处生成 ``.. toctree::`` 的索引.

你需要在 ``conf.py`` 中添加如下内容::

    extensions = [
        ...
        'docfly.directives',
        ...
    ]
