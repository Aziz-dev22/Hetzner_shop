"""
Hetzner Shop
User Service
"""

from __future__ import annotations

from datetime import datetime

from sqlalchemy import select

from sqlalchemy.ext.asyncio import (
    AsyncSession,
)

from app.database.models import (
    User,
    Role,
    Wallet,
)



class UserService:


    def __init__(
        self,
        session: AsyncSession,
    ):

        self.session = session



    async def get_by_telegram_id(
        self,
        telegram_id: int,
    ) -> User | None:


        result = await self.session.execute(
            select(User)
            .where(
                User.telegram_id ==
                telegram_id
            )
        )


        return result.scalar_one_or_none()



    async def create_user(
        self,
        telegram_id: int,
        first_name: str,
        username: str | None = None,
    ) -> User:


        customer_role = await self.session.execute(
            select(Role)
            .where(
                Role.name ==
                "CUSTOMER"
            )
        )


        role = (
            customer_role
            .scalar_one()
        )


        user = User(

            telegram_id=telegram_id,

            first_name=first_name,

            username=username,

            role_id=role.id,

            last_login_at=datetime.utcnow(),

        )


        self.session.add(
            user
        )


        await self.session.flush()



        wallet = Wallet(
            user_id=user.id
        )


        self.session.add(
            wallet
        )


        await self.session.commit()


        await self.session.refresh(
            user
        )


        return user



    async def update_last_login(
        self,
        user: User,
    ):


        user.last_login_at = (
            datetime.utcnow()
        )


        await self.session.commit()
