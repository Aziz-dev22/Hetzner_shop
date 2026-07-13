"""
Hetzner Shop
Logrotate Setup
"""

from __future__ import annotations


from pathlib import Path
import subprocess



LOGROTATE_FILE = Path(
    "/etc/logrotate.d/hetzner-shop"
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
        check=True,
    )



def create_logrotate_config():


    config = """
/var/log/hetzner-shop/*.log {

    daily

    rotate 14

    compress

    delaycompress

    missingok

    notifempty

    copytruncate

}
"""


    LOGROTATE_FILE.write_text(

        config,

        encoding="utf-8",

    )



def test_logrotate():


    run_command(

        [

            "sudo",

            "logrotate",

            "-d",

            str(LOGROTATE_FILE),

        ]

    )



def setup_logrotate():


    print(
        "Setting up log rotation..."
    )


    create_logrotate_config()


    test_logrotate()


    print(
        "Logrotate configured"
    )



if __name__ == "__main__":

    setup_logrotate()
