"""
Hetzner Shop
Application Configuration
"""

from __future__ import annotations


from functools import lru_cache


from pydantic_settings import BaseSettings



class Settings(
    BaseSettings
):


    # Application

    APP_NAME: str = "Hetzner Shop"

    APP_ENV: str = "production"

    APP_DEBUG: bool = False

    APP_URL: str = "http://localhost"



    # Security

    SECRET_KEY: str

    JWT_SECRET_KEY: str



    # Database

    DATABASE_ENGINE: str = "postgresql"

    DATABASE_HOST: str = "127.0.0.1"

    DATABASE_PORT: int = 5432

    DATABASE_NAME: str = "hetzner_shop"

    DATABASE_USER: str = "hetzner"

    DATABASE_PASSWORD: str



    # Redis

    REDIS_HOST: str = "127.0.0.1"

    REDIS_PORT: int = 6379



    # Hetzner

    HETZNER_API_TOKEN: str



    # Telegram

    TELEGRAM_NOTIFICATION_TOKEN: str | None = None

    TELEGRAM_NOTIFICATION_CHAT_ID: str | None = None



    # SMTP

    SMTP_HOST: str | None = None

    SMTP_PORT: int = 587

    SMTP_USERNAME: str | None = None

    SMTP_PASSWORD: str | None = None

    SMTP_FROM_EMAIL: str | None = None



    # Server

    SERVER_TIMEZONE: str = "UTC"



    class Config:

        env_file = ".env"

        case_sensitive = True




@lru_cache
def get_settings():

    return Settings()



settings = get_settings()
