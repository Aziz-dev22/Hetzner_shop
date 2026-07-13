"""
Hetzner Shop
Order Model
"""

from __future__ import annotations

from enum import Enum

from sqlalchemy import Enum as SQLEnum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import BaseModel


class OrderStatus(str, Enum):
    PENDING = "pending"
    WAITING_PAYMENT = "waiting_payment"
    PAID = "paid"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"


class Order(BaseModel):

    __tablename__ = "orders"

    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    order_number: Mapped[str] = mapped_column(
        String(32),
        unique=True,
        nullable=False,
        index=True,
    )

    status: Mapped[OrderStatus] = mapped_column(
        SQLEnum(OrderStatus),
        default=OrderStatus.PENDING,
        nullable=False,
        index=True,
    )

    currency: Mapped[str] = mapped_column(
        String(10),
        default="EUR",
        nullable=False,
    )

    subtotal_amount: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    discount_amount: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    tax_amount: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    total_amount: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    notes: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    user = relationship(
        "User",
        lazy="joined",
    )

    items = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<Order #{self.order_number}>"
