"""
Hetzner Shop
Authentication API
"""

from __future__ import annotations


from sqlalchemy.ext.asyncio import AsyncSession


from fastapi import (

    APIRouter,

    Depends,

    HTTPException,

)



from database.session import get_session


from models.user import User


from schemas.user import (

    UserCreate,

    UserLogin,

)



from core.security import (

    hash_password,

    verify_password,

    create_access_token,

)



router = APIRouter(

    prefix="/api/auth",

    tags=["Authentication"]

)



@router.post("/register")
async def register(

    data: UserCreate,

    db: AsyncSession = Depends(get_session),

):


    user = User(

        email=data.email,

        username=data.username,

        password_hash=hash_password(

            data.password

        ),

    )


    db.add(user)


    await db.commit()


    await db.refresh(user)


    return {

        "message": "User created",

        "user_id": user.id,

    }



@router.post("/login")
async def login(

    data: UserLogin,

    db: AsyncSession = Depends(get_session),

):


    result = await db.execute(

        User.__table__.select()

        .where(

            User.email == data.email

        )

    )


    user = result.fetchone()



    if not user:

        raise HTTPException(

            status_code=401,

            detail="Invalid credentials",

        )



    token = create_access_token(

        {

            "sub": str(user.id)

        }

    )


    return {

        "access_token": token,

        "token_type": "bearer",

  }
