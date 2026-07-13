"""
Hetzner Shop
Hetzner Cloud API Client
"""

from __future__ import annotations


import httpx


from app.core.config import (
    get_settings,
)


class HetznerClient:


    BASE_URL = (
        "https://api.hetzner.cloud/v1"
    )


    def __init__(self):

        settings = get_settings()

        self.token = (
            settings.HETZNER_API_TOKEN
        )


        self.client = httpx.AsyncClient(

            base_url=self.BASE_URL,

            headers={

                "Authorization":
                f"Bearer {self.token}",

                "Content-Type":
                "application/json",

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

            endpoint,

            **kwargs,

        )


        response.raise_for_status()


        return response.json()



    async def close(
        self,
    ):

        await self.client.aclose()
