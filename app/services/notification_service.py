"""
Hetzner Shop
Notification Service
"""

from __future__ import annotations


class NotificationService:


    async def send(
        self,
        user_id: int,
        template: str,
        data: dict,
    ):

        notification = {
            "user_id": user_id,
            "template": template,
            "data": data,
            "status": "pending",
        }


        # در نسخه بعد:
        # ذخیره در Database
        # ارسال به Queue Worker

        return notification
