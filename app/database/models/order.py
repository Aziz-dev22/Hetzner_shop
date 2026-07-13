"""
Hetzner Shop
Order Database Model
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



class OrderStatus(str, PyEnum):

    PENDING = "pending"

    PAID = "paid"

    PROVISIONING = "provisioning"

    ACTIVE = "active"

    SUSPENDED = "suspended"

    CANCELLED = "cancelled"



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


    product_id: Mapped[int] = mapped_column(
        ForeignKey(
            "products.id",
        ),
        nullable=False,
    )


    status: Mapped[OrderStatus] = mapped_column(
        Enum(OrderStatus),
        default=OrderStatus.PENDING,
        nullable=False,
        index=True,
    )


    quantity: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )


    total_amount: Mapped[Decimal] = mapped_column(
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


    user = relationship(
        "User",
        back_populates="orders",
    )


    product = relationship(
        "Product",
        back_populates="orders",
    )


    server = relationship(
        "Server",
        back_populates="order",
        uselist=False,
    )
