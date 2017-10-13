
Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-{{ cookiecutter.library_name }}/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/{{ cookiecutter.library_name }}/en/latest/
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

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_{{ cookiecutter.library_name }}/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

API Reference
=============

.. toctree::
   :maxdepth: 2

   api
