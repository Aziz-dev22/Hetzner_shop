"""
Hetzner Shop
Hetzner Cloud API Service
"""

from __future__ import annotations


import httpx



from core.config import settings



class HetznerAPI:


    BASE_URL = (

        "https://api.hetzner.cloud/v1"

    )



    def __init__(self):


        self.headers = {

            "Authorization":

            f"Bearer {settings.HETZNER_API_TOKEN}",

            "Content-Type":

            "application/json",

        }



    async def get_servers(self):


        async with httpx.AsyncClient() as client:


            response = await client.get(

                f"{self.BASE_URL}/servers",

                headers=self.headers,

            )


            return response.json()



    async def create_server(

        self,

        name: str,

        server_type: str,

        location: str,

    ):


        payload = {


            "name": name,


            "server_type": server_type,


            "location": location,


            "image": "ubuntu-24.04",

        }



        async with httpx.AsyncClient() as client:


            response = await client.post(

                f"{self.BASE_URL}/servers",

                headers=self.headers,

                json=payload,

            )


            return response.json()



    async def delete_server(

        self,

        server_id: int,

    ):


        async with httpx.AsyncClient() as client:


            response = await client.delete(

                f"{self.BASE_URL}/servers/{server_id}",

                headers=self.headers,

            )


            return response.status_code



hetzner = HetznerAPI()
