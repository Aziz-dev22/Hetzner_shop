"""
Hetzner Shop
Hetzner Location Provider
"""

from __future__ import annotations

from app.infrastructure.providers.hetzner.client import (
    HetznerClient,
)


class HetznerLocationProvider:


    def __init__(
        self,
        client: HetznerClient,
    ):
        self.client = client


    async def list_locations(
        self,
    ):

        return await self.client.request(
            "GET",
            "/locations",
        )


    async def get_location(
        self,
        location_id: int,
    ):

        return await self.client.request(
            "GET",
            f"/locations/{location_id}",
        )
