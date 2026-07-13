"""
Hetzner Shop
User Service
"""

from __future__ import annotations

from app.database.unit_of_work import UnitOfWork
from app.database.models.user import User
from app.repositories.user_repository import UserRepository


class UserService:

    def __init__(self, uow: UnitOfWork):
        self.uow = uow
        self.users = UserRepository(uow.session)

    async def get_or_create_user(
        self,
        telegram_id: int,
        username: str | None,
        first_name: str,
        last_name: str | None,
        language_code: str,
        default_role_id: int,
    ) -> User:

        user = await self.users.get_by_telegram_id(
            telegram_id
        )

        if user:
            return user

        user = await self.users.create(
            telegram_id=telegram_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            language_code=language_code,
            role_id=default_role_id,
        )

        return user
