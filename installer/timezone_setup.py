"""
Hetzner Shop
Timezone Setup
"""

from __future__ import annotations


import subprocess



DEFAULT_TIMEZONE = "UTC"



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



def get_timezone():


    timezone = input(

        f"Timezone [{DEFAULT_TIMEZONE}]: "

    ).strip()



    if not timezone:

        timezone = DEFAULT_TIMEZONE



    return timezone



def set_timezone(
    timezone: str,
):


    run_command(

        [

            "sudo",

            "timedatectl",

            "set-timezone",

            timezone,

        ]

    )



def show_timezone():


    run_command(

        [

            "timedatectl",

            "status",

        ]

    )



def setup_timezone():


    print(
        "Configuring timezone..."
    )


    timezone = get_timezone()


    set_timezone(
        timezone
    )


    show_timezone()


    print(
        "Timezone configured"
    )



if __name__ == "__main__":

    setup_timezone()
