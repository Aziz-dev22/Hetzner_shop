"""
Hetzner Shop
Registration Service
"""

from __future__ import annotations

from app.database.models.user import User
from app.database.unit_of_work import UnitOfWork


class RegistrationService:

    def __init__(
        self,
        uow: UnitOfWork,
    ):
        self.uow = uow

    async def register_user(
        self,
        telegram_id: int,
        username: str | None,
        first_name: str,
        last_name: str | None,
        language_code: str,
        default_role_id: int,
    ) -> User:

        existing_user = (
            await self.uow.users
            .get_by_telegram_id(
                telegram_id
            )
        )

        if existing_user:
            return existing_user


        user = await self.uow.users.create(
            telegram_id=telegram_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            language_code=language_code,
            role_id=default_role_id,
        )


        await self.uow.wallets.create(
            user_id=user.id,
            currency="EUR",
            balance=0,
        )


        await self.uow.user_preferences.create(
            user_id=user.id,
            language=language_code or "fa",
        )


        await self.uow.audit_logs.create(
            user_id=user.id,
            action="create",
            resource="user",
            resource_id=user.id,
            details="New user registered",
        )


        return user
