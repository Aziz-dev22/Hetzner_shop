"""
Hetzner Shop
Payment Service
"""

from __future__ import annotations


from sqlalchemy.ext.asyncio import (
    AsyncSession,
)


from app.repositories import (
    PaymentRepository,
    OrderRepository,
)


from app.database.models import (
    Payment,
    PaymentStatus,
    OrderStatus,
)



class PaymentService:


    def __init__(
        self,
        session: AsyncSession,
    ):

        self.payment_repository = (
            PaymentRepository(session)
        )

        self.order_repository = (
            OrderRepository(session)
        )



    async def create_payment(
        self,
        payment: Payment,
    ) -> Payment:


        return await (
            self.payment_repository
            .create(payment)
        )



    async def confirm_payment(
        self,
        payment: Payment,
    ) -> Payment:


        payment.status = (
            PaymentStatus.SUCCESS
        )


        if payment.order_id:

            order = await (
                self.order_repository
                .get(
                    payment.order_id
                )
            )


            if order:

                order.status = (
                    OrderStatus.PAID
                )


                await (
                    self.order_repository
                    .update(order)
                )


        return await (
            self.payment_repository
            .update(payment)
        )



    async def fail_payment(
        self,
        payment: Payment,
    ) -> Payment:


        payment.status = (
            PaymentStatus.FAILED
        )


        return await (
            self.payment_repository
            .update(payment)
        )



    async def get_by_transaction_id(
        self,
        transaction_id: str,
    ):


        return await (
            self.payment_repository
            .get_by_transaction_id(
                transaction_id
            )
      )
