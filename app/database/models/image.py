"""
Hetzner Shop
Image Model
"""

from __future__ import annotations

from enum import Enum

from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import BaseModel


class ImageType(str, Enum):
    SYSTEM = "system"
    APP = "app"
    SNAPSHOT = "snapshot"
    BACKUP = "backup"


class ImageStatus(str, Enum):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"


class Image(BaseModel):
    """
    Cached Hetzner images.
    """

    __tablename__ = "images"

    provider_image_id: Mapped[int] = mapped_column(
        Integer,
        unique=True,
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    image_type: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        index=True,
    )

    os_flavor: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    os_version: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    architecture: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    rapid_deploy: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    deprecated: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    available: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default=ImageStatus.AVAILABLE.value,
        nullable=False,
    )

    def __repr__(self) -> str:
        return (
            f"<Image("
            f"name='{self.name}', "
            f"type='{self.image_type}'"
            f")>"
        )
