# SPDX-FileCopyrightText: 2021 Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Hooks that run before the template is rendered.
"""
import pathlib
import shutil
import sys


base_folder = pathlib.PosixPath().resolve()
docs_dir = base_folder / "docs"
sphinx_docs = "{{cookiecutter.sphinx_docs}}"

if sphinx_docs.lower() in ["n", "no"]:
    """
        Remove the Docs folder if the user doesn't want docs.
    """
    try:
        shutil.rmtree(docs_dir)
    except OSError as e:
        print("Error: %s : %s" % (docs_dir, e.strerror))
