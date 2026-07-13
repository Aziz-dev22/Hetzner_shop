"""
Hetzner Shop
Server Provision Service
"""

from __future__ import annotations


from sqlalchemy.ext.asyncio import (
    AsyncSession,
)


from app.providers.factory import (
    ProviderFactory,
)


from app.repositories import (
    ServerRepository,
    OrderRepository,
)


from app.database.models import (
    Server,
    ServerStatus,
    OrderStatus,
)



class ProvisionService:


    def __init__(
        self,
        session: AsyncSession,
    ):

        self.server_repository = (
            ServerRepository(session)
        )

        self.order_repository = (
            OrderRepository(session)
        )

        self.provider = (
            ProviderFactory
            .create_server_provider()
        )



    async def provision(
        self,
        order_id: int,
        name: str,
        server_type: str,
        image: str,
        location: str,
    ) -> Server:


        order = await (
            self.order_repository
            .get(order_id)
        )


        if not order:

            raise ValueError(
                "Order not found"
            )


        if order.status != OrderStatus.PAID:

            raise ValueError(
                "Order is not paid"
            )



        order.status = (
            OrderStatus.PROVISIONING
        )


        await (
            self.order_repository
            .update(order)
        )



        response = await (
            self.provider
            .create_server(
                name=name,
                server_type=server_type,
                image=image,
                location=location,
            )
        )



        server_data = (
            response["server"]
        )



        server = Server(

            order_id=order.id,

            provider_server_id=(
                server_data["id"]
            ),

            name=(
                server_data["name"]
            ),

            status=(
                ServerStatus.RUNNING
            ),

        )


        await (
            self.server_repository
            .create(server)
        )


        order.status = (
            OrderStatus.ACTIVE
        )


        await (
            self.order_repository
            .update(order)
        )


        return server
