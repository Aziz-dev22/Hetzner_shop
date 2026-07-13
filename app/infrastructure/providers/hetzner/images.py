"""
Hetzner Shop
Hetzner Image Provider
"""

from __future__ import annotations

from app.infrastructure.providers.hetzner.client import (
    HetznerClient,
)


class HetznerImageProvider:


    def __init__(
        self,
        client: HetznerClient,
    ):
        self.client = client


    async def list_images(
        self,
        type: str | None = None,
        status: str | None = None,
    ):

        params = {}

        if type:
            params["type"] = type

        if status:
            params["status"] = status


        return await self.client.request(
            "GET",
            "/images",
            params=params,
        )


    async def get_image(
        self,
        image_id: int,
    ):

        return await self.client.request(
            "GET",
            f"/images/{image_id}",
        )


    async def delete_image(
        self,
        image_id: int,
    ):

        return await self.client.request(
            "DELETE",
            f"/images/{image_id}",
        )


    async def create_snapshot(
        self,
        server_id: int,
        description: str,
    ):

        payload = {
            "type": "snapshot",
            "description": description,
        }


        return await self.client.request(
            "POST",
            f"/servers/{server_id}/actions/create_image",
            json=payload,
        )
