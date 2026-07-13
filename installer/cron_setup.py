"""
Hetzner Shop
Cron Jobs Setup
"""

from __future__ import annotations


from pathlib import Path
import subprocess



CRON_FILE = Path(
    "/tmp/hetzner-shop-cron"
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



def create_cron_file():


    project_path = (
        Path.cwd()
        .resolve()
    )


    cron_content = f"""
# Hetzner Shop Scheduled Tasks


# Daily Backup - 02:00

0 2 * * * cd {project_path} && python3 -m installer.backup_setup


# Health Check every 10 minutes

*/10 * * * * cd {project_path} && python3 -m installer.health_check


# Weekly Cleanup - Sunday 03:00

0 3 * * 0 cd {project_path} && python3 -m installer.cleanup_setup

"""


    CRON_FILE.write_text(

        cron_content.strip(),

        encoding="utf-8",

    )



def install_cron():


    run_command(

        [

            "crontab",

            str(CRON_FILE),

        ]

    )



def setup_cron():


    print(
        "Setting up cron jobs..."
    )


    create_cron_file()


    install_cron()


    print(
        "Cron setup completed"
    )



if __name__ == "__main__":

    setup_cron()
