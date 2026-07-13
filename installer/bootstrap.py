"""
Hetzner Shop
Bootstrap Installer
"""

from __future__ import annotations


import subprocess


import sys



def run_command(
    command: list[str],
):

    subprocess.run(

        command,

        check=True,

    )



def install_dependencies():

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



def start():

    print(
        "Installing Hetzner Shop..."
    )


    install_dependencies()


    run_migrations()


    print(
        "Installation completed"
    )



if __name__ == "__main__":

    start()
