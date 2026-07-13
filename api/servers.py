"""
Hetzner Shop
Servers API
"""

from __future__ import annotations


from fastapi import (

    APIRouter,

    Depends,

)



from sqlalchemy.ext.asyncio import AsyncSession



from database.session import get_session


from core.dependencies import (

    get_current_user,

)



from models.server import Server



router = APIRouter(

    prefix="/api/servers",

    tags=["Servers"]

)



@router.get("/")
async def list_servers(

    current_user = Depends(

        get_current_user

    ),

    db: AsyncSession = Depends(

        get_session

    ),

):


    return {

        "user_id": current_user["id"],

        "servers": []

    }



@router.get("/{server_id}")
async def get_server(

    server_id: int,

    current_user = Depends(

        get_current_user

    ),

):


    return {

        "server_id": server_id,

        "owner": current_user["id"]

    }
