"""
Hetzner Shop
Hetzner Server API
"""

from __future__ import annotations


from app.providers.hetzner.client import (
    HetznerClient,
)



class HetznerServerAPI:


    def __init__(
        self,
        client: HetznerClient,
    ):

        self.client = client



    async def create_server(
        self,
        name: str,
        server_type: str,
        image: str,
        location: str,
    ):


        return await self.client.request(

            "POST",

            "/servers",

            json={

                "name": name,

                "server_type": server_type,

                "image": image,

                "location": location,

            },

        )



    async def get_server(
        self,
        server_id: int,
    ):


        return await self.client.request(

            "GET",

            f"/servers/{server_id}",

        )



    async def list_servers(
        self,
    ):


        return await self.client.request(

            "GET",

            "/servers",

        )



    async def delete_server(
        self,
        server_id: int,
    ):


        return await self.client.request(

            "DELETE",

            f"/servers/{server_id}",

        )
