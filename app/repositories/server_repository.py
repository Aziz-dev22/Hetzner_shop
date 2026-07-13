"""
Hetzner Shop
Server Repository
"""

from __future__ import annotations


from sqlalchemy import select


from sqlalchemy.ext.asyncio import (
    AsyncSession,
)


from app.database.models import (
    Server,
    ServerStatus,
)


from app.repositories.base_repository import (
    BaseRepository,
)



class ServerRepository(
    BaseRepository[Server]
):


    def __init__(
        self,
        session: AsyncSession,
    ):

        super().__init__(
            Server,
            session,
        )



    async def get_by_provider_id(
        self,
        provider_server_id: int,
    ) -> Server | None:


        result = await self.session.execute(

            select(Server)
            .where(
                Server.provider_server_id
                ==
                provider_server_id
            )

        )


        return (
            result
            .scalar_one_or_none()
        )



    async def get_user_servers(
        self,
        user_id: int,
    ) -> list[Server]:


        result = await self.session.execute(

            select(Server)
            .join(
                Server.order
            )
            .where(
                Server.order
                .has(
                    user_id=user_id
                )
            )

        )


        return list(
            result.scalars()
            .all()
        )



    async def get_active_servers(
        self,
    ) -> list[Server]:


        result = await self.session.execute(

            select(Server)
            .where(
                Server.status ==
                ServerStatus.RUNNING
            )

        )


        return list(
            result.scalars()
            .all()
        )



    async def update_status(
        self,
        server: Server,
        status: ServerStatus,
    ) -> Server:


        server.status = status


        await self.session.flush()


        return server
