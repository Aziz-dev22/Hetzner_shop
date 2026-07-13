"""
Hetzner Shop
Main Installer

One Click Installation
"""

from __future__ import annotations


import sys



from installer.dependency_check import (

    run_checks,

)


from installer.system_setup import (

    setup_system,

)


from installer.firewall_setup import (

    setup_firewall,

)



def print_header():

    print(

        """

====================================

        Hetzner Shop Installer

====================================

        """

    )



def check_dependencies():


    print(

        "[1/3] Checking dependencies..."

    )


    result = run_checks()


    failed = [

        name

        for name, status

        in result.items()

        if not status

    ]


    if failed:

        print(

            "Missing dependencies:",

            failed

        )

        sys.exit(1)



    print(

        "Dependencies OK"

    )



def prepare_system():


    print(

        "[2/3] Preparing system..."

    )


    result = setup_system()


    print(result)



def configure_security():


    print(

        "[3/3] Configuring firewall..."

    )


    result = setup_firewall()


    print(result)



def main():


    print_header()


    check_dependencies()


    prepare_system()


    configure_security()


    print(

        """

Installation preparation completed.

Next:

docker compose up -d

        """

    )



if __name__ == "__main__":

    main()
