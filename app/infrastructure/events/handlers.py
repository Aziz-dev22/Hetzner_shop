"""
Hetzner Shop
Event Handler Registration
"""

from app.domain.events.user_events import UserRegistered
from app.infrastructure.events.event_bus import EventBus


def register_event_handlers(
    bus: EventBus,
):

    from app.application.handlers.user_registered import (
        user_registered_handler
    )

    bus.register(
        UserRegistered,
        user_registered_handler,
    )
