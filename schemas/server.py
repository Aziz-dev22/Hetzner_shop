"""
Hetzner Shop
Server Schemas
"""

from __future__ import annotations


from datetime import datetime


from pydantic import BaseModel



class ServerBase(BaseModel):

    name: str

    server_type: str

    location: str



class ServerCreate(
    ServerBase
):

    pass



class ServerResponse(
    ServerBase
):

    id: int

    user_id: int

    hetzner_id: int | None

    ipv4: str | None

    status: str

    created_at: datetime



    class Config:

        from_attributes = True
