"""
Hetzner Shop
Redis Setup
"""

from __future__ import annotations


import subprocess



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



def install_redis():


    run_command(

        [

            "sudo",

            "apt",

            "install",

            "-y",

            "redis-server",

        ]

    )



def enable_redis():


    run_command(

        [

            "sudo",

            "systemctl",

            "enable",

            "redis-server",

        ]

    )


    run_command(

        [

            "sudo",

            "systemctl",

            "restart",

            "redis-server",

        ]

    )



def test_redis():


    run_command(

        [

            "redis-cli",

            "ping",

        ]

    )



def setup_redis():


    print(
        "Setting up Redis..."
    )


    install_redis()


    enable_redis()


    test_redis()


    print(
        "Redis setup completed"
    )



if __name__ == "__main__":

    setup_redis()
