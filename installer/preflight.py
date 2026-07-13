"""
Hetzner Shop
Preflight Installer Check
"""

from __future__ import annotations


import sys



from installer.system_check import (
    run_system_check,
)


from installer.environment_check import (
    run_environment_check,
)



def run_preflight():


    print(
        "=" * 50
    )

    print(
        "Hetzner Shop Preflight Check"
    )

    print(
        "=" * 50
    )


    try:

        run_system_check()


        print(
            ""
        )


        run_environment_check()



    except Exception as error:


        print(
            f"Preflight Failed: {error}"
        )


        sys.exit(1)



    print(
        ""
    )


    print(
        "All preflight checks passed"
    )


    print(
        "Ready to install Hetzner Shop"
    )



if __name__ == "__main__":

    run_preflight()
