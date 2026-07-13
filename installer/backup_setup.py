"""
Hetzner Shop
Backup Setup
"""

from __future__ import annotations


from pathlib import Path
from datetime import datetime
import shutil



BACKUP_DIR = Path(
    "backups"
)



FILES_TO_BACKUP = [

    ".env",

    "shop.db",

]



def create_backup_directory():

    BACKUP_DIR.mkdir(
        exist_ok=True
    )



def create_backup():


    timestamp = (
        datetime.now()
        .strftime(
            "%Y-%m-%d_%H-%M-%S"
        )
    )


    backup_path = (
        BACKUP_DIR /
        timestamp
    )


    backup_path.mkdir(
        exist_ok=True
    )



    for file in FILES_TO_BACKUP:

        source = Path(
            file
        )


        if source.exists():

            shutil.copy2(

                source,

                backup_path /
                source.name,

            )



    print(

        f"Backup created: {backup_path}"

    )



def setup_backup():

    print(
        "Setting up backup system..."
    )


    create_backup_directory()


    create_backup()


    print(
        "Backup setup completed"
    )



if __name__ == "__main__":

    setup_backup()
