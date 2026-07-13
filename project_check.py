"""
Hetzner Shop
Project Structure Checker
"""

from __future__ import annotations


from pathlib import Path



BASE_DIR = Path(__file__).parent



REQUIRED_FILES = [

    "main.py",

    "requirements.txt",

    "Dockerfile",

    "docker-compose.yml",

    ".env.example",

    "README.md",

    "installer/install.py",

    "installer/firewall_setup.py",

]



REQUIRED_DIRS = [

    "api",

    "core",

    "database",

    "models",

    "schemas",

    "services",

    "workers",

    "web",

    "tests",

    "alembic",

]





def check_files():


    result = {}


    for file in REQUIRED_FILES:


        path = BASE_DIR / file


        result[file] = path.exists()



    return result





def check_directories():


    result = {}


    for directory in REQUIRED_DIRS:


        path = BASE_DIR / directory


        result[directory] = path.exists()



    return result





def run_check():


    files = check_files()

    dirs = check_directories()



    failed_files = [

        item

        for item, status

        in files.items()

        if not status

    ]



    failed_dirs = [

        item

        for item, status

        in dirs.items()

        if not status

    ]



    return {

        "status":

        len(failed_files) == 0

        and len(failed_dirs) == 0,


        "missing_files":

        failed_files,


        "missing_directories":

        failed_dirs,

    }





if __name__ == "__main__":


    result = run_check()


    print(result)
