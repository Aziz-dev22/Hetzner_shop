"""
Hetzner Shop
Audit Log Model
"""

from __future__ import annotations

from enum import Enum

from sqlalchemy import Enum as SQLEnum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import BaseModel


class AuditAction(str, Enum):
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    LOGIN = "login"
    LOGOUT = "logout"
    PAYMENT = "payment"
    SERVER = "server"
    ORDER = "order"
    SETTING = "setting"
    PROVIDER = "provider"


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
        SQLEnum(AuditAction),
        nullable=False,
        index=True,
    )

    resource: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    resource_id: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
        index=True,
    )

    ip_address: Mapped[str | None] = mapped_column(
        String(45),
        nullable=True,
    )

    user_agent: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    details: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    user = relationship(
        "User",
        lazy="joined",
    )

    def __repr__(self) -> str:
        return (
            f"<AuditLog("
            f"id={self.id}, "
            f"action={self.action.value}, "
            f"resource={self.resource}"
            f")>"
  )
