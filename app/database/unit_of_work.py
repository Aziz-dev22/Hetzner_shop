"""
Hetzner Shop
Unit Of Work
"""

from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.user_repository import UserRepository
from app.repositories.wallet_repository import WalletRepository
from app.repositories.order_repository import OrderRepository
from app.repositories.payment_repository import PaymentRepository


class UnitOfWork:

    def __init__(self, session: AsyncSession):
        self.session = session

        self.users = UserRepository(session)
        self.wallets = WalletRepository(session)
        self.orders = OrderRepository(session)
        self.payments = PaymentRepository(session)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if exc_type:
            await self.session.rollback()
        else:
            await self.session.commit()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
