"""
Hetzner Shop
Security Module
"""

from __future__ import annotations


from datetime import datetime, timedelta, timezone


from passlib.context import CryptContext


from jose import jwt



from core.config import settings



pwd_context = CryptContext(

    schemes=["bcrypt"],

    deprecated="auto"

)



ALGORITHM = "HS256"



ACCESS_TOKEN_EXPIRE_MINUTES = 60



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
    expires_minutes: int = ACCESS_TOKEN_EXPIRE_MINUTES,
):


    payload = data.copy()


    expire = (

        datetime.now(
            timezone.utc
        )

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

        settings.JWT_SECRET_KEY,

        algorithm=ALGORITHM,

    )



def decode_access_token(
    token: str,
):


    return jwt.decode(

        token,

        settings.JWT_SECRET_KEY,

        algorithms=[ALGORITHM],

    )
