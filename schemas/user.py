"""
Hetzner Shop
User Schemas
"""

from __future__ import annotations


from datetime import datetime



from pydantic import BaseModel, EmailStr



class UserBase(BaseModel):

    email: EmailStr

    username: str



class UserCreate(
    UserBase
):

    password: str



class UserLogin(BaseModel):

    email: EmailStr

    password: str



class UserResponse(
    UserBase
):

    id: int

    is_active: bool

    is_admin: bool

    created_at: datetime



    class Config:

        from_attributes = True
