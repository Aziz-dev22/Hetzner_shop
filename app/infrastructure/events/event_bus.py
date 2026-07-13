"""
Hetzner Shop
Async Event Bus
"""

from __future__ import annotations

from collections import defaultdict
from typing import Callable
from typing import Type


class EventBus:

    def __init__(self):

        self.handlers = defaultdict(list)


    def register(
        self,
        event_type: Type,
        handler: Callable,
    ):

        self.handlers[event_type].append(
            handler
        )


    async def publish(
        self,
        event,
    ):

        handlers = self.handlers.get(
            type(event),
            []
        )

        for handler in handlers:

            await handler(event)
