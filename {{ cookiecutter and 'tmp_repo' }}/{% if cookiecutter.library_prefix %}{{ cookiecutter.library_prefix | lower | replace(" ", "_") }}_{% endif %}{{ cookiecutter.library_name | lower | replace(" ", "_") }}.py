# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) {% now 'utc', '%Y' %} {{ cookiecutter.author_name }}{% if cookiecutter.company %} for {{ cookiecutter.company }}{% endif %}
#
# SPDX-License-Identifier: MIT
"""
`{% if cookiecutter.library_prefix %}{{ cookiecutter.library_prefix | lower | replace(" ", "_") }}_{% endif %}{{ cookiecutter.library_name | lower | replace(" ", "_") }}`
================================================================================

{% if cookiecutter.library_description != "" %}
    {{- cookiecutter.library_description }}
{% else %}
.. todo:: Describe what the library does.
{% endif %}

* Author(s): {{ cookiecutter.author_name }}

Implementation Notes
--------------------

**Hardware:**

.. todo:: Add links to any specific hardware product page(s), or category page(s).
  Use unordered list & hyperlink rST inline format: "* `Link Text <url>`_"

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

.. todo:: Uncomment or remove the Bus Device and/or the Register library dependencies
  based on the library's use of either.

# * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
# * Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register
"""

# imports

{% if cookiecutter.target_bundle != 'CircuitPython Org' -%}
    {%- if cookiecutter.library_prefix -%}
        {%- set repo_name = (cookiecutter.library_prefix | capitalize) -%}
        {%- set repo_name = repo_name + '_CircuitPython_' -%}
        {%- set repo_name = repo_name + cookiecutter.library_name | replace(" ", "_") -%}
    {%- else -%}
        {%- set repo_name = 'CircuitPython_' -%}
        {%- set repo_name = repo_name + cookiecutter.library_name | replace(" ", "_") -%}
    {%- endif -%}
{% else -%}
    {%- set repo_name = 'CircuitPython_Org_' + cookiecutter.library_name | replace(" ", "_") -%}
{% endif -%}

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/{{ cookiecutter.github_user }}/{{ repo_name }}.git"
