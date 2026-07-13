"""
Hetzner Shop
Database Base Models
"""

from __future__ import annotations


from datetime import datetime


from sqlalchemy import (
    DateTime,
    Boolean,
)


from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)



class Base(
    DeclarativeBase
):
    pass




class BaseModel(
    Base
):

    __abstract__ = True



    id: Mapped[int] = mapped_column(

        primary_key=True,

        autoincrement=True,

    )



    created_at: Mapped[datetime] = mapped_column(

        DateTime,

        default=datetime.utcnow,

        nullable=False,

    )



    updated_at: Mapped[datetime] = mapped_column(

        DateTime,

        default=datetime.utcnow,

        onupdate=datetime.utcnow,

        nullable=False,

    )



    is_deleted: Mapped[bool] = mapped_column(

        Boolean,

        default=False,

        nullable=False,

    )
