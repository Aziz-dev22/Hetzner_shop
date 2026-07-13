"""
Hetzner Shop
Subscription Database Model
"""

from __future__ import annotations


from datetime import datetime, timezone



from sqlalchemy import (

    String,

    DateTime,

    ForeignKey,

)



from sqlalchemy.orm import (

    Mapped,

    mapped_column,

    relationship,

)



from database.base import Base



class Subscription(Base):

    __tablename__ = "subscriptions"



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



    server_id: Mapped[int] = mapped_column(

        ForeignKey(

            "servers.id"

        ),

        nullable=False,

    )



    plan: Mapped[str] = mapped_column(

        String(100),

        nullable=False,

    )



    status: Mapped[str] = mapped_column(

        String(50),

        default="active",

    )



    started_at: Mapped[datetime] = mapped_column(

        DateTime(timezone=True),

        default=lambda:

            datetime.now(timezone.utc),

    )



    expires_at: Mapped[datetime] = mapped_column(

        DateTime(timezone=True),

        nullable=False,

    )



    user = relationship(

        "User",

        backref="subscriptions",

    )


    server = relationship(

        "Server",

        backref="subscription",

    )
