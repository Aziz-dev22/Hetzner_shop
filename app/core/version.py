"""
Hetzner Shop
Core Version Information

This file is the single source of truth for the project's version.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
import platform


@dataclass(frozen=True, slots=True)
class VersionInfo:
    project_name: str
    package_name: str

    version: str

    release_name: str

    release_channel: str

    build_number: str

    build_date: str

    python_required: str

    supported_os: tuple[str, ...]

    default_provider: str


VERSION = VersionInfo(
    project_name="Hetzner Shop",
    package_name="server_shop",

    version="1.0.0",

    release_name="Genesis",

    release_channel="Stable",

    build_number="20260712001",

    build_date=datetime.now(
        UTC
    ).strftime("%Y-%m-%d"),

    python_required="3.12",

    supported_os=(
        "Ubuntu 22.04 LTS",
        "Ubuntu 24.04 LTS",
        "Debian 12",
    ),

    default_provider="Hetzner",
)


def project_version() -> str:
    return VERSION.version


def build_number() -> str:
    return VERSION.build_number


def release_name() -> str:
    return VERSION.release_name


def release_channel() -> str:
    return VERSION.release_channel


def application_name() -> str:
    return VERSION.project_name


def package_name() -> str:
    return VERSION.package_name


def supported_os() -> tuple[str, ...]:
    return VERSION.supported_os


def python_required() -> str:
    return VERSION.python_required


def runtime_python() -> str:
    return platform.python_version()


def build_information() -> dict:

    return {
        "application": VERSION.project_name,
        "package": VERSION.package_name,
        "version": VERSION.version,
        "release": VERSION.release_name,
        "channel": VERSION.release_channel,
        "build": VERSION.build_number,
        "build_date": VERSION.build_date,
        "python_required": VERSION.python_required,
        "python_runtime": runtime_python(),
        "provider": VERSION.default_provider,
        "supported_os": list(VERSION.supported_os),
    }


__all__ = [
    "VERSION",
    "VersionInfo",
    "application_name",
    "project_version",
    "build_number",
    "release_name",
    "release_channel",
    "supported_os",
    "python_required",
    "runtime_python",
    "build_information",
  ]
