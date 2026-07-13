"""
Hetzner Shop
Base Repository
"""

from __future__ import annotations

from typing import Generic
from typing import Type
from typing import TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):

    def __init__(
        self,
        session: AsyncSession,
        model: Type[ModelType],
    ):
        self.session = session
        self.model = model

    async def get(self, obj_id: int):

        return await self.session.get(
            self.model,
            obj_id,
        )

    async def get_all(self):

        result = await self.session.execute(
            select(self.model)
        )

        return result.scalars().all()

    async def create(self, **kwargs):

        obj = self.model(**kwargs)

        self.session.add(obj)

        await self.session.flush()

        return obj

    async def delete(self, obj):

        await self.session.delete(obj)

    async def save(self):

        await self.session.commit()

    async def rollback(self):

        await self.session.rollback()
