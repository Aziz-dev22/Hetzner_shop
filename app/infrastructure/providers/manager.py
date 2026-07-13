"""
Hetzner Shop
Cloud Provider Manager
"""

from __future__ import annotations

from app.infrastructure.providers.base import (
    BaseProvider,
)


class ProviderManager:


    def __init__(self):

        self.providers: dict[str, BaseProvider] = {}


    def register(
        self,
        name: str,
        provider: BaseProvider,
    ):

        self.providers[name] = provider


    def get(
        self,
        name: str,
    ) -> BaseProvider:

        provider = self.providers.get(
            name
        )

        if not provider:
            raise ValueError(
                f"Provider '{name}' not found"
            )

        return provider


    def available(
        self,
    ) -> list[str]:

        return list(
            self.providers.keys()
        )
