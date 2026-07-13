"""
Hetzner Shop
Wallet Model
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


class Wallet(BaseModel):

    __tablename__ = "wallets"

    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        unique=True,
        nullable=False,
        index=True,
    )

    currency: Mapped[str] = mapped_column(
        String(10),
        default="EUR",
        nullable=False,
    )

    balance: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    locked_balance: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    user = relationship(
        "User",
        lazy="joined",
    )

    transactions = relationship(
        "WalletTransaction",
        back_populates="wallet",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return (
            f"<Wallet("
            f"user={self.user_id}, "
            f"balance={self.balance}"
            f")>"
        )
