"""
Hetzner Shop
User Model
"""

from __future__ import annotations

from enum import Enum

from sqlalchemy import BigInteger
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import BaseModel


class UserRole(str, Enum):
    OWNER = "owner"
    ADMIN = "admin"
    SUPPORT = "support"
    USER = "user"


class UserStatus(str, Enum):
    ACTIVE = "active"
    DISABLED = "disabled"
    BANNED = "banned"


class User(BaseModel):
    """
    Telegram users.
    """

    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        nullable=False,
        index=True,
    )

    username: Mapped[str | None] = mapped_column(
        String(64),
        nullable=True,
    )

    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    last_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    language: Mapped[str] = mapped_column(
        String(10),
        default="fa",
        nullable=False,
    )

    role: Mapped[str] = mapped_column(
        String(20),
        default=UserRole.USER.value,
        nullable=False,
        index=True,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default=UserStatus.ACTIVE.value,
        nullable=False,
        index=True,
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    is_bot_blocked: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    referral_code: Mapped[str | None] = mapped_column(
        String(32),
        unique=True,
        nullable=True,
    )

    invited_by_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
    )

    balance: Mapped[int] = mapped_column(
        default=0,
        nullable=False,
    )

    total_spent: Mapped[int] = mapped_column(
        default=0,
        nullable=False,
    )

    total_orders: Mapped[int] = mapped_column(
        default=0,
        nullable=False,
    )

    last_login_ip: Mapped[str | None] = mapped_column(
        String(45),
        nullable=True,
    )

    notes: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    invited_by = relationship(
        "User",
        remote_side="User.id",
        lazy="joined",
    )

    def __repr__(self) -> str:
        return (
            f"<User("
            f"id={self.id}, "
            f"telegram_id={self.telegram_id}, "
            f"role='{self.role}'"
            f")>"
  )
