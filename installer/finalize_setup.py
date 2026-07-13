"""
Hetzner Shop
Finalize Installation
"""

from __future__ import annotations


from pathlib import Path
import datetime



INSTALL_FILE = Path(
    ".installation_complete"
)



def create_install_marker():


    content = f"""
Hetzner Shop Installation Completed

Date:
{datetime.datetime.now()}

Status:
SUCCESS
"""


    INSTALL_FILE.write_text(

        content.strip(),

        encoding="utf-8",

    )



def show_summary():


    print(
        """
================================

 Hetzner Shop Installed

================================


Next steps:

1. Configure Domain DNS

2. Login to Admin Panel

3. Check Service Status

4. Review Logs


================================
"""
    )



def finalize_installation():


    print(
        "Finalizing installation..."
    )


    create_install_marker()


    show_summary()


    print(
        "Installation finalized successfully"
    )



if __name__ == "__main__":

    finalize_installation()
