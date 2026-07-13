"""
Hetzner Shop
Server Sync Worker
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
)


from app.database.models import (
    ServerStatus,
)



class SyncWorker:


    def __init__(
        self,
        session: AsyncSession,
    ):

        self.session = session


        self.repository = (
            ServerRepository(
                session
            )
        )


        self.provider = (
            ProviderFactory
            .create_server_provider()
        )



    async def run(
        self,
    ):


        servers = await (
            self.repository
            .get_active_servers()
        )


        for server in servers:


            try:

                response = await (
                    self.provider
                    .get_server(
                        server.provider_server_id
                    )
                )


                remote_server = (
                    response["server"]
                )


                remote_status = (
                    remote_server["status"]
                )


                if remote_status == "running":

                    server.status = (
                        ServerStatus.RUNNING
                    )


                elif remote_status == "stopped":

                    server.status = (
                        ServerStatus.STOPPED
                    )


                else:

                    server.status = (
                        ServerStatus.ERROR
                    )


                await (
                    self.repository
                    .update(
                        server
                    )
                )


            except Exception as error:

                print(
                    f"Sync failed: {error}"
                )
