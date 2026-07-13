"""
Hetzner Shop
Hetzner API Client
"""

from __future__ import annotations

import httpx


class HetznerClient:


    BASE_URL = (
        "https://api.hetzner.cloud/v1"
    )


    def __init__(
        self,
        token: str,
    ):

        self.token = token

        self.client = httpx.AsyncClient(
            headers={
                "Authorization":
                    f"Bearer {token}"
            },
            timeout=30,
        )


    async def request(
        self,
        method: str,
        endpoint: str,
        **kwargs,
    ):

        response = await self.client.request(
            method,
            f"{self.BASE_URL}{endpoint}",
            **kwargs,
        )


        response.raise_for_status()

        return response.json()


    async def close(self):

        await self.client.aclose()
