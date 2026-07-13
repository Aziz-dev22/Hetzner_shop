"""
Hetzner Shop
Server Service
"""

from __future__ import annotations


from sqlalchemy.ext.asyncio import (
    AsyncSession,
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



class ServerService:


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



    async def create_server_record(
        self,
        order_id: int,
        provider_server_id: int,
        name: str,
        ipv4: str | None = None,
    ) -> Server:


        server = Server(

            order_id=order_id,

            provider_server_id=(
                provider_server_id
            ),

            name=name,

            ipv4=ipv4,

            status=(
                ServerStatus.RUNNING
            ),

        )


        return await (
            self.server_repository
            .create(server)
        )



    async def mark_server_error(
        self,
        server: Server,
    ) -> Server:


        server.status = (
            ServerStatus.ERROR
        )


        return await (
            self.server_repository
            .update(server)
        )



    async def delete_server_record(
        self,
        server: Server,
    ) -> Server:


        server.status = (
            ServerStatus.DELETED
        )


        return await (
            self.server_repository
            .update(server)
        )
