.. _en-docfly-quick-start:

docfly Quick Start
==============================================================================
- :ref:`English <en-docfly-quick-start>`
- :ref:`中文 <cn-docfly-quick-start>`


About docfly
------------------------------------------------------------------------------
``docfly`` is a powerful tool that simplifies the creation of `Sphinx documentation <http://www.sphinx-doc.org/en/stable/index.html>`_ by automating repetitive tasks. This guide will help you quickly implement docfly's two key features:

1. **Automatic API Reference Documentation**: Generate comprehensive API documentation from your Python source code
2. **Automatic Table of Contents**: Create and maintain ``toctree`` directives that stay in sync with your folder structure

Let's get started with practical examples of how to use each feature.


Setting Up docfly
------------------------------------------------------------------------------
First, install docfly via pip:

.. code-block:: bash

    pip install "docfly>=3.0.0,<4.0.0"


Auto API Reference Documentation
------------------------------------------------------------------------------
**The Problem**: Sphinx can extract docstrings from your source code to create API documentation using the `autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_ extensions, but you still need to manually create `.rst` files for each module, class, and function - potentially hundreds of files for large projects.

**The Solution**: docfly automatically scans your package structure and generates all necessary `.rst` files with proper autodoc directives.

**Implementation Steps**:

Add the following code to your Sphinx ``conf.py`` `config file <https://www.sphinx-doc.org/en/master/usage/configuration.html>`_:

.. code-block:: python

    from pathlib import Path
    import docfly.api as docfly
    import your_package  # Import your package here

    # Configure API Documentation Generation
    docfly.ApiDocGenerator(
        # Output directory for .rst files, it will be an ``api`` subdirectory
        # next to your ``conf.py`` file
        dir_output=Path(__file__).parent.joinpath("api"),
        # Your package name
        package_name=your_package.__name__,
        ignore_patterns=[
            # Specify any modules or packages to exclude
            f"{your_package.__name__}.tests",
            f"{your_package.__name__}.vendor",
            f"{your_package.__name__}._version.py",
        ],
    ).fly()

**Result**: Next time when you run ``sphinx-build -b html docs/source build`` to build you doc (let's say the sphinx config file is at ``docs/source/conf.py``), this code snippet in your ``conf.py`` will automatically run and generate a folder structure like this::

.. code-block::

    docs/source/api/your_package/
    docs/source/api/your_package/subpackage/__init__.rst
    docs/source/api/your_package/subpackage/module.rst
    ...
    docs/source/api/your_package/__init__.rst
    docs/source/api/your_package/module.rst
    ...


Automatic Table of Contents
------------------------------------------------------------------------------
**The Problem**: Maintaining ``.. toctree::`` directives manually requires updating them each time you add, remove, or rename documentation files.

**The Solution**: docfly's ``.. autotoctree::`` directive automatically discovers and links to subdirectories containing index files.

**Implementation Steps**:

1. First, enable docfly's directives in your Sphinx ``conf.py`` `config file <https://www.sphinx-doc.org/en/master/usage/configuration.html>`_:

.. code-block:: python

    extensions = [
        # ... other extensions
        'docfly.directives',  # Enable docfly directives
    ]

2. Organize your documentation following the :ref:`Sphinx Style Guide <en-sphinx-doc-style-guide>`. For example:

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

3. Use the ``autotoctree`` directive in place of manual toctree directives:

.. dropdown:: source/index.rst

    .. code-block:: rst

        Welcome!
        --------

        .. autotoctree::
            :maxdepth: 1

**Result**: docfly automatically discovers all subdirectories with index files, extracts their titles, and creates a properly formatted toctree directive. When you add new sections, they appear in the table of contents without manual updates.
