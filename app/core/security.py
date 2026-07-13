"""
Hetzner Shop
Security Utilities
"""

from __future__ import annotations

import hashlib
import secrets

from cryptography.fernet import (
    Fernet,
)

from app.core.config import (
    get_settings,
)


class SecurityManager:


    def __init__(self):

        settings = get_settings()

        self.fernet = Fernet(
            settings.ENCRYPTION_KEY.encode()
        )


    def encrypt(
        self,
        value: str,
    ) -> str:

        return self.fernet.encrypt(
            value.encode()
        ).decode()



    def decrypt(
        self,
        value: str,
    ) -> str:

        return self.fernet.decrypt(
            value.encode()
        ).decode()



    @staticmethod
    def hash_password(
        password: str,
    ) -> str:

        return hashlib.sha256(
            password.encode()
        ).hexdigest()



    @staticmethod
    def generate_secret(
        length: int = 64,
    ) -> str:

        return secrets.token_urlsafe(
            length
        )
