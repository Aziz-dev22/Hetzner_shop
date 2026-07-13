"""
Hetzner Shop
Order Database Model
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



class Order(Base):

    __tablename__ = "orders"



    id: Mapped[int] = mapped_column(

        primary_key=True,

        index=True,

    )



    user_id: Mapped[int] = mapped_column(

        ForeignKey(
            "users.id"
        ),

        nullable=False,

    )



    server_type: Mapped[str] = mapped_column(

        String(100),

        nullable=False,

    )



    location: Mapped[str] = mapped_column(

        String(100),

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

        default="pending",

    )



    payment_status: Mapped[str] = mapped_column(

        String(50),

        default="unpaid",

    )



    created_at: Mapped[datetime] = mapped_column(

        DateTime(timezone=True),

        default=lambda:

            datetime.now(timezone.utc),

    )



    user = relationship(

        "User",

        backref="orders",

  )
