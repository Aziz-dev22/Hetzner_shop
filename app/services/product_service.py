"""
Hetzner Shop
Product Service
"""

from __future__ import annotations


from sqlalchemy.ext.asyncio import (
    AsyncSession,
)


from app.repositories import (
    ProductRepository,
)


from app.database.models import (
    Product,
)



class ProductService:


    def __init__(
        self,
        session: AsyncSession,
    ):

        self.repository = ProductRepository(
            session
        )



    async def get_available_products(
        self,
    ) -> list[Product]:


        return await (
            self.repository
            .get_active_products()
        )



    async def get_product(
        self,
        slug: str,
    ) -> Product | None:


        return await (
            self.repository
            .get_by_slug(
                slug
            )
        )



    async def create_product(
        self,
        product: Product,
    ) -> Product:


        return await (
            self.repository
            .create(
                product
            )
        )



    async def disable_product(
        self,
        product: Product,
    ) -> Product:


        product.is_active = False


        return await (
            self.repository
            .update(
                product
            )
        )
