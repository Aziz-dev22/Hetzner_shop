"""
Hetzner Shop
Payment Repository
"""

from __future__ import annotations


from sqlalchemy import select


from sqlalchemy.ext.asyncio import (
    AsyncSession,
)


from app.database.models import (
    Payment,
    PaymentStatus,
)


from app.repositories.base_repository import (
    BaseRepository,
)



class PaymentRepository(
    BaseRepository[Payment]
):


    def __init__(
        self,
        session: AsyncSession,
    ):

        super().__init__(
            Payment,
            session,
        )



    async def get_by_transaction_id(
        self,
        transaction_id: str,
    ) -> Payment | None:


        result = await self.session.execute(

            select(Payment)
            .where(
                Payment.transaction_id
                ==
                transaction_id
            )

        )


        return (
            result
            .scalar_one_or_none()
        )



    async def get_user_payments(
        self,
        user_id: int,
    ) -> list[Payment]:


        result = await self.session.execute(

            select(Payment)
            .where(
                Payment.user_id ==
                user_id
            )
            .order_by(
                Payment.created_at.desc()
            )

        )


        return list(
            result.scalars()
            .all()
        )



    async def get_successful_payments(
        self,
    ) -> list[Payment]:


        result = await self.session.execute(

            select(Payment)
            .where(
                Payment.status ==
                PaymentStatus.SUCCESS
            )

        )


        return list(
            result.scalars()
            .all()
        )



    async def update_status(
        self,
        payment: Payment,
        status: PaymentStatus,
    ) -> Payment:


        payment.status = status


        await self.session.flush()


        return payment
