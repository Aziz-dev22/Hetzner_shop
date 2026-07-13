"""
Hetzner Shop
Base Repository
"""

from __future__ import annotations


from typing import Generic
from typing import TypeVar
from typing import Type


from sqlalchemy import select


from sqlalchemy.ext.asyncio import (
    AsyncSession,
)


from app.infrastructure.database.base import (
    BaseModel,
)



ModelType = TypeVar(
    "ModelType",
    bound=BaseModel,
)



class BaseRepository(
    Generic[ModelType]
):


    def __init__(
        self,
        model: Type[ModelType],
        session: AsyncSession,
    ):

        self.model = model

        self.session = session



    async def get(
        self,
        object_id: int,
    ) -> ModelType | None:


        result = await self.session.execute(
            select(self.model)
            .where(
                self.model.id ==
                object_id
            )
        )


        return (
            result
            .scalar_one_or_none()
        )



    async def get_all(
        self,
    ) -> list[ModelType]:


        result = await self.session.execute(
            select(self.model)
        )


        return list(
            result.scalars()
            .all()
        )



    async def create(
        self,
        obj: ModelType,
    ) -> ModelType:


        self.session.add(
            obj
        )


        await self.session.flush()


        return obj



    async def update(
        self,
        obj: ModelType,
    ) -> ModelType:


        self.session.add(
            obj
        )


        await self.session.flush()


        return obj



    async def delete(
        self,
        obj: ModelType,
    ):


        obj.is_deleted = True


        await self.session.flush()
