"""
Hetzner Shop
Role Database Model
"""

from __future__ import annotations

from sqlalchemy import String
from sqlalchemy import Boolean

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.infrastructure.database.base import (
    BaseModel,
)



class Role(BaseModel):

    __tablename__ = "roles"


    name: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )


    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )


    is_system: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )


    users = relationship(
        "User",
        back_populates="role",
    )
