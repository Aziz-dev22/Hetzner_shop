"""
Hetzner Shop
Provider Factory
"""

from __future__ import annotations

from app.infrastructure.providers.manager import (
    ProviderManager,
)

from app.infrastructure.providers.hetzner.client import (
    HetznerClient,
)

from app.infrastructure.providers.hetzner.servers import (
    HetznerServerProvider,
)

from app.infrastructure.providers.hetzner.images import (
    HetznerImageProvider,
)

from app.infrastructure.providers.hetzner.locations import (
    HetznerLocationProvider,
)

from app.infrastructure.providers.hetzner.server_types import (
    HetznerServerTypeProvider,
)



def create_provider_manager(
    hetzner_token: str,
) -> ProviderManager:


    manager = ProviderManager()


    client = HetznerClient(
        token=hetzner_token
    )


    hetzner = HetznerServerProvider(
        client
    )


    manager.register(
        "hetzner",
        hetzner,
    )


    return manager
