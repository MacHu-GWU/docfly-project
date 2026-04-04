# -*- coding: utf-8 -*-

import subprocess
from docfly.paths import path_enum

bin_jupyter = path_enum.dir_venv_bin / "jupyter"

for path_notebook in path_enum.dir_docs_source.glob("**/*.ipynb"):
    if ".ipynb_checkpoints" in str(path_notebook):
        continue
    path_markdown = path_notebook.parent / f"{path_notebook.stem}.md"
    args = [
        f"{bin_jupyter}",
        "nbconvert",
        "--to",
        "markdown",
        str(path_notebook),
        "--output",
        str(path_markdown),
    ]
    cmd = " ".join(args)
    print(f"run command: {cmd}")
    subprocess.run(args, check=True)