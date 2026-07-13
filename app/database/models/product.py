"""
Hetzner Shop
Product Database Model
"""

from __future__ import annotations

from decimal import Decimal

from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Numeric
from sqlalchemy import Integer

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.infrastructure.database.base import (
    BaseModel,
)



class Product(BaseModel):

    __tablename__ = "products"


    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )


    slug: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False,
        index=True,
    )


    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )


    provider: Mapped[str] = mapped_column(
        String(50),
        default="hetzner",
        nullable=False,
    )


    provider_product_id: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )


    cpu_cores: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )


    ram_gb: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )


    storage_gb: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )


    traffic_tb: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )


    cost_price: Mapped[Decimal] = mapped_column(
        Numeric(
            12,
            2,
        ),
        nullable=False,
    )


    selling_price: Mapped[Decimal] = mapped_column(
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


    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )


    orders = relationship(
        "Order",
        back_populates="product",
    )
