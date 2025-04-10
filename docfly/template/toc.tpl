.. toctree::
    :maxdepth: {{ maxdepth }}

    {% for child_page_folder in child_page_folders -%}
    {{ child_page_folder.title }} <{{ child_page_folder.path_str }}>
    {% endfor -%}
