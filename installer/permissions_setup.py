"""
Hetzner Shop
Permissions Setup
"""

from __future__ import annotations


from pathlib import Path
import subprocess



PROJECT_DIR = (
    Path.cwd()
    .resolve()
)



APP_USER = "www-data"



DIRECTORIES = [

    "logs",

    "storage",

    "uploads",

    "backups",

]



def run_command(
    command: list[str],
):

    print(
        "Running:",
        " ".join(command)
    )


    subprocess.run(
        command,
        check=True,
    )



def create_directories():


    for directory in DIRECTORIES:

        path = (
            PROJECT_DIR /
            directory
        )


        path.mkdir(
            exist_ok=True
        )



def set_owner():


    run_command(

        [

            "sudo",

            "chown",

            "-R",

            f"{APP_USER}:{APP_USER}",

            str(PROJECT_DIR),

        ]

    )



def set_permissions():


    run_command(

        [

            "sudo",

            "chmod",

            "-R",

            "755",

            str(PROJECT_DIR),

        ]

    )



def setup_permissions():


    print(
        "Setting permissions..."
    )


    create_directories()


    set_owner()


    set_permissions()


    print(
        "Permissions configured"
    )



if __name__ == "__main__":

    setup_permissions()
