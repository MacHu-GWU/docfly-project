# Jupyter Notebook 与 DocFly 框架的高级使用技巧

有关使用 nbsphinx 扩展的基本信息，请参阅[官方文档](https://nbsphinx.readthedocs.io/)。本指南重点介绍将 Jupyter Notebook 与 DocFly 框架集成用于 Sphinx 文档的高级技术。

## 在 Jupyter Notebook 中使用 RestructuredText

Jupyter Notebook 主要使用 Markdown，但您仍然可以通过使用原始单元格（Raw cells）在 Notebook 中使用 RestructuredText (RST) 或 Sphinx 语法：

1. 创建一个新单元格并将其类型更改为"Raw"
2. 点击"COMMON TOOLS"按钮
3. 将"Raw NBConvert Format"设置为"ReStructured Text"

## 文档标题设置

当设置能被 nbsphinx 正确检测到的文档标题用于目录时，请在 Raw 单元格中使用以下模式：

```
.. _unique-reference-id:

文档标题
================================================================================
```

这个单元格在 notebook 文件中的 JSON 表示将是：

```json
  {
   "cell_type": "raw",
   "id": "d1454a25-eb5f-4eb3-b5fb-f1ac1f012b18",
   "metadata": {
    "editable": true,
    "raw_mimetype": "text/restructuredtext", // <--- mimitype
    "slideshow": {
     "slide_type": ""
    },
    "tags": []
   },
   "source": [
    ".. _unique-reference-id:\n",
    "\n",
    "文档标题\n",
    "================================================================================\n",
    "..."
   ]
  },
```

⚠️ 已知问题：自 2025 年 1 月 2 日起，nbsphinx 存在一个 bug，当使用 RestructuredText 单元格作为文档标题时，会阻止正确创建 TOC 链接。详见 [GitHub PR #834](https://github.com/spatialaudio/nbsphinx/pull/834)。

## 文档交叉引用

要使用 Sphinx 的 ``:ref:`` [交叉引用语法](https://www.sphinx-doc.org/en/master/usage/referencing.html#role-ref) 创建文档之间的引用：

## 从其他文档引用此点：

1. 在任何 RST 内容中定义一个引用点：

```
.. _unique-ref-link:

任何内容
```

2. 从任何其他文档引用此点：

```
更多信息，请参见 :ref:`unique-ref-link`。
```


```python

```
