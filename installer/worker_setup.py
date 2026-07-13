"""
Hetzner Shop
Worker Service Setup
"""

from __future__ import annotations


from pathlib import Path
import subprocess



WORKER_NAME = "hetzner-shop-worker"



SERVICE_PATH = Path(
    f"/etc/systemd/system/{WORKER_NAME}.service"
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



def create_worker_service():


    project_path = (
        Path.cwd()
        .resolve()
    )


    content = f"""
[Unit]

Description=Hetzner Shop Background Worker

After=network.target redis-server.service



[Service]

Type=simple


WorkingDirectory={project_path}


ExecStart=/usr/bin/python3 -m app.worker


Restart=always


RestartSec=5


EnvironmentFile={project_path}/.env



[Install]

WantedBy=multi-user.target
"""


    SERVICE_PATH.write_text(

        content.strip(),

        encoding="utf-8",

    )



def enable_worker():


    run_command(

        [

            "sudo",

            "systemctl",

            "daemon-reload",

        ]

    )


    run_command(

        [

            "sudo",

            "systemctl",

            "enable",

            WORKER_NAME,

        ]

    )


    run_command(

        [

            "sudo",

            "systemctl",

            "restart",

            WORKER_NAME,

        ]

    )



def setup_worker():


    print(
        "Setting up worker service..."
    )


    create_worker_service()


    enable_worker()


    print(
        "Worker service installed"
    )



if __name__ == "__main__":

    setup_worker()
