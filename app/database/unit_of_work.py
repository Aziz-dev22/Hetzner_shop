"""
Hetzner Shop
Unit Of Work
"""

from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession


class UnitOfWork:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if exc:
            await self.rollback()
        else:
            await self.commit()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()

    async def flush(self):
        await self.session.flush()

    async def refresh(self, instance):
        await self.session.refresh(instance)
