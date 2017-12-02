docfly使用说明
==============================================================================
docfly是一个帮助你更容易地使用 `sphinx-doc <http://www.sphinx-doc.org/en/stable/index.html>`_ 来构建你的文档网站的工具。


API Reference
------------------------------------------------------------------------------

如果你在为你的Python代码写文档, Sphinx有一个杀手级的功能: 自动从源代码中摘取docstring, 生成API文档。 然后你就可以使用在你的文档中使用 ``:ref:`modindex``` 引用之。但是, 你需要手动编写大量代码, 告诉Sphinx哪些模块你想要自动为它生成文档。具体做法请参考 `这篇说明 <http://www.sphinx-doc.org/en/stable/ext/autodoc.html>`_。

**docfly** 的 **杀手级功能** 是, 自动分析你的源代码, 然后自动生成 ``:ref:`modindex``` 所需的一切文件。并且在你的源代码结构发生变化之后, 自动更新。下面我们就以docfly本项目本身为例进行说明。你可以在 `这里 <https://github.com/MacHu-GWU/docfly-project>`_ 找到本文档中的示例代码。

1. 在你的项目中创建一个 ``create_doctree.py`` 文件, 将其放在和你文档的source目录的旁边, 也同时是Makefile的旁边(当然你也可以放在任何地方, 不过就需要修改 ``dst`` 参数了), 文件内容如下::

	# Content of create_doctree.py

	import docfly

	#--- Api Reference Doc ---
	package_name = "docfly"

	doc = docfly.ApiReferenceDoc(
	    package_name,
	    dst="source", # your sphinx doc source destination
	    ignore=[
	        "%s.pkg" % package_name,
	        "%s.zzz_ezinstall.py" % package_name,
	    ]
	)
	doc.fly()

2. 如果是Windows, 创建一个 ``build_doc.bat`` 文件(如果是MacOS, Linux系统, 参考Windows命令行创建一个类似的Shell脚本即可), 将其放在 ``create_doctree.py`` 旁边, 内容如下::

	pushd "%~dp0"
	python create_doctree.py
	make html

这样你就可以通过双击, 一键Build你自带API文档的网站了。


Table of Content
------------------------------------------------------------------------------
写一个文档网站就像写一本书。分Chapter, Section, ... 一级一级的往下延伸。而我们希望能自动地从上往下, 为每一章生成它下面每一节的链接, 同理递归下去。

而docfly的另一个重要功能就是: 只要你按照 `Sphinx文档项目规范 <https://github.com/MacHu-GWU/docfly-project/blob/master/source/sphinx-doc-style-guide/content.rst>`_, 那么就可以使用docfly轻松生成章节, 目录的链接, 只要你在 ``create_doctree.py`` 文件中加入以下内容::

	# Uncomment this if you follow Sanhe's Sphinx Doc Style Guide
	#--- Manually Made Doc ---
	doc = docfly.DocTree("source")
	doc.fly()

同理, 你可以使用自动化批处理文件, 一键Build你的文档网站。