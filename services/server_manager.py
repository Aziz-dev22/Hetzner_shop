"""
Hetzner Shop
Server Manager Service
"""

from __future__ import annotations


from sqlalchemy.ext.asyncio import AsyncSession



from models.server import Server


from services.hetzner_api import hetzner



class ServerManager:



    async def create_server(

        self,

        db: AsyncSession,

        user_id: int,

        name: str,

        server_type: str,

        location: str,

    ):


        response = await hetzner.create_server(

            name=name,

            server_type=server_type,

            location=location,

        )


        server_data = response.get(

            "server",

            {}

        )


        server = Server(

            user_id=user_id,

            hetzner_id=server_data.get(

                "id"

            ),

            name=name,

            server_type=server_type,

            location=location,

            status="running",

            ipv4=(

                server_data

                .get("public_net", {})

                .get("ipv4", {})

                .get("ip")

            ),

        )


        db.add(server)


        await db.commit()


        await db.refresh(server)


        return server



    async def delete_server(

        self,

        server_id: int,

    ):


        return await hetzner.delete_server(

            server_id

        )



server_manager = ServerManager()
