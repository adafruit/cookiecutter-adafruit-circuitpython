
Introduction
============

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

This cookiecutter creates a project structure for a Adafruit CircuitPython
library.

To use:

.. code-block:: bash

  # The first time
  pip install cookiecutter

  cookiecutter gh:adafruit/cookiecutter-adafruit-circuitpython

Then, fill in the prompts.

Prompts
--------

* `library_name` - Shortest name for the library. Usually a chip name such as LIS3DH.
* `depends_on_bus_device` - Determines whether to add comments about a dependency on [BusDevice](https://github.com/adafruit/Adafruit_CircuitPython_BusDevice). Leave empty if the library won't use BusDevice.
* `depends_on_register` - Determines whether to add comments about a dependency on [Register](https://github.com/adafruit/Adafruit_CircuitPython_Register). Leave empty if the library won't use Register.
* `author` - Who you are! Sets the copyright to you.
* `github_user` - GitHub user or organization which will host this repo. For example, Adafruit funded libraries should say "adafruit" here.
* `library_prefix` - Used to prefix the code to the organization creating the library. For example, Adafruit supported libraries should say "adafruit" here. Do not add a - or _.
* `company` - Used to give Copyright credit to the company funding the library. For example, Adafruit funded libraries should say "Adafruit Industries" here.
