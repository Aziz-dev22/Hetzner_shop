"""
Hetzner Shop
Order Service
"""

from __future__ import annotations


from decimal import Decimal


from sqlalchemy.ext.asyncio import (
    AsyncSession,
)


from app.repositories import (
    OrderRepository,
    ProductRepository,
)


from app.database.models import (
    Order,
    OrderStatus,
)



class OrderService:


    def __init__(
        self,
        session: AsyncSession,
    ):

        self.order_repository = (
            OrderRepository(session)
        )

        self.product_repository = (
            ProductRepository(session)
        )



    async def create_order(
        self,
        user_id: int,
        product_id: int,
    ) -> Order:


        product = await (
            self.product_repository
            .get(product_id)
        )


        if not product:

            raise ValueError(
                "Product not found"
            )


        if not product.is_active:

            raise ValueError(
                "Product unavailable"
            )


        order = Order(

            user_id=user_id,

            product_id=product.id,

            status=OrderStatus.PENDING,

            quantity=1,

            total_amount=(
                product.selling_price
            ),

            currency=(
                product.currency
            ),

        )


        return await (
            self.order_repository
            .create(order)
        )



    async def get_user_orders(
        self,
        user_id: int,
    ):

        return await (
            self.order_repository
            .get_user_orders(
                user_id
            )
        )



    async def mark_as_paid(
        self,
        order: Order,
    ):

        return await (
            self.order_repository
            .update_status(
                order,
                OrderStatus.PAID,
            )
  )
