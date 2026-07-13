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



def configure_rules():


    run_command(

        [

            "sudo",

            "ufw",

            "default",

            "deny",

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



def setup_firewall():


    print(
        "Configuring firewall..."
    )


    install_ufw()


    configure_rules()


    enable_firewall()


    print(
        "Firewall enabled"
    )



if __name__ == "__main__":

    setup_firewall()
