"""
Hetzner Shop
Security Utilities
"""

from __future__ import annotations


from datetime import datetime, timedelta, timezone


from jose import jwt


from passlib.context import CryptContext


from core.config import settings





pwd_context = CryptContext(

    schemes=["bcrypt"],

    deprecated="auto"

)



ALGORITHM = "HS256"





def hash_password(

    password: str

):


    return pwd_context.hash(password)





def verify_password(

    plain_password: str,

    hashed_password: str,

):


    return pwd_context.verify(

        plain_password,

        hashed_password

    )





def create_access_token(

    data: dict,

    expires_minutes: int = 60,

):


    payload = data.copy()



    expire = datetime.now(

        timezone.utc

    ) + timedelta(

        minutes=expires_minutes

    )



    payload.update(

        {

            "exp": expire

        }

    )



    token = jwt.encode(

        payload,

        settings.JWT_SECRET_KEY,

        algorithm=ALGORITHM

    )



    return token





def decode_access_token(

    token: str

):


    try:


        payload = jwt.decode(

            token,

            settings.JWT_SECRET_KEY,

            algorithms=[ALGORITHM]

        )


        return payload



    except Exception:


        return None
