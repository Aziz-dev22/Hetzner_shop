"""
Hetzner Shop
Payment Database Model
"""

from __future__ import annotations

from decimal import Decimal

from enum import Enum as PyEnum

from sqlalchemy import String
from sqlalchemy import Numeric
from sqlalchemy import ForeignKey
from sqlalchemy import Enum

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.infrastructure.database.base import (
    BaseModel,
)



class PaymentStatus(str, PyEnum):

    PENDING = "pending"

    PROCESSING = "processing"

    SUCCESS = "success"

    FAILED = "failed"

    CANCELLED = "cancelled"



class PaymentMethod(str, PyEnum):

    WALLET = "wallet"

    CARD = "card"

    CRYPTO = "crypto"

    MANUAL = "manual"



class Payment(BaseModel):

    __tablename__ = "payments"


    order_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "orders.id",
            ondelete="SET NULL",
        ),
        nullable=True,
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


    method: Mapped[PaymentMethod] = mapped_column(
        Enum(PaymentMethod),
        nullable=False,
    )


    status: Mapped[PaymentStatus] = mapped_column(
        Enum(PaymentStatus),
        default=PaymentStatus.PENDING,
        nullable=False,
        index=True,
    )


    gateway: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )


    transaction_id: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
        unique=True,
    )


    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )


    order = relationship(
        "Order",
    )


    user = relationship(
        "User",
    )
