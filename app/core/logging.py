"""
Hetzner Shop
Application Logging System
"""

from __future__ import annotations


import logging

from logging.handlers import (
    RotatingFileHandler,
)


from pathlib import Path



LOG_DIR = Path(
    "logs"
)


LOG_DIR.mkdir(
    exist_ok=True
)



def setup_logging():


    formatter = logging.Formatter(

        "%(asctime)s | "
        "%(levelname)s | "
        "%(name)s | "
        "%(message)s"

    )



    file_handler = (
        RotatingFileHandler(

            LOG_DIR / "app.log",

            maxBytes=5_000_000,

            backupCount=5,

            encoding="utf-8",

        )
    )



    file_handler.setFormatter(
        formatter
    )



    console_handler = (
        logging.StreamHandler()
    )


    console_handler.setFormatter(
        formatter
    )



    root_logger = logging.getLogger()


    root_logger.setLevel(
        logging.INFO
    )


    root_logger.addHandler(
        file_handler
    )


    root_logger.addHandler(
        console_handler
    )



    return root_logger
