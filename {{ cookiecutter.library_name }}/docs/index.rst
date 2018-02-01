{% if cookiecutter.library_prefix -%}
    {% set prefix = cookiecutter.library_prefix + "_" -%}
{% else -%}
    {% set prefix = '' -%}
{% endif -%}
{% set repo_name = prefix + "CircuitPython_" + cookiecutter.library_name -%}
{% set full_repo_name = cookiecutter.github_user + "/" + repo_name -%}

.. include:: ../README.rst

Table of Contents
=================

.. toctree::
    :maxdepth: 4
    :hidden:

    self

.. toctree::
    :caption: Examples

    examples

.. toctree::
    :caption: API Reference
    :maxdepth: 3

    api

.. toctree::
    :caption: Tutorials

.. todo:: Add any Learn guide links here. If there are none, then simply delete this todo and leave
    the toctree above for use later.

.. toctree::
    :caption: Related Products

.. todo:: Add any product links here. If there are none, then simply delete this todo and leave
    the toctree above for use later.

.. toctree::
    :caption: Other Links

    Download <https://github.com/{{ full_repo_name }}/releases/latest>
    CircuitPython Reference Documentation <https://circuitpython.readthedocs.io>
    CircuitPython Support Forum <https://forums.adafruit.com/viewforum.php?f=60>
    Discord Chat <https://adafru.it/discord>
    Adafruit Learning System <https://learn.adafruit.com>
    Adafruit Blog <https://blog.adafruit.com>
    Adafruit Store <https://www.adafruit.com>

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
