"""
Hetzner Shop
Hetzner Server Types
"""

from __future__ import annotations

from sqlalchemy import Boolean
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import BaseModel


class ServerType(BaseModel):
    """
    Cached Hetzner server types.
    """

    __tablename__ = "server_types"

    provider_server_type_id: Mapped[int] = mapped_column(
        Integer,
        unique=True,
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

    architecture: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    cpu_cores: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    cpu_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    memory_gb: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    disk_gb: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    storage_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    hourly_price: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    monthly_price: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    traffic_included_tb: Mapped[int] = mapped_column(
        Integer,
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

    def __repr__(self) -> str:
        return (
            f"<ServerType("
            f"{self.name}, "
            f"{self.cpu_cores} CPU, "
            f"{self.memory_gb} GB RAM"
            f")>"
  )
