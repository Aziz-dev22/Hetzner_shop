"""
Hetzner Shop
Order Schemas
"""

from __future__ import annotations


from datetime import datetime


from pydantic import BaseModel



class OrderBase(BaseModel):

    server_type: str

    location: str



class OrderCreate(
    OrderBase
):

    amount: int



class OrderResponse(
    OrderBase
):

    id: int

    user_id: int

    amount: int

    currency: str

    status: str

    payment_status: str

    created_at: datetime



    class Config:

        from_attributes = True
