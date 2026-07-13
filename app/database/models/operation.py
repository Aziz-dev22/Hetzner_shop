"""
Hetzner Shop
Operation Model
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


class OperationType(str, Enum):
    CREATE_SERVER = "create_server"
    DELETE_SERVER = "delete_server"
    REBUILD_SERVER = "rebuild_server"
    POWER_ON = "power_on"
    POWER_OFF = "power_off"
    REBOOT = "reboot"
    RESET_PASSWORD = "reset_password"
    ENABLE_RESCUE = "enable_rescue"
    DISABLE_RESCUE = "disable_rescue"
    ENABLE_BACKUP = "enable_backup"
    DISABLE_BACKUP = "disable_backup"
    CHANGE_NAME = "change_name"
    CHANGE_REVERSE_DNS = "change_reverse_dns"


class OperationStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    CANCELLED = "cancelled"


class Operation(BaseModel):

    __tablename__ = "operations"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    server_id: Mapped[int | None] = mapped_column(
        ForeignKey("servers.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    operation_type: Mapped[OperationType] = mapped_column(
        SQLEnum(OperationType),
        nullable=False,
        index=True,
    )

    status: Mapped[OperationStatus] = mapped_column(
        SQLEnum(OperationStatus),
        default=OperationStatus.PENDING,
        nullable=False,
        index=True,
    )

    requested_by: Mapped[str] = mapped_column(
        String(20),
        default="bot",
        nullable=False,
    )

    retry_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    error_message: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    user = relationship("User")

    server = relationship("Server")
