"""
Hetzner Shop
Notification Service
"""

from __future__ import annotations


import httpx



from core.config import settings



class NotificationService:



    async def send_telegram(

        self,

        message: str,

    ):


        if not settings.TELEGRAM_NOTIFICATION_TOKEN:

            return False



        url = (

            "https://api.telegram.org/"

            f"bot{settings.TELEGRAM_NOTIFICATION_TOKEN}"

            "/sendMessage"

        )



        payload = {

            "chat_id":

            settings.TELEGRAM_NOTIFICATION_CHAT_ID,


            "text":

            message,

        }



        async with httpx.AsyncClient() as client:


            response = await client.post(

                url,

                json=payload,

            )



            return response.status_code == 200



    async def send_email(

        self,

        subject: str,

        message: str,

    ):


        # در نسخه بعدی با SMTP کامل می‌شود


        return True




    async def notify_server_created(

        self,

        server_name: str,

    ):


        return await self.send_telegram(

            f"Server created: {server_name}"

        )




    async def notify_payment_success(

        self,

        amount: int,

    ):


        return await self.send_telegram(

            f"Payment completed: {amount} EUR"

        )



notification_service = NotificationService()
