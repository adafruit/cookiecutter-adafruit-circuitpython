import cookiecutter

MIN_VERSION = 2.1

semver = cookiecutter.__version__
major, minor, _ = semver.split(".")
maj_min_ver = float(major + "." + minor)

if maj_min_ver < MIN_VERSION:
    print("cookiecutter must be at a minimum of version", MIN_VERSION)
    raise SystemExit(1)
