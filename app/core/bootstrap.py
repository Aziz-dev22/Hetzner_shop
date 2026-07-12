"""
Hetzner Shop

Bootstrap

این فایل مسئول آماده‌سازی محیط اجرای پروژه است.

هیچ منطق تجاری (Business Logic) نباید در این فایل قرار بگیرد.
"""

from __future__ import annotations

import os
import platform
import sys
from pathlib import Path

from app.core.paths import (
    BACKUP_DIR,
    CACHE_DIR,
    DATA_DIR,
    EXPORT_DIR,
    LOG_DIR,
    RUNTIME_DIRECTORIES,
    TEMP_DIR,
    UPLOAD_DIR,
)


###############################################################################
# Supported Systems
###############################################################################

SUPPORTED_SYSTEMS = (
    "Linux",
)

SUPPORTED_PYTHON = (
    3,
    12,
)


###############################################################################
# Python
###############################################################################


def check_python() -> None:

    if sys.version_info < SUPPORTED_PYTHON:

        version = ".".join(
            map(str, SUPPORTED_PYTHON)
        )

        raise RuntimeError(
            f"Python {version}+ is required."
        )


###############################################################################
# Operating System
###############################################################################


def check_operating_system() -> None:

    system = platform.system()

    if system not in SUPPORTED_SYSTEMS:

        raise RuntimeError(
            f"Unsupported operating system: {system}"
        )


###############################################################################
# Directories
###############################################################################


def create_runtime_directories() -> None:

    for directory in RUNTIME_DIRECTORIES:

        directory.mkdir(
            parents=True,
            exist_ok=True,
        )


###############################################################################
# Permissions
###############################################################################


def check_write_permissions() -> None:

    targets = (
        DATA_DIR,
        LOG_DIR,
        BACKUP_DIR,
        CACHE_DIR,
        TEMP_DIR,
        UPLOAD_DIR,
        EXPORT_DIR,
    )

    for target in targets:

        if not os.access(target, os.W_OK):

            raise PermissionError(
                f"Directory is not writable:\n{target}"
            )


###############################################################################
# Environment File
###############################################################################


def environment_exists(env_path: Path) -> bool:

    return env_path.exists()
###############################################################################
# Project Structure
###############################################################################


def verify_project_structure() -> None:

    required_paths = (
        DATA_DIR,
        LOG_DIR,
        BACKUP_DIR,
        CACHE_DIR,
        TEMP_DIR,
        UPLOAD_DIR,
        EXPORT_DIR,
    )

    for path in required_paths:

        if not path.exists():

            raise FileNotFoundError(
                f"Missing required path:\n{path}"
            )


###############################################################################
# Bootstrap
###############################################################################


def bootstrap() -> None:
    """
    Prepare the runtime environment.

    This function is safe to call multiple times.
    """

    check_python()

    check_operating_system()

    create_runtime_directories()

    check_write_permissions()

    verify_project_structure()


###############################################################################
# Bootstrap Status
###############################################################################


def bootstrap_status() -> dict[str, object]:

    return {
        "python": platform.python_version(),
        "system": platform.system(),
        "machine": platform.machine(),
        "platform": platform.platform(),
        "runtime_ready": True,
        "data_directory": str(DATA_DIR),
        "log_directory": str(LOG_DIR),
        "backup_directory": str(BACKUP_DIR),
        "cache_directory": str(CACHE_DIR),
        "temp_directory": str(TEMP_DIR),
        "upload_directory": str(UPLOAD_DIR),
        "export_directory": str(EXPORT_DIR),
    }


###############################################################################
# Startup
###############################################################################


def initialize() -> None:
    """
    Complete application initialization.

    This is the only function that should be called
    by app.main before starting the application.
    """

    bootstrap()


__all__ = (
    "bootstrap",
    "bootstrap_status",
    "check_python",
    "check_operating_system",
    "create_runtime_directories",
    "check_write_permissions",
    "verify_project_structure",
    "environment_exists",
    "initialize",
      )
