"""
Hetzner Shop
Locale Setup
"""

from __future__ import annotations


import subprocess



DEFAULT_LOCALE = "en_US.UTF-8"



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



def install_locales():


    run_command(

        [

            "sudo",

            "apt",

            "install",

            "-y",

            "locales",

        ]

    )



def generate_locale(
    locale: str,
):


    run_command(

        [

            "sudo",

            "locale-gen",

            locale,

        ]

    )



def set_system_locale(
    locale: str,
):


    run_command(

        [

            "sudo",

            "update-locale",

            f"LANG={locale}",

            f"LC_ALL={locale}",

        ]

    )



def show_locale():


    run_command(

        [

            "locale",

        ]

    )



def setup_locale():


    print(
        "Configuring locale..."
    )


    install_locales()


    generate_locale(
        DEFAULT_LOCALE
    )


    set_system_locale(
        DEFAULT_LOCALE
    )


    show_locale()


    print(
        "Locale configured"
    )



if __name__ == "__main__":

    setup_locale()
