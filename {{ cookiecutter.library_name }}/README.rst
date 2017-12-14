
Introduction
============

.. image:: https://readthedocs.org/projects/{% if cookiecutter.library_prefix %}{{ cookiecutter.library_prefix | lower }}-{% endif %}circuitpython-{{ cookiecutter.library_name | lower }}/badge/?version=latest
{% if cookiecutter.library_prefix %}
    :target: https://circuitpython.readthedocs.io/projects/{{ cookiecutter.library_name | lower }}/en/latest/
{% else %}
    :target: https://circuitpython-{{ cookiecutter.library_name | lower }}.readthedocs.io/
{% endif %}
    :alt: Documentation Status

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

TODO

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
{%- if cookiecutter.depends_on_bus_device != "" %}
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_
{%- endif %}
{%- if cookiecutter.depends_on_register != "" %}
* `Register <https://github.com/adafruit/Adafruit_CircuitPython_Register>`_
{%- endif %}

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
=============

TODO

API Reference
=============

.. toctree::
   :maxdepth: 2

   api

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/{{ cookiecutter.github_user }}/{% if cookiecutter.library_prefix %}{{ cookiecutter.library_prefix | capitalize }}_{% endif %}CircuitPython_{{ cookiecutter.library_name }}/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Building locally
================

To build this library locally you'll need to install the
`circuitpython-build-tools <https://github.com/adafruit/circuitpython-build-tools>`_ package.

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install circuitpython-build-tools

Once installed, make sure you are in the virtual environment:

.. code-block:: shell

    source .env/bin/activate

Then run the build:

.. code-block:: shell

    circuitpython-build-bundles --filename_prefix {% if cookiecutter.library_prefix %}{{ cookiecutter.library_prefix | lower }}-{% endif %}circuitpython-{{ cookiecutter.library_name | lower }} --library_location .
