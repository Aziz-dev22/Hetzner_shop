"""
Hetzner Shop
SSH Key Model
"""

from __future__ import annotations

from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import BaseModel


class SSHKey(BaseModel):
    """
    Cached Hetzner SSH Keys.
    """

    __tablename__ = "ssh_keys"

    provider_account_id: Mapped[int] = mapped_column(
        ForeignKey(
            "provider_accounts.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    provider_ssh_key_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    fingerprint: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    public_key: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    is_default: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
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
            f"<SSHKey("
            f"id={self.id}, "
            f"name='{self.name}'"
            f")>"
        )
