"""
Hetzner Shop
User Registered Event Handler
"""

from __future__ import annotations

from app.domain.events.user_events import UserRegistered
from app.services.notification_service import NotificationService


async def user_registered_handler(
    event: UserRegistered,
):

    notification_service = (
        NotificationService()
    )

    await notification_service.send(
        user_id=event.user_id,
        template="welcome_user",
        data={
            "username": event.username,
        },
    )
