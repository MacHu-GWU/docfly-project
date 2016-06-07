{{ package.name }}
{{ "=" * package.name|length }}

.. automodule:: {{ package.fullname }}
    :members:

sub packages and modules
------------------------

.. toctree::
   :maxdepth: 1

    {% for pkg in package.sub_packages.values() -%}
    {{ pkg.name }} <{{ pkg.name }}/__init__>
    {% endfor -%}
    {% for mod in package.sub_modules.values() -%}
    {{ mod.name }} <{{ mod.name }}>
    {% endfor -%}