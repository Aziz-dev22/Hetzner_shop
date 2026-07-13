"""
Hetzner Shop
User Service
"""

from app.database.models.user import User
from app.database.unit_of_work import UnitOfWork


class UserService:

    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_or_create_user(
        self,
        telegram_id: int,
        username: str | None,
        first_name: str,
        last_name: str | None,
        language_code: str,
        default_role_id: int,
    ) -> User:

        user = await self.uow.users.get_by_telegram_id(
            telegram_id
        )

        if user:
            return user

        return await self.uow.users.create(
            telegram_id=telegram_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            language_code=language_code,
            role_id=default_role_id,
        )
