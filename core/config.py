"""
Hetzner Shop
Application Configuration
"""

from __future__ import annotations


from functools import lru_cache


from pydantic_settings import BaseSettings



class Settings(BaseSettings):


    APP_NAME: str = "Hetzner Shop"


    APP_ENV: str = "production"


    APP_DEBUG: bool = False


    APP_URL: str = "http://localhost:8000"



    SECRET_KEY: str


    JWT_SECRET_KEY: str



    DATABASE_ENGINE: str = "postgresql"


    DATABASE_HOST: str = "postgres"


    DATABASE_PORT: int = 5432


    DATABASE_NAME: str


    DATABASE_USER: str


    DATABASE_PASSWORD: str



    REDIS_HOST: str = "redis"


    REDIS_PORT: int = 6379



    HETZNER_API_TOKEN: str



    TELEGRAM_NOTIFICATION_TOKEN: str | None = None


    TELEGRAM_NOTIFICATION_CHAT_ID: str | None = None



    SMTP_HOST: str | None = None


    SMTP_PORT: int = 587


    SMTP_USERNAME: str | None = None


    SMTP_PASSWORD: str | None = None


    SMTP_FROM_EMAIL: str | None = None



    SERVER_TIMEZONE: str = "UTC"



    @property

    def DATABASE_URL(self):


        return (

            f"{self.DATABASE_ENGINE}+asyncpg://"

            f"{self.DATABASE_USER}:"

            f"{self.DATABASE_PASSWORD}@"

            f"{self.DATABASE_HOST}:"

            f"{self.DATABASE_PORT}/"

            f"{self.DATABASE_NAME}"

        )



    class Config:

        env_file = ".env"

        case_sensitive = True





@lru_cache

def get_settings():


    return Settings()





settings = get_settings()
