"""
Hetzner Shop
Role Permission Association Model
"""

from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint


from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


from app.infrastructure.database.base import (
    BaseModel,
)



class RolePermission(BaseModel):

    __tablename__ = "role_permissions"


    role_id: Mapped[int] = mapped_column(
        ForeignKey(
            "roles.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )


    permission_id: Mapped[int] = mapped_column(
        ForeignKey(
            "permissions.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )


    role = relationship(
        "Role",
        back_populates="permissions",
    )


    permission = relationship(
        "Permission",
        back_populates="roles",
    )


    __table_args__ = (
        UniqueConstraint(
            "role_id",
            "permission_id",
            name="uq_role_permission",
        ),
    )
