"""
Hetzner Shop
Firewall Setup
"""

from __future__ import annotations


import subprocess



ALLOWED_PORTS = [

    "22/tcp",     # SSH

    "80/tcp",     # HTTP

    "443/tcp",    # HTTPS

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



def install_ufw():


    run_command(

        [

            "sudo",

            "apt",

            "install",

            "-y",

            "ufw",

        ]

    )



def reset_firewall():


    run_command(

        [

            "sudo",

            "ufw",

            "--force",

            "reset",

        ]

    )



def set_default_policy():


    run_command(

        [

            "sudo",

            "ufw",

            "default",

            "deny",

            "incoming",

        ]

    )


    run_command(

        [

            "sudo",

            "ufw",

            "default",

            "allow",

            "outgoing",

        ]

    )



def allow_ports():


    for port in ALLOWED_PORTS:

        run_command(

            [

                "sudo",

                "ufw",

                "allow",

                port,

            ]

        )



def enable_firewall():


    run_command(

        [

            "sudo",

            "ufw",

            "--force",

            "enable",

        ]

    )



def show_status():


    run_command(

        [

            "sudo",

            "ufw",

            "status",

            "verbose",

        ]

    )



def setup_firewall():


    print(
        "Starting firewall setup..."
    )


    install_ufw()


    reset_firewall()


    set_default_policy()


    allow_ports()


    enable_firewall()


    show_status()


    print(
        "Firewall configured successfully"
    )



if __name__ == "__main__":

    setup_firewall()
