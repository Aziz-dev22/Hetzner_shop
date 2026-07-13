"""
Hetzner Shop
Update System Setup
"""

from __future__ import annotations


import subprocess


from pathlib import Path



PROJECT_DIR = (
    Path.cwd()
    .resolve()
)



SERVICE_NAME = (
    "hetzner-shop"
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

        cwd=PROJECT_DIR,

        check=True,

    )



def pull_updates():


    run_command(

        [

            "git",

            "pull",

            "origin",

            "main",

        ]

    )



def install_updates():


    run_command(

        [

            "python3",

            "-m",

            "pip",

            "install",

            "-r",

            "requirements.txt",

        ]

    )



def migrate_database():


    run_command(

        [

            "alembic",

            "upgrade",

            "head",

        ]

    )



def restart_application():


    run_command(

        [

            "sudo",

            "systemctl",

            "restart",

            SERVICE_NAME,

        ]

    )



def update_application():


    print(
        "Starting update..."
    )


    pull_updates()


    install_updates()


    migrate_database()


    restart_application()



    print(
        "Update completed successfully"
    )



if __name__ == "__main__":

    update_application()
