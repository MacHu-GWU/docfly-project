.. _cn-sphinx-doc-style-guide:

Sphinx 文档项目规范
==============================================================================
- :ref:`English <en-sphinx-doc-style-guide>`
- :ref:`中文 <cn-sphinx-doc-style-guide>`

这些最佳实践源于真实项目的丰富经验。遵循既定的约定可以使您的文档更具可读性，同时通过已验证的模式帮助您避免常见的陷阱。

本指南展示了通过多年使用 Sphinx-doc、构建包含 API 参考、层次结构和多语言支持的复杂文档系统所开发的最佳实践。通过遵循这些建议，您可以显著减少重复性工作，专注于创建有价值的内容。


文件组织
------------------------------------------------------------------------------
以逻辑层次结构组织您的 Sphinx 文档。典型的结构可能如下：

.. code-block:: text

    docs/
    ├── source/             # 源文件 (.rst, .md, .ipynb)
    │   ├── _static/        # 静态文件 (CSS, 图片)
    │   ├── _templates/     # 自定义模板
    │   ├── conf.py         # Sphinx 配置
    │   ├── index.rst       # 主入口点
    │   ├── installation/   # 章节目录
    │   │   └── index.rst
    │   ├── usage/
    │   │   └── index.rst
    │   └── api/            # API 文档（可自动生成）
    │       └── ...
    └── build/              # 生成的输出 (HTML, PDF 等)
        └── html/           # 生成的 HTML 文件


命名约定
------------------------------------------------------------------------------
为了保持一致、可维护的文档：

1. **文件名和目录中避免使用空格** - 使用连字符或下划线代替
2. **优先使用连字符而非下划线** - 连字符在 URL 中有效，而下划线可能会导致问题
3. **对文件和目录名使用 kebab-case 命名法** - 例如，使用 ``user-guide.rst`` 而非 ``UserGuide.rst``
4. **坚持使用 ASCII 字符** - 尽可能使用英文名称和字母数字字符
5. **保持一致性** - 选择一种命名约定并在整个项目中应用它


.. _cn-sphinx-doc-style-guide-page:

页面组织
------------------------------------------------------------------------------
**推荐：使用基于文件夹的结构**

与其使用包含许多 .rst 文件的平面层次结构，不如将每个主要文档章节组织为带有索引文件的文件夹：

.. code-block:: text

    # 推荐
    docs/source/
    ├── user-guide/           # "用户指南"章节的目录
    │   ├── index.rst         # 主要内容（相当于 user-guide.rst）
    │   ├── images/           # 章节特定的图片
    │   │   ├── screenshot1.png
    │   │   └── diagram.png
    │   └── examples/         # 额外的子章节文件
    │       └── index.rst
    └── index.rst             # 根文档

而不是：

.. code-block:: text

    # 不推荐
    docs/source/
    ├── user-guide.rst        # 单个文件
    ├── screenshot1.png       # 图片与文档混合
    ├── diagram.png
    ├── examples.rst
    └── index.rst             # 根文档

**基于文件夹组织的好处：**

1. **更好的组织** - 相关内容保持在一起
2. **可扩展性** - 易于添加子章节和资源
3. **改进的导航** - 为读者提供逻辑层次结构
4. **可维护性** - 更容易管理相关资源
5. **更整洁的目录** - 没有文档和资源的混合


图片管理
------------------------------------------------------------------------------
为了一致且可维护的图片处理：

1. 在每个文档章节内创建 ``images/`` 子目录：

.. code-block:: text

    docs/source/user-guide/
    ├── images/
    │   ├── screenshot1.png
    │   └── diagram.png
    └── index.rst

2. 使用相对路径引用图片：

.. code-block:: rst

    .. image:: ./images/screenshot1.png
       :alt: 应用程序截图
       :width: 80%

3. **一致命名** - 为图片使用描述性的、带连字符的名称
4. **优化图片** - 压缩图片以减小大小而不牺牲质量
5. **适当的替代文本** - 始终包含描述性替代文本以提高可访问性
6. **版本控制** - 在界面变更时更新图片，保持与文本的一致性


多语言支持
------------------------------------------------------------------------------
如果您希望每个 HTML 页面都支持多种语言，官方方法过于复杂，不推荐使用。基本上它的做法是：

1. 使用 `gentext 插件 <https://www.gnu.org/software/gettext/manual/gettext.html#Introduction>`_ 将文档翻译成目标语言 - 但是，翻译质量很差。
2. 使用 `readthedocs.org 上的多语言功能 <https://docs.readthedocs.com/platform/stable/localization.html>`_，但这需要维护多个 Git 仓库，这使得它们难以保持同步。

相反，我建议遵循 :ref:`cn-sphinx-doc-style-guide-page` 中定义的样式，并使用像 ``_es.rst`` 或 ``_cn.rst`` 这样的后缀来表示同一文档的不同语言版本。您的文件结构可能如下所示：

.. code-block::

    tutorial
    |--- index.rst      # 英语（默认）
    |--- index_es.rst   # 西班牙语
    |--- index_cn.rst   # 中文

在每个 ``.rst`` 文件的开头，定义一个引用链接，如 ``.. _en_tutorial:``、``.. _es_tutorial:`` 或 ``.. _cn_tutorial:``。然后，在顶级标题下插入以下片段，作为语言切换器：

.. code-block::

    - :ref:`English <en_tutorial>`
    - :ref:`española <es_tutorial>`
    - :ref:`中文 <cn_tutorial>`

当您需要为非默认（非英语）子文档使用 ``.. autotoctree::`` 时，可以使用 ``:index_file:`` 选项指定特定语言的索引文件，如下所示：

.. code-block::

    .. autotoctree::
        :maxdepth: 1
        :index_file: index_cn.rst
