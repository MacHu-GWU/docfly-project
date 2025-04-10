.. _en-sphinx-doc-style-guide:

Sphinx Style Guide
==============================================================================
- :ref:`English <en-sphinx-doc-style-guide>`
- :ref:`中文 <cn-sphinx-doc-style-guide>`

These best practices stem from extensive experience with real-world projects. Following established conventions makes your documentation more readable while helping you avoid common pitfalls through proven patterns.

This guide presents best practices developed through years of working with Sphinx-doc, building complex documentation systems with API references, hierarchical structures, and multilingual support. By adhering to these recommendations, you can dramatically reduce repetitive work and focus on creating valuable content.


File Organization
------------------------------------------------------------------------------
Organize your Sphinx documentation in a logical hierarchy. A typical structure might look like:

.. code-block:: text

    docs/
    ├── source/             # Source files (.rst, .md, .ipynb)
    │   ├── _static/        # Static files (CSS, images)
    │   ├── _templates/     # Custom templates
    │   ├── conf.py         # Sphinx configuration
    │   ├── index.rst       # Main entry point
    │   ├── installation/   # Section directories
    │   │   └── index.rst
    │   ├── usage/
    │   │   └── index.rst
    │   └── api/            # API documentation (can be auto-generated)
    │       └── ...
    └── build/              # Generated output (HTML, PDF, etc.)
        └── html/           # Generated HTML files


Naming Conventions
------------------------------------------------------------------------------
For consistent, maintainable documentation:

1. **Avoid spaces in filenames and directories** - Use hyphens or underscores instead
2. **Prefer hyphens over underscores** - Hyphens are valid in URLs, while underscores can cause issues
3. **Use kebab-case for file and directory names** - For example, `user-guide.rst` not `UserGuide.rst`
4. **Stick to ASCII characters** - Use English names and alphanumeric characters when possible
5. **Be consistent** - Choose one naming convention and apply it throughout your project


.. _en-sphinx-doc-style-guide-page:

Page Organization
------------------------------------------------------------------------------
**Recommended: Use Folder-Based Structure**

Instead of a flat hierarchy with many .rst files, organize each major documentation section as a folder with an index file:

.. code-block:: text

    # RECOMMENDED
    docs/source/
    ├── user-guide/           # A directory for the "User Guide" section
    │   ├── index.rst         # The main content (equivalent to user-guide.rst)
    │   ├── images/           # Section-specific images
    │   │   ├── screenshot1.png
    │   │   └── diagram.png
    │   └── examples/         # Additional subsection files
    │       └── index.rst
    └── index.rst             # Root document

Rather than:

.. code-block:: text

    # NOT RECOMMENDED
    docs/source/
    ├── user-guide.rst        # A single file
    ├── screenshot1.png       # Images mixed with documents
    ├── diagram.png
    ├── examples.rst
    └── index.rst             # Root document

**Benefits of folder-based organization:**

1. **Better organization** - Related content stays together
2. **Scalability** - Easy to add subsections and resources
3. **Improved navigation** - Logical hierarchy for readers
4. **Maintainability** - Easier to manage related assets
5. **Cleaner directories** - No mixture of documents and resources


Image Management
------------------------------------------------------------------------------
For consistent and maintainable image handling:

1. Create an ``images/`` subdirectory within each documentation section:

.. code-block:: text

    docs/source/user-guide/
    ├── images/
    │   ├── screenshot1.png
    │   └── diagram.png
    └── index.rst

2. Reference images using relative paths:

.. code-block:: rst

    .. image:: ./images/screenshot1.png
       :alt: Application Screenshot
       :width: 80%

3. **Consistent naming** - Use descriptive, hyphenated names for images
4. **Optimize images** - Compress images to reduce size without sacrificing quality
5. **Proper alt text** - Always include descriptive alt text for accessibility
6. **Versioning** - Update images when interfaces change, maintaining consistency with text


Multi-Language Support
------------------------------------------------------------------------------
If you want every HTML page to support multiple languages, the `official methods <https://www.sphinx-doc.org/en/master/usage/advanced/intl.html>`_ are overly complicated and not recommended. Basically what it does is:

1. Use the `gentext plugin <https://www.gnu.org/software/gettext/manual/gettext.html#Introduction>`_ to translate the documentation into the target language - however, the translation quality is very poor.
2. Use the `multilingual feature on readthedocs.org <https://docs.readthedocs.com/platform/stable/localization.html>`_, but this requires maintaining multiple Git repositories, which makes it difficult to keep them synchronized.

Instead, I recommend following the style defined in :ref:`en-sphinx-doc-style-guide-page`, and using suffixes like ``_es.rst`` or ``_cn.rst`` to indicate different language versions of the same document. Your file structure might look like this::

    tutorial
    |--- index.rst      # English (default)
    |--- index_es.rst   # Spanish (default)
    |--- index_cn.rst   # Chinese (default)

At the beginning of each ``.rst`` file, define a reference link such as ``.. _en_tutorial:``, ``.. _es_tutorial:``, or ``.. _cn_tutorial:``. Then, insert the following snippet below your top-level header to serve as a language switcher::

    - :ref:`English <en_tutorial>`
    - :ref:`española <es_tutorial>`
    - :ref:`中文 <cn_tutorial>`

When you need to use ``.. autotoctree::`` for non-default (non-English) sub-documents, you can specify the language-specific index file with the ``:index_file:`` option, like this:

When you need ``.. autotoctree::`` for non-default (english) sub documents, you can use this option ``:index_file: index_cn.rst`` to locate sub documents that is in specific language:::

    .. autotoctree::
        :maxdepth: 1
        :index_file: index_cn.rst
