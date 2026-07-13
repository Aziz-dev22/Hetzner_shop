"""
Hetzner Shop
Product Repository
"""

from __future__ import annotations


from sqlalchemy import select


from sqlalchemy.ext.asyncio import (
    AsyncSession,
)


from app.database.models import (
    Product,
)


from app.repositories.base_repository import (
    BaseRepository,
)



class ProductRepository(
    BaseRepository[Product]
):


    def __init__(
        self,
        session: AsyncSession,
    ):

        super().__init__(
            Product,
            session,
        )


    async def get_active_products(
        self,
    ) -> list[Product]:


        result = await self.session.execute(

            select(Product)
            .where(
                Product.is_active == True
            )

        )


        return list(
            result.scalars()
            .all()
        )



    async def get_by_slug(
        self,
        slug: str,
    ) -> Product | None:


        result = await self.session.execute(

            select(Product)
            .where(
                Product.slug == slug
            )

        )


        return (
            result
            .scalar_one_or_none()
        )



    async def get_by_provider_id(
        self,
        provider_product_id: str,
    ) -> Product | None:


        result = await self.session.execute(

            select(Product)
            .where(
                Product.provider_product_id
                ==
                provider_product_id
            )

        )


        return (
            result
            .scalar_one_or_none()
        )
