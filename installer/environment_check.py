"""
Hetzner Shop
Environment Check
"""

from __future__ import annotations


import subprocess
import sys
from pathlib import Path



MIN_PYTHON = (3, 10)



REQUIRED_FILES = [

    "requirements.txt",

    ".env",

]



def check_python():


    version = sys.version_info


    print(

        f"Python: {version.major}.{version.minor}"

    )


    if (

        version.major,

        version.minor

    ) < MIN_PYTHON:

        raise RuntimeError(

            "Python 3.10+ required"

        )



def check_git():


    try:

        subprocess.run(

            [

                "git",

                "--version",

            ],

            check=True,

            capture_output=True,

        )


        print(
            "Git: OK"
        )


    except Exception:


        raise RuntimeError(
            "Git is not installed"
        )



def check_files():


    for file in REQUIRED_FILES:

        path = Path(
            file
        )


        if path.exists():

            print(
                f"{file}: OK"
            )

        else:

            print(
                f"{file}: Missing"
            )



def check_virtual_environment():


    if (

        sys.prefix !=
        sys.base_prefix

    ):

        print(
            "Virtual Environment: OK"
        )

    else:

        print(
            "Virtual Environment: Not Active"
        )



def run_environment_check():


    print(
        "Checking environment..."
    )


    check_python()


    check_git()


    check_files()


    check_virtual_environment()


    print(
        "Environment check completed"
    )



if __name__ == "__main__":

    run_environment_check()
