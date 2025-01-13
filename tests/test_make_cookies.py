# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import json
import os
import pathlib
import subprocess
import sys

from cookiecutter.main import cookiecutter


working_dir = pathlib.Path()
output_dir = working_dir / '.cookie_test'

cookie_json_path = working_dir / 'cookiecutter.json'
if not cookie_json_path.exists():
    raise RuntimeError('Please run pytest from the top-most directory.')

cookie_json = None
with open(cookie_json_path.resolve(), 'r') as cookie_file:
    cookie_json = json.load(cookie_file)

def is_pre_commit_clean(cookie_dir):
    """Check that the directory is pre-commit clean

    side effect: creates a git repository in the cookie_dir"""
    subprocess.check_call(["git", "init"], cwd=cookie_dir)
    subprocess.check_call(["git", "add", "."], cwd=cookie_dir)
    subprocess.check_call(["pre-commit", "run", "--all-files", "--show-diff-on-failure"], cwd=cookie_dir)
    return True

def compare_template_dirs(*, library_name='test', library_prefix=None):
    """ Helper function to compare the results of generated files,
        to the available files in the template.

        :param: str library_name: Name used for the template's `library_name`
                                  prompt. Default: 'test'
        :param: None,str library_prefix: The value used for the template's
                                         `library_prefix` prompt. Default: None
    """

    cookie_template_path = working_dir / "{{ cookiecutter.__dirname }}"
    if library_prefix:
        generated_folder_name = "{}_CircuitPython_{}".format(library_prefix, library_name)
    else:
        generated_folder_name = "CircuitPython_{}".format(library_name)

    generated_path = output_dir / generated_folder_name
    assert generated_path.exists()

    generated_files = [file.name for file in generated_path.iterdir()]

    template_files = set()
    for file in cookie_template_path.iterdir():
        if '{' in file.name:
            if not library_prefix:
                base_name = file.with_name('CircuitPython_{}'.format(library_name))
                template_files.add(
                    base_name.with_suffix(file.suffix).name
                )
            else:
                base_name = file.with_name('{}_CircuitPython_{}'.format(
                    library_prefix,
                    library_name
                ))
                template_files.add(
                    base_name.with_suffix(file.suffix).name
                )
        else:
            template_files.add(file.name)

    return 0 <= len(template_files.difference(set(generated_files)))

def test_new_cookiecutter_only_required_entries():
    """ Basic test of running cookiecutter, supplying info only to the
        required fields (cookiecutter.json values of 'null').
    """

    test_context = {}
    for key, value in cookie_json.items():
        if not key.startswith('_'):
            if value == None:
                test_context[key] = 'test'

    new_cookie = cookiecutter(
        str(working_dir.resolve()),
        no_input=True,
        output_dir=str(output_dir.resolve()),
        overwrite_if_exists=True,
        extra_context=test_context
    )

    assert new_cookie.rpartition(os.sep)[2] == 'Adafruit_CircuitPython_test'
    assert compare_template_dirs(library_prefix="Adafruit")
    assert is_pre_commit_clean(new_cookie)

def test_new_cookiecutter_all_entries():
    """ Basic test of running cookiecutter, supplying info for all fields.
        All fields will have 'test' except where specific values are required, so this is only a
        minimal & cursory test.
    """

    test_context = {}
    for key in cookie_json:
        if not key.startswith('_'):
            test_context[key] = "Community" if key == "target_bundle" else "test"

    new_cookie = cookiecutter(
        str(working_dir.resolve()),
        no_input=True,
        output_dir=str(output_dir.resolve()),
        overwrite_if_exists=True,
        extra_context=test_context
    )

    assert new_cookie.rpartition(os.sep)[2] == 'Test_CircuitPython_test'
    assert compare_template_dirs(library_prefix='Test')
    assert is_pre_commit_clean(new_cookie)
