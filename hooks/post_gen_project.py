import pathlib

CI_SERVICE = "{{ cookiecutter.ci_service }}"
AVAILABLE_CI = {
    "GitHub Actions": (".travis.yml",),
    "TravisCI": (".github",),
    "None": (".github", ".travis.yml")
}

ADAFRUIT_CI = "GitHub Actions"
TARGET_BUNDLE = "{{ cookiecutter.target_bundle }}"

def _remove_files(target):
    """ Remove all files from the path.

        :param: target: The `pathilb.Path` pointing to the desired path
                        to remove. Can be a file or directory.
    """

    if not target.is_dir():
        target.unlink()
    else:
        target_tree = sorted(
            list(target.rglob("*")),
            reverse=True
        )

        for target_path in target_tree:
            if target_path.is_dir():
                target_path.rmdir()
            else:
                target_path.unlink()

        target.rmdir()

def finalize_ci_files():
    """ Removes the undesired template files, based on the choice of
        cookiecutter.ci_service.
    """
    working_dir = pathlib.Path.cwd()

    for ci_target in AVAILABLE_CI[CI_SERVICE]:
        target_path = working_dir / ci_target
        _remove_files(target_path)

if __name__ == "__main__":
    if TARGET_BUNDLE == "Adafruit" and CI_SERVICE != ADAFRUIT_CI:
        raise SystemExit(
            "\nLibraries targeted for the Adafruit Bundle must use GitHub Actions "
            "as their CI service.\n"
        )
    finalize_ci_files()
