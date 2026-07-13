"""
Hetzner Shop
Logging Configuration
"""

from __future__ import annotations

import logging
import sys

from logging.handlers import RotatingFileHandler

from app.core.config import get_settings


def setup_logging():

    settings = get_settings()

    logger = logging.getLogger()

    logger.setLevel(
        settings.LOG_LEVEL
    )


    formatter = logging.Formatter(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(name)s | "
        "%(message)s"
    )


    console = logging.StreamHandler(
        sys.stdout
    )

    console.setFormatter(
        formatter
    )


    file_handler = RotatingFileHandler(
        "logs/app.log",
        maxBytes=10_000_000,
        backupCount=5,
        encoding="utf-8",
    )

    file_handler.setFormatter(
        formatter
    )


    logger.addHandler(
        console
    )

    logger.addHandler(
        file_handler
    )


    return logger
