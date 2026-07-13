"""
Hetzner Shop
Server Database Model
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



class Server(Base):

    __tablename__ = "servers"



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



    hetzner_id: Mapped[int | None] = mapped_column(

        Integer,

        unique=True,

        nullable=True,

    )



    name: Mapped[str] = mapped_column(

        String(100),

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



    ipv4: Mapped[str | None] = mapped_column(

        String(50),

        nullable=True,

    )



    status: Mapped[str] = mapped_column(

        String(50),

        default="creating",

    )



    created_at: Mapped[datetime] = mapped_column(

        DateTime(timezone=True),

        default=lambda:

            datetime.now(timezone.utc),

    )



    user = relationship(

        "User",

        backref="servers",

    )
