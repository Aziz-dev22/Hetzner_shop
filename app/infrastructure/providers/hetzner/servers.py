"""
Hetzner Shop
Hetzner Server Provider
"""

from __future__ import annotations

from app.infrastructure.providers.hetzner.client import (
    HetznerClient,
)


class HetznerServerProvider:


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
        location: str | None = None,
        ssh_keys: list[int] | None = None,
    ):

        payload = {
            "name": name,
            "server_type": server_type,
            "image": image,
        }


        if location:
            payload["location"] = location


        if ssh_keys:
            payload["ssh_keys"] = ssh_keys


        return await self.client.request(
            "POST",
            "/servers",
            json=payload,
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


    async def reboot_server(
        self,
        server_id: int,
    ):

        return await self.client.request(
            "POST",
            f"/servers/{server_id}/actions/reboot",
        )


    async def power_on(
        self,
        server_id: int,
    ):

        return await self.client.request(
            "POST",
            f"/servers/{server_id}/actions/poweron",
        )


    async def power_off(
        self,
        server_id: int,
    ):

        return await self.client.request(
            "POST",
            f"/servers/{server_id}/actions/poweroff",
        )
