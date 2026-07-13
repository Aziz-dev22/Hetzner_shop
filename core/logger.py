"""
Hetzner Shop
Application Logger
"""

from __future__ import annotations


import logging

from pathlib import Path



LOG_DIR = Path("logs")


LOG_DIR.mkdir(

    exist_ok=True

)



LOG_FILE = LOG_DIR / "app.log"





def get_logger(

    name: str = "hetzner_shop"

):


    logger = logging.getLogger(name)



    if logger.handlers:

        return logger



    logger.setLevel(

        logging.INFO

    )



    formatter = logging.Formatter(

        "%(asctime)s | "

        "%(levelname)s | "

        "%(name)s | "

        "%(message)s"

    )



    file_handler = logging.FileHandler(

        LOG_FILE

    )


    file_handler.setFormatter(

        formatter

    )



    console_handler = logging.StreamHandler()


    console_handler.setFormatter(

        formatter

    )



    logger.addHandler(

        file_handler

    )


    logger.addHandler(

        console_handler

    )



    return logger





logger = get_logger()
