"""
Hetzner Shop
Wallet Database Model
"""

from __future__ import annotations

from decimal import Decimal

from sqlalchemy import String
from sqlalchemy import Numeric
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.infrastructure.database.base import (
    BaseModel,
)



class Wallet(BaseModel):

    __tablename__ = "wallets"


    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        unique=True,
        nullable=False,
    )


    currency: Mapped[str] = mapped_column(
        String(10),
        default="EUR",
        nullable=False,
    )


    balance: Mapped[Decimal] = mapped_column(
        Numeric(
            12,
            2,
        ),
        default=Decimal("0.00"),
        nullable=False,
    )


    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )


    user = relationship(
        "User",
        back_populates="wallet",
    )


    transactions = relationship(
        "WalletTransaction",
        back_populates="wallet",
    )
