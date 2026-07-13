"""
Hetzner Shop
Permission Database Model
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


class Permission(BaseModel):

    __tablename__ = "permissions"


    code: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )


    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )


    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )


    is_system: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )


    roles = relationship(
        "RolePermission",
        back_populates="permission",
    )
