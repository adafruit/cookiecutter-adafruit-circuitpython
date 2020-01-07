
import json
import pathlib
import shutil
import sys

from cookiecutter.main import cookiecutter


# only verified on linux
if not sys.platform.startswith('linux'):
    raise RuntimeError('These tests are only verified to run on Linux systems.')

working_dir = pathlib.Path()
output_dir = working_dir / '.cookie_test'

cookie_json_path = working_dir / 'cookiecutter.json'
if not cookie_json_path.exists():
    raise RuntimeError('Please run pytest from the top-most directory.')

cookie_json = None
with open(cookie_json_path.resolve(), 'r') as cookie_file:
    cookie_json = json.load(cookie_file)

def overwrite_workaround():
    """ cookiecutter's `overwrite_if_exists=True` is currently broken.
        There is an accepted PR slated for release 1.8.0, but until
        it is released, we'll need to work around it.
    """
    if output_dir.exists():
        shutil.rmtree(str(output_dir.resolve()))


def compare_template_dirs(*, library_name='test', library_prefix=None):
    """ Helper function to compare the results of generated files,
        to the available files in the template.

        :param: str library_name: Name used for the template's `library_name`
                                  prompt. Default: 'test'
        :param: None,str library_prefix: The value used for the template's
                                         `library_prefix` prompt. Default: None
    """

    cookie_template_path = working_dir / '{{ cookiecutter.library_name }}'
    generated_path = output_dir / library_name

    assert generated_path.exists()

    generated_files = [file.name for file in generated_path.iterdir()]

    template_files = set()
    for file in cookie_template_path.iterdir():
        if '{' in file.name:
            if not library_prefix:
                base_name = file.with_name(library_name)
                template_files.add(
                    base_name.with_suffix(file.suffix).name
                )
            else:
                base_name = file.with_name('{}_{}'.format(
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

    # delete testing output directory if exists
    overwrite_workaround()

    test_context = {}
    for key, value in cookie_json.items():
        if value == None:
            test_context[key] = 'test'
        if key.startswith('_'):
            test_context[key] = value

    new_cookie = cookiecutter(
        str(working_dir.resolve()),
        no_input=True,
        output_dir=str(output_dir.resolve()),
        overwrite_if_exists=True,
        extra_context=test_context
    )

    assert new_cookie == '{}/test'.format(output_dir.resolve())
    assert compare_template_dirs()

def test_new_cookiecutter_all_entries():
    """ Basic test of running cookiecutter, supplying info for all fields.
        All fields will have 'test' as their value, so this is only a
        minimal & cursory test.
    """

    # delete testing output directory if exists
    overwrite_workaround()

    test_context = {}
    for key, value in cookie_json.items():
        if not key.startswith('_'):
            test_context[key] = 'test'
        else:
            test_context[key] = value

    new_cookie = cookiecutter(
        str(working_dir.resolve()),
        no_input=True,
        output_dir=str(output_dir.resolve()),
        overwrite_if_exists=True,
        extra_context=test_context
    )

    assert new_cookie == '{}/test'.format(output_dir.resolve())
    assert compare_template_dirs(library_prefix='test')
