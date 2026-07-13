"""
Hetzner Shop
Audit Log Database Model
"""

from __future__ import annotations

from enum import Enum as PyEnum

from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import Enum

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.infrastructure.database.base import (
    BaseModel,
)



class AuditAction(str, PyEnum):

    CREATE = "create"

    UPDATE = "update"

    DELETE = "delete"

    LOGIN = "login"

    LOGOUT = "logout"

    PAYMENT = "payment"

    PROVISION = "provision"

    SECURITY = "security"



class AuditLog(BaseModel):

    __tablename__ = "audit_logs"


    user_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="SET NULL",
        ),
        nullable=True,
        index=True,
    )


    action: Mapped[AuditAction] = mapped_column(
        Enum(AuditAction),
        nullable=False,
        index=True,
    )


    entity_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )


    entity_id: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )


    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )


    ip_address: Mapped[str | None] = mapped_column(
        String(45),
        nullable=True,
    )


    user_agent: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )
