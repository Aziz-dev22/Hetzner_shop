"""
Hetzner Shop
System Setup Installer
"""

from __future__ import annotations


import platform
import subprocess
import shutil



REQUIRED_PACKAGES = [

    "git",

    "curl",

    "python3",

    "python3-pip",

    "python3-venv",

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



def check_os():

    system = platform.system()


    if system != "Linux":

        raise RuntimeError(
            "Only Linux systems are supported"
        )


    print(
        "Linux detected"
    )



def check_apt():

    apt = shutil.which(
        "apt"
    )


    if not apt:

        raise RuntimeError(
            "APT package manager not found"
        )


    print(
        "APT detected"
    )



def update_system():

    run_command(

        [

            "sudo",

            "apt",

            "update",

        ]

    )



def install_packages():


    run_command(

        [

            "sudo",

            "apt",

            "install",

            "-y",

            *REQUIRED_PACKAGES,

        ]

    )



def setup_system():


    print(
        "Starting system setup..."
    )


    check_os()


    check_apt()


    update_system()


    install_packages()


    print(
        "System setup completed"
    )



if __name__ == "__main__":

    setup_system()
