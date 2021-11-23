.. _en_docfly_quick_start:

docfly Quick Start
==============================================================================

- :ref:`English <en_docfly_quick_start>`
- :ref:`中文 <cn_docfly_quick_start>`

``docfly`` helps you to reduce duplicate works building your documentation website with `sphinx-doc <http://www.sphinx-doc.org/en/stable/index.html>`_. The killer features are:

- Automatically generate API reference document with a few line of codes
- Automatically generate table of content (the ``.. toctree::`` directive) and the reference code to the sub documents.


Auto API Reference Document
------------------------------------------------------------------------------

There's a Sphinx doc feature that can automatically extract docstring from your source code, and generate API doc for you to search, reference. Howevery, **you still need to declare which package / module / class / method / function you want to include. It could be 1,000+ line of code to maintain in large project**.

Giving a package name, ``docfly`` can automatically generate those declaration files for your package, and keep your reference up-to-date when source code changes. You can find the example `here <https://github.com/MacHu-GWU/docfly-project/docs/source/conf.py>`_.

**Usage**

It's eazy, just add following code snippet to your ``conf.py`` file::

    import docfly

    #--- Api Reference Doc ---
    package_name = docfly.__name__

    docfly.ApiReferenceDoc(
        conf_file=__file__, # locate the path of conf.py
        package_name=package_name, # specify which package you want to generate api doc for
        ignored_package=[ # specify sub package / module you want to ignore
            "%s.pkg" % package_name,
        ]
    ).fly()

Basically it does three things:

1. tell ``docfly`` where is the ``conf.py`` file. So it can generate the ``.rst`` file accordingly.
2. tell ``docfly`` which package you want to generate api doc for.
3. tell ``docfly`` which sub package / module you want to ignore


Auto Table Of Content
------------------------------------------------------------------------------

A documentation website like a book. It usually use a hierarchy structure like Chapter, Section, ... We expect that it automatically generate the hyperlink from top to bottom.

The ``sphinx-doc`` `official doc <http://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#toctree-directive>`_ shows that you need to put this directive at where you want to generate table of content::

    .. toctree::
        :maxdepth: 1

        Title of your sub document <path-to-the-rst-file> # manual work
        ...

In other word, you still need to manually specify the title and path to the sub document, and you need to update the toc when sub documents changed.

The other ``docfly`` killer feature is that it provides a new directive ``.. autotoctree::`` can automatically generate the underlying ``.. toctree::`` directive for you if you are following the :ref:`Sphinx Style Guide <en_sphinx_doc_style_guide>`.

**Usage**

Add the following code snippet to ``conf.py``::

    extensions = [
        ...
        'docfly.directives', # enable docfly directives
        ...
    ]
