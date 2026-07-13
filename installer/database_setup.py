"""
Hetzner Shop
Database Setup
"""

from __future__ import annotations


import subprocess


from getpass import getpass



DATABASE_NAME = "hetznershop"

DATABASE_USER = "hetzner"



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



def install_postgresql():


    run_command(

        [

            "sudo",

            "apt",

            "install",

            "-y",

            "postgresql",

            "postgresql-contrib",

        ]

    )



def create_database():


    password = getpass(
        "Database password: "
    )


    commands = [

        [

            "sudo",

            "-u",

            "postgres",

            "psql",

            "-c",

            f"CREATE USER {DATABASE_USER} WITH PASSWORD '{password}';",

        ],


        [

            "sudo",

            "-u",

            "postgres",

            "psql",

            "-c",

            f"CREATE DATABASE {DATABASE_NAME} OWNER {DATABASE_USER};",

        ],

    ]


    for command in commands:

        run_command(
            command
        )



def restart_postgresql():


    run_command(

        [

            "sudo",

            "systemctl",

            "restart",

            "postgresql",

        ]

    )



def setup_database():


    print(
        "Setting up PostgreSQL..."
    )


    install_postgresql()


    create_database()


    restart_postgresql()


    print(
        "Database setup completed"
    )



if __name__ == "__main__":

    setup_database()
