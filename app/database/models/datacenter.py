"""
Hetzner Shop
Datacenter Model
"""

from __future__ import annotations

from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import BaseModel


class Datacenter(BaseModel):
    """
    Cached Hetzner datacenters.
    """

    __tablename__ = "datacenters"

    provider_datacenter_id: Mapped[int] = mapped_column(
        Integer,
        unique=True,
        nullable=False,
        index=True,
    )

    location_id: Mapped[int] = mapped_column(
        ForeignKey(
            "locations.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

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

    available: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    location = relationship(
        "Location",
        lazy="joined",
    )

    def __repr__(self) -> str:
        return (
            f"<Datacenter("
            f"name='{self.name}', "
            f"location_id={self.location_id}"
            f")>"
        )
