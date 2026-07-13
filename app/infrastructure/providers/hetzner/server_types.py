"""
Hetzner Shop
Hetzner Server Type Provider
"""

from __future__ import annotations

from app.infrastructure.providers.hetzner.client import (
    HetznerClient,
)


class HetznerServerTypeProvider:


    def __init__(
        self,
        client: HetznerClient,
    ):
        self.client = client


    async def list_server_types(
        self,
    ):

        return await self.client.request(
            "GET",
            "/server_types",
        )


    async def get_server_type(
        self,
        server_type_id: int,
    ):

        return await self.client.request(
            "GET",
            f"/server_types/{server_type_id}",
        )
