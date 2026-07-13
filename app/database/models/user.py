"""
Hetzner Shop
User Database Model
"""

from __future__ import annotations

from datetime import datetime

from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.infrastructure.database.base import (
    BaseModel,
)



class User(BaseModel):

    __tablename__ = "users"


    telegram_id: Mapped[int] = mapped_column(
        Integer,
        unique=True,
        nullable=False,
        index=True,
    )


    username: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
        index=True,
    )


    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )


    last_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )


    language_code: Mapped[str] = mapped_column(
        String(10),
        default="en",
        nullable=False,
    )


    role_id: Mapped[int] = mapped_column(
        ForeignKey(
            "roles.id"
        ),
        nullable=False,
    )


    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )


    last_login_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )


    role = relationship(
        "Role",
        back_populates="users",
    )


    wallet = relationship(
        "Wallet",
        back_populates="user",
        uselist=False,
    )


    orders = relationship(
        "Order",
        back_populates="user",
    )
