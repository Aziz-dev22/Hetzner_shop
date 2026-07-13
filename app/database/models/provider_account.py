"""
Hetzner Shop
Provider Account Model
"""

from __future__ import annotations

from enum import Enum

from sqlalchemy import Boolean
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import BaseModel


class ProviderType(str, Enum):
    HETZNER = "hetzner"


class ProviderAccountStatus(str, Enum):
    ACTIVE = "active"
    DISABLED = "disabled"
    INVALID_TOKEN = "invalid_token"
    ERROR = "error"


class ProviderAccount(BaseModel):

    __tablename__ = "provider_accounts"

    provider: Mapped[ProviderType] = mapped_column(
        SQLEnum(ProviderType),
        default=ProviderType.HETZNER,
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    api_token: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    is_default: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    status: Mapped[ProviderAccountStatus] = mapped_column(
        SQLEnum(ProviderAccountStatus),
        default=ProviderAccountStatus.ACTIVE,
        nullable=False,
        index=True,
    )

    auto_sync: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    last_sync_at: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    created_by: Mapped[int | None] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="SET NULL",
        ),
        nullable=True,
    )

    creator = relationship(
        "User",
        lazy="joined",
    )

    def __repr__(self) -> str:
        return (
            f"<ProviderAccount("
            f"{self.provider.value}, "
            f"{self.name}"
            f")>"
        )
