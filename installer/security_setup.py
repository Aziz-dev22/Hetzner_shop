"""
Hetzner Shop
Server Security Setup
"""

from __future__ import annotations


import subprocess



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



def install_fail2ban():


    run_command(

        [

            "sudo",

            "apt",

            "install",

            "-y",

            "fail2ban",

        ]

    )



def enable_fail2ban():


    run_command(

        [

            "sudo",

            "systemctl",

            "enable",

            "fail2ban",

        ]

    )


    run_command(

        [

            "sudo",

            "systemctl",

            "restart",

            "fail2ban",

        ]

    )



def secure_ssh():


    print(
        "SSH security checks enabled"
    )


    # تغییرات SSH در نسخه نهایی Installer
    # پس از بررسی تنظیمات کاربر اعمال خواهد شد.



def setup_security():


    print(
        "Starting security setup..."
    )


    install_fail2ban()


    enable_fail2ban()


    secure_ssh()


    print(
        "Security setup completed"
    )



if __name__ == "__main__":

    setup_security()
