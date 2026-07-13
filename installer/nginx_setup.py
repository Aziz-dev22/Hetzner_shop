"""
Hetzner Shop
Nginx Setup
"""

from __future__ import annotations


import subprocess

from pathlib import Path



PROJECT_NAME = "hetzner-shop"


NGINX_CONFIG = Path(
    f"/etc/nginx/sites-available/{PROJECT_NAME}"
)


NGINX_LINK = Path(
    f"/etc/nginx/sites-enabled/{PROJECT_NAME}"
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



def install_nginx():


    run_command(

        [

            "sudo",

            "apt",

            "install",

            "-y",

            "nginx",

        ]

    )



def create_config():


    config = """
server {

    listen 80;

    server_name example.com;


    location / {

        proxy_pass http://127.0.0.1:8000;


        proxy_http_version 1.1;


        proxy_set_header Host $host;

        proxy_set_header X-Real-IP $remote_addr;

        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        proxy_set_header X-Forwarded-Proto $scheme;

    }

}
"""


    NGINX_CONFIG.write_text(

        config,

        encoding="utf-8",

    )



def enable_site():


    run_command(

        [

            "sudo",

            "ln",

            "-sf",

            str(NGINX_CONFIG),

            str(NGINX_LINK),

        ]

    )


    run_command(

        [

            "sudo",

            "nginx",

            "-t",

        ]

    )


    run_command(

        [

            "sudo",

            "systemctl",

            "reload",

            "nginx",

        ]

    )



def setup_nginx():


    print(
        "Setting up Nginx..."
    )


    install_nginx()


    create_config()


    enable_site()


    print(
        "Nginx setup completed"
    )



if __name__ == "__main__":

    setup_nginx()
