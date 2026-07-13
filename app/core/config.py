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



class Settings(
    BaseSettings
):


    APP_NAME: str = (
        "Hetzner Shop"
    )


    ENVIRONMENT: str = (
        "development"
    )


    DEBUG: bool = True



    DATABASE_URL: str = (
        "sqlite+aiosqlite:///./shop.db"
    )



    SECRET_KEY: str = (
        "change-this-secret"
    )



    HETZNER_API_TOKEN: str = (
        ""
    )


    DEFAULT_PROVIDER: str = (
        "hetzner"
    )



    TELEGRAM_BOT_TOKEN: str = (
        ""
    )


    ADMIN_ID: int = 0



    model_config = SettingsConfigDict(

        env_file=".env",

        env_file_encoding="utf-8",

        extra="ignore",

    )




@lru_cache
def get_settings():

    return Settings()
