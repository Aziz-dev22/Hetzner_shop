"""
Hetzner Shop
Queue Worker Setup
"""

from __future__ import annotations


from pathlib import Path



ENV_FILE = Path(
    ".env"
)



def ask(
    message: str,
    default: str = "",
):

    value = input(
        f"{message} "
    )


    if value.strip():

        return value.strip()


    return default



def setup_queue():


    print(
        "Configuring queue system..."
    )


    queue_driver = ask(

        "Queue Driver:",

        "redis",

    )


    redis_host = ask(

        "Redis Host:",

        "127.0.0.1",

    )


    redis_port = ask(

        "Redis Port:",

        "6379",

    )


    worker_count = ask(

        "Worker Count:",

        "2",

    )



    content = f"""

QUEUE_DRIVER={queue_driver}

REDIS_HOST={redis_host}

REDIS_PORT={redis_port}

WORKER_COUNT={worker_count}

"""



    with ENV_FILE.open(

        "a",

        encoding="utf-8"

    ) as file:

        file.write(
            content
        )



    print(
        "Queue configuration saved"
    )



if __name__ == "__main__":

    setup_queue()
