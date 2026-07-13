"""
Hetzner Shop
Security Utilities
"""

from __future__ import annotations


from datetime import datetime
from datetime import timedelta


from passlib.context import CryptContext


from jose import jwt


from app.core.config import (
    get_settings,
)



pwd_context = CryptContext(

    schemes=[
        "bcrypt"
    ],

    deprecated="auto",

)



def hash_password(
    password: str,
) -> str:


    return pwd_context.hash(
        password
    )



def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:


    return pwd_context.verify(

        plain_password,

        hashed_password,

    )



def create_access_token(
    data: dict,
    expires_minutes: int = 60,
):


    settings = get_settings()


    payload = data.copy()


    expire = (
        datetime.utcnow()
        +
        timedelta(
            minutes=expires_minutes
        )
    )


    payload.update(

        {
            "exp": expire
        }

    )


    return jwt.encode(

        payload,

        settings.SECRET_KEY,

        algorithm="HS256",

    )



def decode_access_token(
    token: str,
):


    settings = get_settings()


    return jwt.decode(

        token,

        settings.SECRET_KEY,

        algorithms=[
            "HS256"
        ],

    )
