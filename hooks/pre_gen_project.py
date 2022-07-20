# SPDX-FileCopyrightText: 2022 Alec Delaney, written for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import cookiecutter
from pkg_resources import packaging

MIN_VERSION_SEMVER = "2.1"
MIN_VERSION = packaging.version.parse(MIN_VERSION_SEMVER)

user_version_semver = cookiecutter.__version__
user_version = packaging.version.parse(user_version_semver)

if MIN_VERSION > user_version:
    print("")
    print("!!! cookiecutter must be at a minimum of version", MIN_VERSION, "!!!")
    print("")
    raise SystemExit(1)
