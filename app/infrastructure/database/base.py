"""
Hetzner Shop
Database Base Models
"""

from __future__ import annotations

import uuid

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass



class BaseModel(Base):

    __abstract__ = True


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )


    public_id: Mapped[str] = mapped_column(
        String(32),
        unique=True,
        nullable=False,
        default=lambda:
            uuid.uuid4()
            .hex[:16]
            .upper(),
        index=True,
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
        index=True,
    )
