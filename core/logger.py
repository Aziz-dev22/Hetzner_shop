"""
Hetzner Shop
Logging System
"""

from __future__ import annotations


import logging

from pathlib import Path



LOG_DIR = Path(
    "logs"
)


LOG_FILE = LOG_DIR / "app.log"



def setup_logger():


    LOG_DIR.mkdir(

        exist_ok=True

    )


    logger = logging.getLogger(

        "hetzner_shop"

    )


    logger.setLevel(

        logging.INFO

    )


    if not logger.handlers:


        file_handler = logging.FileHandler(

            LOG_FILE,

            encoding="utf-8",

        )


        formatter = logging.Formatter(

            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

        )


        file_handler.setFormatter(

            formatter

        )


        logger.addHandler(

            file_handler

        )



    return logger



logger = setup_logger()
