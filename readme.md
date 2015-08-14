# docfly项目

docfly是一个用于快速初始化python项目的API文档树文件的工具。

在python社区, 最常用的项目文档工具是[sphinx](http://sphinx-doc.org/)。虽然sphinx提供了很多工具能方便用户构建自己的文档网站, 但是用户仍然需要自己设计自己的文档结构。对于Python项目, 吸收了许多开源项目的文档经验之后, 我们制定了一套项目文档结构标准。


## 实际案例

假设我们的项目目录的包和模块的组织结构如下所示, 在此前提下进行文档网站的设计。

```Python
|---toppackage
	|---subpackage1
		|---__init__.py
		|---module11.py
		|---module12.py
	|---subpackage2
		|---__init__.py
		|---module21.py
		|---module22.py
	|---__init__.py
	|---module1.py
	|---module2.py
```

文档网站内容包含三大模块:

1. 用restructuredText文件撰写的文档书, 组织结构上按照一般的出版物的标准, 按照章(Chapter), 节(Section)的方式, 用更友好的语言针对项目的用途, 具体的例子进行介绍。

2. 用autodoc扩展自动生成的API文档, 组织结构上跟Python包组织的结构一样, 自动提取docstring, 生成带索引的API参考文档。

3. 项目相关信息的介绍, 主要包括项目的主旨, 开发团队, 版权, 联系方式等信息。

这三个部分中, 第一部分和第三部分都由用户自己根据需要组织, 而第二部分的API文档, 我们需要根据Python包的组织结构, 生成类似的文档树文件结构。这部分繁琐的工作我们可以使程序为我们自动生成, 这就是docfly的主要功能。


## index.rst主页的内容

主页应当包含一些对于项目的基本介绍

**Table of Content**

这部分内容由用户手动撰写。

```
|---Chapter1
	|---section1.1
	|---section1.2
	...
|---Chapter2
	|---section2.1
	|---section2.2
	...
...
|---ChapterN
	|---sectionN.1
	|---sectionN.2
	...
```

**Indices and tables**

这部分内容由docfly自动生成。

Index

```
A | B | C ... X | Y | Z

A
------


B
------

...


Z
------
```

Module Index

```
|---toppackage
	|---subpackage1
		|---module11
		|---module12
	|---subpackage2
		|---module21
		|---module22
	|---module1
	|---module2
```

## 详细文档

在docfly-project项目目录下, 有一个示例项目toppackage-project。我们下面以这个项目为例, 为这个项目建立一个标准化的文档网站。([成品网站Demo点这里](http://toppackage-project.readthedocs.org/en/latest/index.html))

首先要确保成功安装了[sphinx](http://sphinx-doc.org/latest/install.html)

首先进入docfly项目根目录

```console
$ cd docfly-project
```

安装docfly

```console
$ python setup.py build
$ python setup.py install
```

安装toppackage

```console
$ cd toppackage-project
$ python setup.py build
$ python setup.py install
```

使用[sphinx入门教程](http://sphinx-doc.org/tutorial.html)中的sphinx-quickstart生成文档项目。确保有`make.bat`, `conf.py`, `index.rst`等这些由sphinx自动生成的文件。

然后使用docfly生成文档书。

首先建立一个Python文件, 例如`test.py`, 并填入如下内容。

```python
from docfly import Docfly

docfly = Docfly("toppackage")
docfly.fly()
```

执行之后, 则会在当前目录下生成一个`_source`文件夹, 里面有一个`toppackage`的文件夹, 将这个文件夹拷贝到sphinx的文档源文件所在的目录。即跟`conf.py`和`index.rst`文件在一个目录下。

在此之后, 在`toppackage-project`目录下执行

```console
$ make html
```

然后打开build文件夹中的index.html文件, 即可看到自动生成的[index](http://toppackage-project.readthedocs.org/en/latest/genindex.html), [module index](http://toppackage-project.readthedocs.org/en/latest/py-modindex.html)页面, 查看API文档的索引了。
