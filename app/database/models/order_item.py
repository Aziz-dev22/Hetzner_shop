"""
Hetzner Shop
Order Item Model
"""

from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import BaseModel


class OrderItem(BaseModel):

    __tablename__ = "order_items"

    order_id: Mapped[int] = mapped_column(
        ForeignKey(
            "orders.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey(
            "products.id",
            ondelete="RESTRICT",
        ),
        nullable=False,
        index=True,
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        default=1,
        nullable=False,
    )

    unit_price: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    total_price: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    currency: Mapped[str] = mapped_column(
        String(10),
        default="EUR",
        nullable=False,
    )

    product_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    server_type_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    image_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    location_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    configuration: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    order = relationship(
        "Order",
        back_populates="items",
    )

    product = relationship(
        "Product",
        lazy="joined",
    )

    def __repr__(self) -> str:
        return (
            f"<OrderItem("
            f"id={self.id}, "
            f"product='{self.product_name}'"
            f")>"
        )
