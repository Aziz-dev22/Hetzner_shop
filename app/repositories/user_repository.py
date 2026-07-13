"""
Hetzner Shop
User Repository
"""

from __future__ import annotations

from sqlalchemy import select

from app.database.models.user import User
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):

    def __init__(self, session):
        super().__init__(session, User)

    async def get_by_telegram_id(
        self,
        telegram_id: int,
    ) -> User | None:

        result = await self.session.execute(
            select(User).where(
                User.telegram_id == telegram_id
            )
        )

        return result.scalar_one_or_none()

    async def get_by_username(
        self,
        username: str,
    ) -> User | None:

        result = await self.session.execute(
            select(User).where(
                User.username == username
            )
        )

        return result.scalar_one_or_none()

    async def exists(
        self,
        telegram_id: int,
    ) -> bool:

        user = await self.get_by_telegram_id(
            telegram_id
        )

        return user is not None
