"""
Hetzner Shop
Invoice Database Model
"""

from __future__ import annotations


from datetime import datetime, timezone



from sqlalchemy import (

    String,

    Integer,

    DateTime,

    ForeignKey,

)



from sqlalchemy.orm import (

    Mapped,

    mapped_column,

    relationship,

)



from database.base import Base



class Invoice(Base):

    __tablename__ = "invoices"



    id: Mapped[int] = mapped_column(

        primary_key=True,

        index=True,

    )



    order_id: Mapped[int] = mapped_column(

        ForeignKey(

            "orders.id"

        ),

        nullable=False,

    )



    user_id: Mapped[int] = mapped_column(

        ForeignKey(

            "users.id"

        ),

        nullable=False,

    )



    amount: Mapped[int] = mapped_column(

        Integer,

        nullable=False,

    )



    currency: Mapped[str] = mapped_column(

        String(10),

        default="EUR",

    )



    status: Mapped[str] = mapped_column(

        String(50),

        default="unpaid",

    )



    invoice_number: Mapped[str] = mapped_column(

        String(100),

        unique=True,

        nullable=False,

    )



    created_at: Mapped[datetime] = mapped_column(

        DateTime(timezone=True),

        default=lambda:

            datetime.now(timezone.utc),

    )



    order = relationship(

        "Order",

        backref="invoice",

    )



    user = relationship(

        "User",

        backref="invoices",

    )
