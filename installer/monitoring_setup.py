"""
Hetzner Shop
Monitoring Setup
"""

from __future__ import annotations


import shutil
import psutil
import time



def get_cpu_usage():

    return psutil.cpu_percent(
        interval=1
    )



def get_memory_usage():

    memory = psutil.virtual_memory()

    return memory.percent



def get_disk_usage():

    disk = shutil.disk_usage(
        "/"
    )

    used = (
        disk.used /
        disk.total
    ) * 100

    return round(
        used,
        2
    )



def collect_metrics():


    metrics = {

        "cpu":
            get_cpu_usage(),

        "memory":
            get_memory_usage(),

        "disk":
            get_disk_usage(),

        "timestamp":
            time.time(),

    }


    return metrics



def show_status():


    print(
        "Collecting system metrics..."
    )


    metrics = collect_metrics()


    print(
        f"""
CPU: {metrics['cpu']}%

RAM: {metrics['memory']}%

DISK: {metrics['disk']}%

"""
    )



def setup_monitoring():


    print(
        "Monitoring initialized"
    )


    show_status()



if __name__ == "__main__":

    setup_monitoring()
