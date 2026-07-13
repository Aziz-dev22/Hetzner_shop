"""
Hetzner Shop
Application Configuration
"""

from __future__ import annotations

from functools import lru_cache

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):


    APP_NAME: str = "Hetzner Shop"

    ENVIRONMENT: str = "development"

    DEBUG: bool = True


    # Database

    DATABASE_URL: str


    # Telegram

    TELEGRAM_BOT_TOKEN: str

    TELEGRAM_ADMIN_ID: int


    # Security

    SECRET_KEY: str

    ENCRYPTION_KEY: str


    # Hetzner

    HETZNER_API_TOKEN: str


    # Redis

    REDIS_URL: str = (
        "redis://localhost:6379/0"
    )


    # Logging

    LOG_LEVEL: str = "INFO"



    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )



@lru_cache
def get_settings() -> Settings:

    return Settings()
