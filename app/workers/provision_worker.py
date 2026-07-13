"""
Hetzner Shop
Provision Worker
"""

from __future__ import annotations


from sqlalchemy.ext.asyncio import (
    AsyncSession,
)


from sqlalchemy import select


from app.database.models import (
    Order,
    OrderStatus,
)


from app.services.provision_service import (
    ProvisionService,
)



class ProvisionWorker:


    def __init__(
        self,
        session: AsyncSession,
    ):

        self.session = session



    async def run(
        self,
    ):


        result = await self.session.execute(

            select(Order)
            .where(
                Order.status ==
                OrderStatus.PAID
            )

        )


        orders = (
            result.scalars()
            .all()
        )


        provision_service = (
            ProvisionService(
                self.session
            )
        )


        for order in orders:

            try:

                await (
                    provision_service
                    .provision(
                        order_id=order.id,

                        name=(
                            f"server-{order.id}"
                        ),

                        server_type="cx22",

                        image="ubuntu-24.04",

                        location="fsn1",

                    )
                )


            except Exception as error:

                print(
                    f"Provision failed: {error}"
                )
