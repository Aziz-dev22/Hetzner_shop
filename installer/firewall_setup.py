"""
Hetzner Shop
Firewall Setup Installer

Ubuntu / Debian Compatible
"""

from __future__ import annotations


import subprocess



DEFAULT_PORTS = [

    "22/tcp",

    "80/tcp",

    "443/tcp",

    "8000/tcp",

]



def run_command(

    command: list[str],

):


    result = subprocess.run(

        command,

        stdout=subprocess.PIPE,

        stderr=subprocess.PIPE,

        text=True,

    )


    return {

        "code": result.returncode,

        "output": result.stdout.strip(),

        "error": result.stderr.strip(),

    }



def install_ufw():


    check = run_command(

        [

            "which",

            "ufw"

        ]

    )


    if check["code"] == 0:

        return True



    result = run_command(

        [

            "apt-get",

            "update"

        ]

    )


    if result["code"] != 0:

        return False



    result = run_command(

        [

            "apt-get",

            "install",

            "-y",

            "ufw"

        ]

    )


    return result["code"] == 0



def allow_port(

    port: str,

):


    result = run_command(

        [

            "ufw",

            "allow",

            port

        ]

    )


    return result["code"] == 0



def enable_firewall():


    # جلوگیری از قطع SSH

    run_command(

        [

            "ufw",

            "allow",

            "OpenSSH"

        ]

    )


    result = run_command(

        [

            "ufw",

            "--force",

            "enable"

        ]

    )


    return result["code"] == 0



def setup_firewall():


    if not install_ufw():

        return {

            "status":

            "failed",

            "message":

            "UFW installation failed",

        }



    allowed = []



    for port in DEFAULT_PORTS:


        if allow_port(port):

            allowed.append(port)



    enabled = enable_firewall()



    return {

        "status":

        "completed" if enabled else "partial",


        "allowed_ports":

        allowed,

        }
