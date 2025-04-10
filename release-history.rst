.. _release_history:

Release and Version History
==============================================================================


Backlog (TODO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


3.0.0 (2025-04-10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**💥Breaking Change**

- Prior to 2.X.Y, the package maintained compatibility with Python 2.7 ~ 3.8, which came with significant technical burden. In 3.X.Y, we reworked the public API, greatly improved the API design, unit tests, and documentation. The package now only supports Python 3.9+.

**Features and Improvements**

- Now we support the following Public APIs:
    - ``docfly.api.ApiDocGenerator``
    - ``docfly.api.IndexFileNotFoundError``
    - ``docfly.api.PageFolder``
    - ``docfly.api.AutoTocTree``
    - ``docfly.api.directives``

**Minor Improvements**

- Add support for ``nbconvert>=7.16.5`` due to a change in the MIME type of Raw ReStructuredText cells from ``text/restructuredtext`` to ``text/x-rst``.

**Bugfixes**

**Miscellaneous**

- Migrate to ``https://github.com/MacHu-GWU/cookiecutter-pywf_open_source@0.1.1`` code skeleton.


2.0.3 (2024-02-02)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- Fix a bug that unable to locate the notebook title when the header 1 is a raw-restructuredText cell.


2.0.2 (2024-01-12)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Minor Improvements**

- Upgrade picage to 0.2.2 to support both hyphen and underscore in package names.


2.0.1 (2023-08-11)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Breaking change**

- from 2.X, the ``.. autotoctree::`` directive's ``:index_file:`` option should only include the file base name. For example, if you want to include ``index.rst``, you should define ``:index_file: index``. This is because we start to support more file extension like ``.ipynb``.

**Features and Improvements**

- Add support to automatically create ``.. toctree`` directive for folder that has an ``index.ipynb``.


1.1.1 (2023-02-27)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Miscellaneous**

- upgrade vendor package ``picage`` to 0.2.1.
- drop support for <=3.6, only support >=3.7


1.0.2 (2021-11-28)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Minor Improvements**

- add :attr:`docfly.doctreeArticalFolder.DEFAULT_INDEX_FILE` constant, allow changing default index file by editing one line of code.


1.0.1 (2021-11-23)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add directive option: ``:index_file: index.rst`` for ``.. autotoctree::``. Allow generate toctree other than ``index.rst``
- add multi language best practice guide

**Minor Improvements**

- migrate CI from travis.ci to Github CI
- change docfly doc theme to furo

**Miscellaneous**

- start using trunkbase git workflow


0.0.18 (2020-04-15)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- allow ``.. autotoctree::`` to detect header line if it use ``.. include:: other-file.rst`` at the top, then it exam after the ``other-file.rst`` merged into the original rst file.


0.0.17 (2018-11-30)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Now I finally know how to write sphinx extension correctly!**

**Features and Improvements**

- now docfly can be used as a sphinx extensions.
- ``.. articles::`` can be replaced by ``.. autotoctree::``


0.0.16 (2018-10-16)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Automatic API Reference Doc Generation.
- Easy Table of Content directive Generation (``.. toctree::``).


0.0.1 (2015-08-13)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- First release
