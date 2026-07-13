"""
Hetzner Shop
System Setup Installer
"""

from __future__ import annotations


import os

from pathlib import Path



PROJECT_DIR = Path(

    "/opt/hetzner-shop"

)



REQUIRED_DIRS = [

    PROJECT_DIR,

    PROJECT_DIR / "logs",

    PROJECT_DIR / "backup",

    PROJECT_DIR / "data",

]



def create_directories():


    for directory in REQUIRED_DIRS:


        directory.mkdir(

            parents=True,

            exist_ok=True,

        )



def set_permissions():


    for directory in REQUIRED_DIRS:


        os.chmod(

            directory,

            0o755,

        )



def setup_system():


    create_directories()


    set_permissions()


    return {

        "status": "completed",

        "project_path":

        str(PROJECT_DIR),

    }
