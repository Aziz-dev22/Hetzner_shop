"""
Hetzner Shop
User Domain Events
"""

from dataclasses import dataclass


@dataclass
class UserRegistered:

    user_id: int

    telegram_id: int

    username: str | None
