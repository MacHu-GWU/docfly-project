.. _cn-docfly-quick-start:

docfly 快速开始
==============================================================================
- :ref:`English <en-docfly-quick-start>`
- :ref:`中文 <cn-docfly-quick-start>`


关于 docfly
------------------------------------------------------------------------------
``docfly`` 是一个强大的工具，通过自动化重复性任务来简化 `Sphinx 文档 <http://www.sphinx-doc.org/en/stable/index.html>`_ 的创建过程。本指南将帮助您快速实现 docfly 的两个关键功能：

1. **自动生成 API 参考文档**：从 Python 源代码生成全面的 API 文档
2. **自动生成目录**：创建并维护与文件夹结构保持同步的 ``toctree`` 指令

让我们通过实例了解如何使用这些功能。


安装 docfly
------------------------------------------------------------------------------
首先，通过 pip 安装 docfly：

.. code-block:: bash

    pip install "docfly>=3.0.0,<4.0.0"


自动生成 API 参考文档
------------------------------------------------------------------------------
**问题**：Sphinx 可以使用 `autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_ 扩展从源代码中提取文档字符串来创建 API 文档，但您仍需为每个模块、类和函数手动创建 `.rst` 文件——对于大型项目可能需要创建数百个文件。

**解决方案**：docfly 自动扫描您的包结构并生成所有必要的 `.rst` 文件，包含适当的 autodoc 指令。

**实现步骤**：

在 Sphinx 的 ``conf.py`` `配置文件 <https://www.sphinx-doc.org/en/master/usage/configuration.html>`_ 中添加以下代码：

.. code-block:: python

    from pathlib import Path
    import docfly.api as docfly
    import your_package  # 在此导入您的包

    # 配置 API 文档生成
    docfly.ApiDocGenerator(
        # 输出 .rst 文件的目录，它将是 ``conf.py`` 文件同级的 ``api`` 子目录
        dir_output=Path(__file__).parent.joinpath("api"),
        # 您的包名
        package_name=your_package.__name__,
        ignore_patterns=[
            # 指定要排除的任何模块或包
            f"{your_package.__name__}.tests",
            f"{your_package.__name__}.vendor",
            f"{your_package.__name__}._version.py",
        ],
    ).fly()

**结果**：下次当您运行 ``sphinx-build -b html docs/source build`` 构建文档时（假设 sphinx 配置文件位于 ``docs/source/conf.py``），``conf.py`` 中的这段代码将自动运行并生成如下文件夹结构：

.. code-block::

    docs/source/api/your_package/
    docs/source/api/your_package/subpackage/__init__.rst
    docs/source/api/your_package/subpackage/module.rst
    ...
    docs/source/api/your_package/__init__.rst
    docs/source/api/your_package/module.rst
    ...


自动生成目录
------------------------------------------------------------------------------
**问题**：手动维护 ``.. toctree::`` 指令需要在每次添加、删除或重命名文档文件时更新它们。

**解决方案**：docfly 的 ``.. autotoctree::`` 指令会自动发现并链接到包含索引文件的子目录。

**实现步骤**：

1. 首先，在 Sphinx 的 ``conf.py`` `配置文件 <https://www.sphinx-doc.org/en/master/usage/configuration.html>`_ 中启用 docfly 指令：

.. code-block:: python

    extensions = [
        # ... 其他扩展
        'docfly.directives',  # 启用 docfly 指令
    ]

2. 按照 :ref:`Sphinx 文档项目规范 <cn-sphinx-doc-style-guide>` 组织您的文档。例如：

    .. code-block:: text

        docs/
        ├── source/
        │   ├── index.rst
        │   ├── installation/
        │   │   └── index.rst
        │   ├── tutorial/
        │   │   └── index.rst
        │   └── advanced/
        │       └── index.rst

3. 使用 ``autotoctree`` 指令替代手动 toctree 指令：

.. dropdown:: source/index.rst

    .. code-block:: rst

        欢迎！
        --------

        .. autotoctree::
            :maxdepth: 1

**结果**：docfly 会自动发现所有带有索引文件的子目录，提取它们的标题，并创建格式正确的 toctree 指令。当您添加新章节时，它们会自动出现在目录中，无需手动更新。
