"""
Hetzner Shop
Cleanup System
"""

from __future__ import annotations


from pathlib import Path
import shutil



CLEAN_TARGETS = [

    "logs",

    "__pycache__",

    ".pytest_cache",

]



def remove_path(
    path: Path,
):

    if not path.exists():

        return



    if path.is_dir():

        shutil.rmtree(
            path
        )


    else:

        path.unlink()



def cleanup_project():


    print(
        "Starting cleanup..."
    )


    for target in CLEAN_TARGETS:

        path = Path(
            target
        )


        remove_path(
            path
        )


        print(
            f"Removed: {target}"
        )



def recreate_directories():


    directories = [

        "logs",

    ]


    for directory in directories:

        Path(
            directory
        ).mkdir(
            exist_ok=True
        )



def run_cleanup():


    cleanup_project()


    recreate_directories()


    print(
        "Cleanup completed"
    )



if __name__ == "__main__":

    run_cleanup()
