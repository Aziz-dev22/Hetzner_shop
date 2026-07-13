"""
Hetzner Shop
SSL Setup
"""

from __future__ import annotations


import subprocess



DOMAIN = "example.com"



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



def install_certbot():


    run_command(

        [

            "sudo",

            "apt",

            "install",

            "-y",

            "certbot",

            "python3-certbot-nginx",

        ]

    )



def generate_certificate():


    run_command(

        [

            "sudo",

            "certbot",

            "--nginx",

            "-d",

            DOMAIN,

            "--non-interactive",

            "--agree-tos",

            "-m",

            "admin@example.com",

        ]

    )



def enable_auto_renew():


    run_command(

        [

            "sudo",

            "systemctl",

            "enable",

            "certbot.timer",

        ]

    )


    run_command(

        [

            "sudo",

            "systemctl",

            "start",

            "certbot.timer",

        ]

    )



def setup_ssl():


    print(
        "Setting up SSL..."
    )


    install_certbot()


    generate_certificate()


    enable_auto_renew()


    print(
        "SSL configured successfully"
    )



if __name__ == "__main__":

    setup_ssl()
