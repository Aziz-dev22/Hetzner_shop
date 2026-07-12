"""
Hetzner Shop
Environment Utilities
"""

from __future__ import annotations

import os
import platform
import sys
from enum import Enum


class Environment(str, Enum):
    DEVELOPMENT = "development"
    TESTING = "testing"
    PRODUCTION = "production"


def current_environment() -> Environment:
    value = os.getenv("ENVIRONMENT", "production").lower()

    try:
        return Environment(value)
    except ValueError:
        return Environment.PRODUCTION


def is_production() -> bool:
    return current_environment() is Environment.PRODUCTION


def is_development() -> bool:
    return current_environment() is Environment.DEVELOPMENT


def is_testing() -> bool:
    return current_environment() is Environment.TESTING


def python_version() -> str:
    return platform.python_version()


def python_version_info() -> tuple[int, int, int]:
    return (
        sys.version_info.major,
        sys.version_info.minor,
        sys.version_info.micro,
    )


def operating_system() -> str:
    return platform.system()


def operating_system_release() -> str:
    return platform.release()


def hostname() -> str:
    return platform.node()


def architecture() -> str:
    return platform.machine()


def runtime_information() -> dict[str, str]:
    return {
        "environment": current_environment().value,
        "python": python_version(),
        "system": operating_system(),
        "release": operating_system_release(),
        "hostname": hostname(),
        "architecture": architecture(),
}
