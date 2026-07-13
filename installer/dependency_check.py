"""
Hetzner Shop
Installer Dependency Checker
"""

from __future__ import annotations


import shutil

import subprocess

import sys



MIN_PYTHON_VERSION = (

    3,

    10,

)



def check_python():


    current = sys.version_info[:2]


    if current < MIN_PYTHON_VERSION:

        raise RuntimeError(

            "Python 3.10 or higher is required"

        )


    return True



def check_command(

    command: str

):


    return shutil.which(

        command

    ) is not None



def check_git():


    return check_command(

        "git"

    )



def check_docker():


    return check_command(

        "docker"

    )



def check_docker_compose():


    result = subprocess.run(

        [

            "docker",

            "compose",

            "version"

        ],

        stdout=subprocess.PIPE,

        stderr=subprocess.PIPE,

    )


    return result.returncode == 0



def run_checks():


    checks = {


        "python":

        check_python(),



        "git":

        check_git(),



        "docker":

        check_docker(),



        "docker_compose":

        check_docker_compose(),

    }



    return checks
