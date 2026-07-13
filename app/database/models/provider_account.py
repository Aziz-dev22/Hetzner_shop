"""
Hetzner Shop
Provider Account Model
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


class ProviderType(str, Enum):
    HETZNER = "hetzner"


class ProviderStatus(str, Enum):
    ACTIVE = "active"
    DISABLED = "disabled"
    ERROR = "error"


class ProviderAccount(BaseModel):
    """
    Provider accounts (Hetzner).
    """

    __tablename__ = "provider_accounts"

    provider: Mapped[str] = mapped_column(
        String(30),
        default=ProviderType.HETZNER.value,
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    api_token: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    is_default: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default=ProviderStatus.ACTIVE.value,
        nullable=False,
    )

    owner_user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
    )

    project_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    account_email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    server_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    last_sync_at: Mapped[str | None] = mapped_column(
        String(40),
        nullable=True,
    )

    last_error: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    owner = relationship(
        "User",
        lazy="joined",
    )

    def __repr__(self) -> str:
        return (
            f"<ProviderAccount("
            f"id={self.id}, "
            f"name='{self.name}', "
            f"provider='{self.provider}'"
            f")>"
  )
