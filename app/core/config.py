"""
Hetzner Shop
Configuration Manager
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from pydantic import SecretStr
from pydantic import computed_field
from pydantic import field_validator
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


ROOT_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    """
    Global application configuration.
    """

    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    ####################################################################
    # Application
    ####################################################################

    app_name: str = "Hetzner Shop"

    app_version: str = "1.0.0"

    environment: str = "production"

    debug: bool = False

    language: str = "fa"

    timezone: str = "UTC"

    ####################################################################
    # Telegram
    ####################################################################

    bot_token: SecretStr

    admin_ids: str = ""

    ####################################################################
    # Web
    ####################################################################

    web_host: str = "0.0.0.0"

    web_port: int = 8080

    ####################################################################
    # Database
    ####################################################################

    database_url: str = (
        "sqlite+aiosqlite:///data/database.db"
    )

    ####################################################################
    # Security
    ####################################################################

    secret_key: SecretStr

    jwt_secret_key: SecretStr

    encryption_key: SecretStr

    jwt_algorithm: str = "HS256"

    jwt_expire_hours: int = 24

    ####################################################################
    # Logging
    ####################################################################

    log_level: str = "INFO"

    log_to_file: bool = True

    ####################################################################
    # Backup
    ####################################################################

    auto_backup: bool = True

    backup_keep_days: int = 30

    ####################################################################
    # Provider
    ####################################################################

    default_provider: str = "hetzner"

    ####################################################################
    # Validators
    ####################################################################

    @field_validator("environment")
    @classmethod
    def validate_environment(cls, value: str) -> str:

        value = value.lower()

        if value not in (
            "development",
            "production",
            "testing",
        ):
            raise ValueError(
                "Invalid environment."
            )

        return value

    @field_validator("language")
    @classmethod
    def validate_language(cls, value: str) -> str:

        value = value.lower()

        if value not in (
            "fa",
            "en",
        ):
            raise ValueError(
                "Unsupported language."
            )

        return value

    @field_validator("web_port")
    @classmethod
    def validate_web_port(cls, value: int) -> int:

        if not 1 <= value <= 65535:
            raise ValueError(
                "Invalid web port."
            )

        return value
    ####################################################################
    # Computed Fields
    ####################################################################

    @computed_field
    @property
    def admin_list(self) -> list[int]:
        """
        Convert ADMIN_IDS environment variable
        from comma-separated string to list[int].
        """

        if not self.admin_ids.strip():
            return []

        result: list[int] = []

        for item in self.admin_ids.split(","):

            item = item.strip()

            if not item:
                continue

            result.append(int(item))

        return result

    ####################################################################
    # Helpers
    ####################################################################

    @property
    def is_production(self) -> bool:
        return self.environment == "production"

    @property
    def is_development(self) -> bool:
        return self.environment == "development"

    @property
    def is_testing(self) -> bool:
        return self.environment == "testing"


###############################################################################
# Global Settings
###############################################################################


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """
    Returns cached application settings.
    """

    return Settings()


settings = get_settings()


def reload_settings() -> Settings:
    """
    Reload settings after .env changes.
    """

    get_settings.cache_clear()

    global settings

    settings = get_settings()

    return settings


__all__ = (
    "Settings",
    "settings",
    "get_settings",
    "reload_settings",
)
