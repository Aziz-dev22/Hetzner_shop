"""
Hetzner Shop
FastAPI Dependencies
"""

from __future__ import annotations


from typing import AsyncGenerator


from fastapi import Depends, HTTPException, status

from fastapi.security import OAuth2PasswordBearer



from core.security import (
    decode_access_token,
)


from database.session import (
    AsyncSessionLocal,
)



oauth2_scheme = OAuth2PasswordBearer(

    tokenUrl="/api/auth/login"

)



async def get_db()
-> AsyncGenerator:


    async with AsyncSessionLocal() as session:

        yield session



async def get_current_user(

    token: str = Depends(oauth2_scheme),

):


    try:

        payload = decode_access_token(

            token

        )


        user_id = payload.get(

            "sub"

        )


        if not user_id:

            raise Exception



        return {

            "id": user_id

        }



    except Exception:


        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="Invalid authentication token",

        )
