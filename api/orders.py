"""
Hetzner Shop
Orders API
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



from models.order import Order


from schemas.order import (

    OrderCreate,

)



router = APIRouter(

    prefix="/api/orders",

    tags=["Orders"]

)



@router.post("/")
async def create_order(

    data: OrderCreate,

    current_user = Depends(

        get_current_user

    ),

    db: AsyncSession = Depends(

        get_session

    ),

):


    order = Order(

        user_id=current_user["id"],

        server_type=data.server_type,

        location=data.location,

        amount=data.amount,

    )


    db.add(order)


    await db.commit()


    await db.refresh(order)



    return {

        "message": "Order created",

        "order_id": order.id,

    }



@router.get("/")
async def list_orders(

    current_user = Depends(

        get_current_user

    ),

):


    return {

        "user_id": current_user["id"],

        "orders": []

    }
