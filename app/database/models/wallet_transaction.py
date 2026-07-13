"""
Hetzner Shop
Wallet Transaction Database Model
"""

from __future__ import annotations

from decimal import Decimal

from sqlalchemy import String
from sqlalchemy import Numeric
from sqlalchemy import ForeignKey
from sqlalchemy import Enum

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from enum import Enum as PyEnum

from app.infrastructure.database.base import (
    BaseModel,
)


class TransactionType(str, PyEnum):

    DEPOSIT = "deposit"

    PAYMENT = "payment"

    REFUND = "refund"

    BONUS = "bonus"

    ADJUSTMENT = "adjustment"



class WalletTransaction(BaseModel):

    __tablename__ = "wallet_transactions"


    wallet_id: Mapped[int] = mapped_column(
        ForeignKey(
            "wallets.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )


    transaction_type: Mapped[
        TransactionType
    ] = mapped_column(
        Enum(TransactionType),
        nullable=False,
    )


    amount: Mapped[Decimal] = mapped_column(
        Numeric(
            12,
            2,
        ),
        nullable=False,
    )


    currency: Mapped[str] = mapped_column(
        String(10),
        default="EUR",
        nullable=False,
    )


    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )


    reference_id: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
        index=True,
    )


    wallet = relationship(
        "Wallet",
        back_populates="transactions",
    )
