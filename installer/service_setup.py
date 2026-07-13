"""
Hetzner Shop
Systemd Service Setup
"""

from __future__ import annotations


from pathlib import Path
import subprocess



SERVICE_NAME = "hetzner-shop"


SERVICE_PATH = Path(
    f"/etc/systemd/system/{SERVICE_NAME}.service"
)



def run_command(
    command: list[str],
):

    subprocess.run(
        command,
        check=True,
    )



def create_service_file():


    project_path = (
        Path.cwd()
        .resolve()
    )


    service_content = f"""
[Unit]
Description=Hetzner Shop Application
After=network.target


[Service]

Type=simple

WorkingDirectory={project_path}

ExecStart=/usr/bin/python3 -m app.main

Restart=always

RestartSec=5

EnvironmentFile={project_path}/.env


[Install]

WantedBy=multi-user.target
"""


    SERVICE_PATH.write_text(
        service_content,
        encoding="utf-8",
    )



def enable_service():


    run_command(

        [

            "systemctl",

            "daemon-reload",

        ]

    )


    run_command(

        [

            "systemctl",

            "enable",

            SERVICE_NAME,

        ]

    )


    run_command(

        [

            "systemctl",

            "restart",

            SERVICE_NAME,

        ]

    )



def setup_service():


    print(
        "Creating systemd service..."
    )


    create_service_file()


    enable_service()


    print(
        "Systemd service installed"
    )



if __name__ == "__main__":

    setup_service()
