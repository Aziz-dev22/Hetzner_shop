"""
Hetzner Shop
Bootstrap Installer
"""

from __future__ import annotations


import subprocess
import sys
from pathlib import Path


from installer.env_setup import (
    create_env,
)



ROOT_DIR = Path(__file__).resolve().parent.parent


REQUIREMENTS_FILE = (
    ROOT_DIR / "requirements.txt"
)



def run_command(
    command: list[str],
):

    print(
        "Running:",
        " ".join(command)
    )


    subprocess.run(
        command,
        cwd=ROOT_DIR,
        check=True,
    )



def check_python_version():

    major = sys.version_info.major

    minor = sys.version_info.minor


    if major < 3 or (
        major == 3 and minor < 10
    ):

        raise RuntimeError(
            "Python 3.10+ is required"
        )



def install_dependencies():

    if not REQUIREMENTS_FILE.exists():

        raise FileNotFoundError(
            "requirements.txt not found"
        )


    run_command(

        [

            sys.executable,

            "-m",

            "pip",

            "install",

            "--upgrade",

            "pip",

        ]

    )


    run_command(

        [

            sys.executable,

            "-m",

            "pip",

            "install",

            "-r",

            "requirements.txt",

        ]

    )



def run_migrations():

    run_command(

        [

            "alembic",

            "upgrade",

            "head",

        ]

    )



def create_directories():

    directories = [

        "logs",

        "storage",

        "uploads",

    ]


    for directory in directories:

        path = ROOT_DIR / directory


        path.mkdir(
            exist_ok=True
        )



def start():

    print(
        """
================================

   Hetzner Shop Installer

================================
"""
    )


    check_python_version()


    create_env()


    create_directories()


    install_dependencies()


    run_migrations()



    print(
        """
================================

 Installation Completed

 Run:

 python -m app.main

================================
"""
    )



if __name__ == "__main__":

    start()
