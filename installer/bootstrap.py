"""
Hetzner Shop
Professional Installer Bootstrap
"""

from __future__ import annotations


import subprocess
import sys



INSTALL_STEPS = [

    (
        "Preflight Check",
        "installer.preflight"
    ),

    (
        "System Setup",
        "installer.system_setup"
    ),

    (
        "Environment Setup",
        "installer.env_setup"
    ),

    (
        "Requirements Installation",
        "installer.requirements"
    ),

    (
        "Database Setup",
        "installer.database_setup"
    ),

    (
        "Redis Setup",
        "installer.redis_setup"
    ),

    (
        "Queue Setup",
        "installer.queue_setup"
    ),

    (
        "Worker Setup",
        "installer.worker_setup"
    ),

    (
        "Admin User Setup",
        "installer.user_setup"
    ),

    (
        "Nginx Setup",
        "installer.nginx_setup"
    ),

    (
        "SSL Setup",
        "installer.ssl_setup"
    ),

    (
        "Security Setup",
        "installer.security_setup"
    ),

    (
        "Firewall Setup",
        "installer.firewall_setup"
    ),

    (
        "Backup Setup",
        "installer.backup_setup"
    ),

    (
        "Cron Setup",
        "installer.cron_setup"
    ),

    (
        "Monitoring Setup",
        "installer.monitoring_setup"
    ),

    (
        "Health Check",
        "installer.health_check"
    ),

    (
        "Finalize Installation",
        "installer.finalize_setup"
    ),

]



def run_step(
    name: str,
    module: str,
):

    print(
        "\n" + "=" * 60
    )

    print(
        f"Running: {name}"
    )

    print(
        "=" * 60
    )


    subprocess.run(

        [

            sys.executable,

            "-m",

            module,

        ],

        check=True,

    )



def bootstrap():


    print(
        """
====================================

 Hetzner Shop Installer

 Starting Installation

====================================
"""
    )


    for name, module in INSTALL_STEPS:

        run_step(

            name,

            module

        )


    print(
        """
====================================

 Installation Completed Successfully

====================================
"""
    )



if __name__ == "__main__":

    bootstrap()
