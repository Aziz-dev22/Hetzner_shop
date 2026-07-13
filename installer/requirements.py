"""
Hetzner Shop
Installation Requirements Checker
"""

from __future__ import annotations


import shutil
import subprocess
import sys



PYTHON_MIN_MAJOR = 3
PYTHON_MIN_MINOR = 10



def check_python():

    major = sys.version_info.major

    minor = sys.version_info.minor


    if (
        major < PYTHON_MIN_MAJOR
        or
        (
            major == PYTHON_MIN_MAJOR
            and minor < PYTHON_MIN_MINOR
        )
    ):

        raise RuntimeError(

            "Python 3.10 or newer required"

        )


    print(
        f"Python OK: {major}.{minor}"
    )



def check_pip():

    pip = shutil.which(
        "pip"
    )


    if not pip:

        raise RuntimeError(
            "pip not found"
        )


    print(
        "pip OK"
    )



def check_command(
    command: str,
):

    result = shutil.which(
        command
    )


    if not result:

        raise RuntimeError(

            f"{command} not found"

        )


    print(
        f"{command} OK"
    )



def upgrade_pip():

    subprocess.run(

        [

            sys.executable,

            "-m",

            "pip",

            "install",

            "--upgrade",

            "pip",

        ],

        check=True,

    )



def validate_environment():


    print(
        "Checking requirements..."
    )


    check_python()


    check_pip()


    check_command(
        "git"
    )


    print(
        "All requirements satisfied"
    )



if __name__ == "__main__":

    validate_environment()
