{% if cookiecutter.library_prefix -%}
    {% set prefix = cookiecutter.library_prefix | capitalize + "_" -%}
{% else -%}
    {% set prefix = '' -%}
{% endif -%}
{% set repo_name = prefix + "CircuitPython_" + cookiecutter.library_name -%}
{% set full_repo_name = cookiecutter.github_user + "/" + repo_name -%}
{%- set pypi_name = cookiecutter.library_name|lower|replace("_", "-") -%}
Introduction
============

.. image:: https://readthedocs.org/projects/{% if cookiecutter.library_prefix %}{{ cookiecutter.library_prefix | lower | replace("_", "-")}}-{% endif %}circuitpython-{{ cookiecutter.library_name | lower }}/badge/?version=latest
{%- if cookiecutter.library_prefix %}
    :target: https://circuitpython.readthedocs.io/projects/{{ cookiecutter.library_name | lower }}/en/latest/
{%- else %}
    :target: https://circuitpython-{{ cookiecutter.library_name | lower }}.readthedocs.io/
{%- endif %}
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://github.com/{{ full_repo_name }}/workflows/Build%20CI/badge.svg
    :target: https://github.com/{{ full_repo_name }}/actions
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

{% if cookiecutter.library_description != "" %}
    {{- cookiecutter.library_description }}
{% else %}
.. todo:: Describe what the library does.
{% endif %}

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
{%- if cookiecutter.requires_bus_device in ["y", "yes"] %}
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_
{%- endif %}
{%- if cookiecutter.requires_register in ["y", "yes"] %}
* `Register <https://github.com/adafruit/Adafruit_CircuitPython_Register>`_
{%- endif %}

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

Installing from PyPI
=====================
.. note:: This library is not available on PyPI yet. Install documentation is included
   as a standard element. Stay tuned for PyPI availability!

.. todo:: Remove the above note if PyPI version is/will be available at time of release.
   If the library is not planned for PyPI, remove the entire 'Installing from PyPI' section.

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-{{ cookiecutter.library_name|lower }}/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-{{ pypi_name }}

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-{{ pypi_name }}

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-{{ pypi_name }}

Usage Example
=============

.. todo:: Add a quick, simple example. It and other examples should live in the examples folder and be included in docs/examples.rst.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/{{ full_repo_name }}/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
