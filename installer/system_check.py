"""
Hetzner Shop
System Requirements Check
"""

from __future__ import annotations


import os
import shutil
import socket



MIN_RAM_GB = 2

MIN_DISK_GB = 10



REQUIRED_PORTS = [

    22,

    80,

    443,

]



def check_cpu():


    cpu = os.cpu_count()


    print(
        f"CPU Cores: {cpu}"
    )


    if cpu < 1:

        raise RuntimeError(
            "CPU requirement not met"
        )



def check_memory():


    with open(
        "/proc/meminfo"
    ) as file:

        data = file.read()



    mem_kb = int(

        data.split(
            "MemTotal:"
        )[1]
        .split()[0]

    )


    ram_gb = (
        mem_kb /
        1024 /
        1024
    )


    print(
        f"RAM: {ram_gb:.2f} GB"
    )


    if ram_gb < MIN_RAM_GB:

        raise RuntimeError(
            "Not enough RAM"
        )



def check_disk():


    usage = shutil.disk_usage(
        "/"
    )


    free_gb = (

        usage.free /

        1024 /

        1024 /

        1024

    )


    print(
        f"Free Disk: {free_gb:.2f} GB"
    )


    if free_gb < MIN_DISK_GB:

        raise RuntimeError(
            "Not enough disk space"
        )



def check_ports():


    for port in REQUIRED_PORTS:

        sock = socket.socket()


        result = sock.connect_ex(

            (

                "127.0.0.1",

                port

            )

        )


        sock.close()


        if result == 0:

            print(
                f"Port {port}: Used"
            )

        else:

            print(
                f"Port {port}: Available"
            )



def run_system_check():


    print(
        "Running system checks..."
    )


    check_cpu()


    check_memory()


    check_disk()


    check_ports()


    print(
        "System check completed"
    )



if __name__ == "__main__":

    run_system_check()
