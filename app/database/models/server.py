"""
Hetzner Shop
Server Database Model
"""

from __future__ import annotations

from datetime import datetime

from enum import Enum as PyEnum

from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Enum

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.infrastructure.database.base import (
    BaseModel,
)


class ServerStatus(str, PyEnum):

    CREATING = "creating"

    RUNNING = "running"

    STOPPED = "stopped"

    ERROR = "error"

    DELETED = "deleted"



class Server(BaseModel):

    __tablename__ = "servers"


    order_id: Mapped[int] = mapped_column(
        ForeignKey(
            "orders.id",
            ondelete="CASCADE",
        ),
        unique=True,
        nullable=False,
    )


    provider: Mapped[str] = mapped_column(
        String(50),
        default="hetzner",
        nullable=False,
    )


    provider_server_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        unique=True,
        index=True,
    )


    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )


    ipv4: Mapped[str | None] = mapped_column(
        String(45),
        nullable=True,
    )


    ipv6: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )


    location: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )


    status: Mapped[ServerStatus] = mapped_column(
        Enum(ServerStatus),
        default=ServerStatus.CREATING,
        nullable=False,
        index=True,
    )


    expires_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )


    auto_renew: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )


    order = relationship(
        "Order",
        back_populates="server",
    )
