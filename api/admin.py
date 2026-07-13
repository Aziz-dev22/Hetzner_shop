"""
Hetzner Shop
Admin API
"""

from __future__ import annotations


from fastapi import (

    APIRouter,

    Depends,

    HTTPException,

)



from core.dependencies import (

    get_current_user,

)



router = APIRouter(

    prefix="/api/admin",

    tags=["Admin"]

)



async def admin_required(

    user = Depends(

        get_current_user

    ),

):


    # در نسخه نهایی از دیتابیس بررسی می‌شود

    # که کاربر نقش Admin دارد یا خیر


    if not user:

        raise HTTPException(

            status_code=403,

            detail="Admin access required",

        )


    return user



@router.get("/dashboard")
async def dashboard(

    admin = Depends(

        admin_required

    ),

):


    return {

        "message": "Admin dashboard",

        "admin_id": admin["id"],

    }



@router.get("/stats")
async def statistics(

    admin = Depends(

        admin_required

    ),

):


    return {

        "users": 0,

        "servers": 0,

        "orders": 0,

    }
