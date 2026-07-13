"""
Hetzner Shop
Cloud Provider Factory
"""

from __future__ import annotations


from app.core.config import (
    get_settings,
)


from app.providers.hetzner import (
    HetznerClient,
    HetznerServerAPI,
)



class ProviderFactory:


    @staticmethod
    def create_server_provider():

        settings = get_settings()


        provider = (
            settings.DEFAULT_PROVIDER
            .lower()
        )


        if provider == "hetzner":

            client = HetznerClient()

            return HetznerServerAPI(
                client
            )


        raise ValueError(
            f"Unsupported provider: {provider}"
        )
