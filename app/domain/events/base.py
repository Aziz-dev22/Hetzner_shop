"""
Hetzner Shop
Base Domain Event
"""

from __future__ import annotations

from datetime import datetime
from dataclasses import dataclass
from uuid import UUID
from uuid import uuid4


@dataclass
class DomainEvent:

    event_id: UUID = uuid4()

    created_at: datetime = datetime.utcnow()
