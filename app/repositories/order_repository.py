"""
Hetzner Shop
Order Repository
"""

from __future__ import annotations


from sqlalchemy import select


from sqlalchemy.ext.asyncio import (
    AsyncSession,
)


from app.database.models import (
    Order,
    OrderStatus,
)


from app.repositories.base_repository import (
    BaseRepository,
)



class OrderRepository(
    BaseRepository[Order]
):


    def __init__(
        self,
        session: AsyncSession,
    ):

        super().__init__(
            Order,
            session,
        )



    async def get_user_orders(
        self,
        user_id: int,
    ) -> list[Order]:


        result = await self.session.execute(

            select(Order)
            .where(
                Order.user_id ==
                user_id
            )
            .order_by(
                Order.created_at.desc()
            )

        )


        return list(
            result.scalars()
            .all()
        )



    async def get_pending_orders(
        self,
    ) -> list[Order]:


        result = await self.session.execute(

            select(Order)
            .where(
                Order.status ==
                OrderStatus.PENDING
            )

        )


        return list(
            result.scalars()
            .all()
        )



    async def get_provisioning_orders(
        self,
    ) -> list[Order]:


        result = await self.session.execute(

            select(Order)
            .where(
                Order.status ==
                OrderStatus.PROVISIONING
            )

        )


        return list(
            result.scalars()
            .all()
        )



    async def update_status(
        self,
        order: Order,
        status: OrderStatus,
    ) -> Order:


        order.status = status


        await self.session.flush()


        return order
