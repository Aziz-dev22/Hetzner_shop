"""
Hetzner Shop
Network Model
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


class Network(BaseModel):
    """
    Cached Hetzner Networks.
    """

    __tablename__ = "networks"

    provider_account_id: Mapped[int] = mapped_column(
        ForeignKey(
            "provider_accounts.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    provider_network_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
        index=True,
    )

    ip_range: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
    )

    network_zone: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    subnet_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    available: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    provider_account = relationship(
        "ProviderAccount",
        lazy="joined",
    )

    def __repr__(self) -> str:
        return (
            f"<Network("
            f"id={self.id}, "
            f"name='{self.name}'"
            f")>"
        )
