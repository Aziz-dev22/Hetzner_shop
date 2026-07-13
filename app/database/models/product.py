"""
Hetzner Shop
Product Model
"""

from __future__ import annotations

from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import BaseModel


class Product(BaseModel):
    """
    Sellable products.
    """

    __tablename__ = "products"

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        index=True,
    )

    slug: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False,
        index=True,
    )

    provider: Mapped[str] = mapped_column(
        String(30),
        default="hetzner",
        nullable=False,
    )

    server_type_id: Mapped[int] = mapped_column(
        ForeignKey(
            "server_types.id",
            ondelete="RESTRICT",
        ),
        nullable=False,
    )

    image_id: Mapped[int] = mapped_column(
        ForeignKey(
            "images.id",
            ondelete="RESTRICT",
        ),
        nullable=False,
    )

    location_id: Mapped[int] = mapped_column(
        ForeignKey(
            "locations.id",
            ondelete="RESTRICT",
        ),
        nullable=False,
    )

    selling_price: Mapped[float] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    monthly_cost: Mapped[float] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    currency: Mapped[str] = mapped_column(
        String(10),
        default="EUR",
        nullable=False,
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    sort_order: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    server_type = relationship("ServerType")
    image = relationship("Image")
    location = relationship("Location")
