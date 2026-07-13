"""
Hetzner Shop
Payment Service
"""

from __future__ import annotations


from sqlalchemy.ext.asyncio import AsyncSession



from models.payment import Payment


from models.invoice import Invoice



class PaymentService:



    async def create_payment(

        self,

        db: AsyncSession,

        invoice_id: int,

        gateway: str,

        amount: int,

        transaction_id: str,

    ):


        payment = Payment(

            invoice_id=invoice_id,

            gateway=gateway,

            amount=amount,

            transaction_id=transaction_id,

            status="pending",

        )


        db.add(payment)


        await db.commit()


        await db.refresh(payment)


        return payment



    async def confirm_payment(

        self,

        db: AsyncSession,

        payment: Payment,

    ):


        payment.status = "completed"



        invoice = await db.get(

            Invoice,

            payment.invoice_id

        )


        if invoice:

            invoice.status = "paid"



        await db.commit()



        return payment



    async def reject_payment(

        self,

        db: AsyncSession,

        payment: Payment,

    ):


        payment.status = "failed"


        await db.commit()


        return payment



payment_service = PaymentService()
