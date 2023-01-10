{%- if cookiecutter.target_bundle != 'CircuitPython Org' -%}
    {%- if cookiecutter.library_prefix -%}
        {%- set repo_name = (cookiecutter.library_prefix | capitalize) -%}
        {%- set repo_name = repo_name + '_CircuitPython_' -%}
    {%- else -%}
        {%- set repo_name = 'CircuitPython_' -%}
    {%- endif -%}
    {%- set repo_name = repo_name + cookiecutter.library_name | replace(" ", "_") -%}
{%- else -%}
    {%- set repo_name = 'CircuitPython_Org_' + cookiecutter.library_name | replace(" ", "_") -%}
{%- endif -%}
{%- set full_repo_name = cookiecutter.github_user + "/" + repo_name -%}
{%- set pypi_name = cookiecutter.library_name|lower|replace("_", "-")|replace(" ", "-") -%}
{%- if cookiecutter.target_bundle == 'Adafruit' -%}
    {%- set docs_url = 'https://docs.circuitpython.org/projects/' + cookiecutter.library_name | lower | replace(" ", "-") + '/en/latest/' -%}
{%- else -%}
    {%- set docs_url = 'https://circuitpython-' + cookiecutter.library_name | lower | replace(" ", "-") | replace("_", "-") + '.readthedocs.io/' -%}
{%- endif -%}
Introduction
============

{% if cookiecutter.sphinx_docs | lower in ["yes", "y"] %}
.. image:: https://readthedocs.org/projects/{% if cookiecutter.library_prefix %}{{ cookiecutter.library_prefix | lower | replace("_", "-")}}-{% endif %}circuitpython-{{ cookiecutter.library_name | lower | replace(" ", "-") | replace("_", "-") }}/badge/?version=latest
{%- if cookiecutter.target_bundle == 'Adafruit' %}
    :target: {{ docs_url }}
{%- else %}
    :target: {{ docs_url }}
{%- endif %}
    :alt: Documentation Status
{% endif %}

{% if cookiecutter.target_bundle == 'Adafruit' -%}
.. image:: https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_Bundle/main/badges/adafruit_discord.svg
{%- else %}
.. image:: https://img.shields.io/discord/327254708534116352.svg
{%- endif %}
    :target: https://adafru.it/discord
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
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

{%- if cookiecutter.target_bundle == 'Adafruit' %}

.. todo:: Describe the Adafruit product this library works with. For PCBs, you can also add the
image from the assets folder in the PCB's GitHub repo.

`Purchase one from the Adafruit shop <http://www.adafruit.com/products/{{cookiecutter.adafruit_product_id}}>`_
{% endif -%}

Installing from PyPI
=====================
.. note:: This library is not available on PyPI yet. Install documentation is included
   as a standard element. Stay tuned for PyPI availability!

.. todo:: Remove the above note if PyPI version is/will be available at time of release.

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/{%- if cookiecutter.library_prefix -%}{{ cookiecutter.library_prefix }}-{%- endif -%}circuitpython-{{ pypi_name }}/>`_.
To install for current user:

.. code-block:: shell

    pip3 install {% if cookiecutter.library_prefix %}{{ cookiecutter.library_prefix }}-{% endif %}circuitpython-{{ pypi_name }}

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install {% if cookiecutter.library_prefix %}{{ cookiecutter.library_prefix }}-{% endif %}circuitpython-{{ pypi_name }}

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install {% if cookiecutter.library_prefix -%}{{ cookiecutter.library_prefix }}-{% endif -%}circuitpython-{{ pypi_name }}

Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install {{ cookiecutter.__libprefix }}{{ cookiecutter.__libname }}

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

.. todo:: Add a quick, simple example. It and other examples should live in the
examples folder and be included in docs/examples.rst.

Documentation
=============
API documentation for this library can be found on `Read the Docs <{{ docs_url }}>`_.

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/{{ full_repo_name }}/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
