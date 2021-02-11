# SPDX-FileCopyrightText: 2021 Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Hooks that run before the template is rendered.
"""

import sys

github_user = '{{cookiecutter.github_user}}'

if github_user in ["", None]:
    print("ERROR: github_user is a required field.")
    # exits with status 1 to indicate failure
    sys.exit(1)
