{{ package.shortname }}
{{ "=" * package.shortname|length }}

.. automodule:: {{ package.fullname }}
    :members:

sub packages and modules
------------------------

.. toctree::
    :maxdepth: 1

    {% for pkg in package.sub_packages.values() -%}
    {% if not is_ignored(pkg, ignore_patterns) -%}
    {{ pkg.shortname }} <{{ pkg.shortname }}/__init__>
    {% endif -%}
    {% endfor -%}
    {% for mod in package.sub_modules.values() -%}
    {% if not is_ignored(mod, ignore_patterns) -%}
    {{ mod.shortname }} <{{ mod.shortname }}>
    {% endif -%}
    {% endfor -%}