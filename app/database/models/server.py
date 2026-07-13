"""
Hetzner Shop
Server Model
"""

from __future__ import annotations

from enum import Enum

from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import BaseModel


class ServerStatus(str, Enum):
    CREATING = "creating"
    RUNNING = "running"
    STOPPED = "stopped"
    REBUILDING = "rebuilding"
    RESCUING = "rescue"
    DELETING = "deleting"
    DELETED = "deleted"
    ERROR = "error"


class Server(BaseModel):
    """
    Hetzner Cloud Server
    """

    __tablename__ = "servers"

    provider_account_id: Mapped[int] = mapped_column(
        ForeignKey(
            "provider_accounts.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    hetzner_server_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        unique=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
    )

    hostname: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default=ServerStatus.CREATING.value,
        nullable=False,
        index=True,
    )

    server_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    image: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    location: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    datacenter: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    ipv4: Mapped[str | None] = mapped_column(
        String(45),
        nullable=True,
    )

    ipv6: Mapped[str | None] = mapped_column(
        String(64),
        nullable=True,
    )

    rescue_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    backups_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    locked: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    monthly_price: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    labels: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    provider_account = relationship(
        "ProviderAccount",
        lazy="joined",
    )

    user = relationship(
        "User",
        lazy="joined",
    )

    def __repr__(self) -> str:
        return (
            f"<Server("
            f"id={self.id}, "
            f"hetzner_id={self.hetzner_server_id}, "
            f"name='{self.name}'"
            f")>"
  )
