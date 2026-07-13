"""
Hetzner Shop
Subscription Schemas
"""

from __future__ import annotations


from datetime import datetime


from pydantic import BaseModel



class SubscriptionBase(BaseModel):

    plan: str



class SubscriptionCreate(
    SubscriptionBase
):

    server_id: int



class SubscriptionResponse(
    SubscriptionBase
):

    id: int

    user_id: int

    server_id: int

    status: str

    started_at: datetime

    expires_at: datetime



    class Config:

        from_attributes = True
