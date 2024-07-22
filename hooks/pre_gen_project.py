# SPDX-FileCopyrightText: 2022 Alec Delaney, written for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import cookiecutter
from packaging.version import parse

MIN_VERSION_SEMVER = "2.1"
MIN_VERSION = parse(MIN_VERSION_SEMVER)

user_version_semver = cookiecutter.__version__
user_version = parse(user_version_semver)

if MIN_VERSION > user_version:
    print("")
    print("!!! cookiecutter must be at a minimum of version", MIN_VERSION, "!!!")
    print("")
    raise SystemExit(1)
