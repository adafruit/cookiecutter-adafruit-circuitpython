
.. If you created a package, create one automodule per module in the package.

.. If your library file(s) are nested in a directory (e.g. /adafruit_foo/foo.py)
.. use this format as the module name: "adafruit_foo.foo"

.. automodule:: {% if cookiecutter.library_prefix %}{{ cookiecutter.library_prefix | lower }}_{% endif %}{{ cookiecutter.library_name | lower }}
   :members:
