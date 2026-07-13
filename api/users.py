"""
Hetzner Shop
Users API
"""

from __future__ import annotations


from fastapi import (

    APIRouter,

    Depends,

)



from core.dependencies import (

    get_current_user,

)



router = APIRouter(

    prefix="/api/users",

    tags=["Users"]

)



@router.get("/me")
async def get_profile(

    current_user = Depends(

        get_current_user

    ),

):


    return {

        "user": current_user

    }
