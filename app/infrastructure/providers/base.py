"""
Hetzner Shop
Base Cloud Provider
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    async def create_server(
        self,
        **kwargs,
    ):
        pass


    @abstractmethod
    async def delete_server(
        self,
        server_id: int,
    ):
        pass


    @abstractmethod
    async def reboot_server(
        self,
        server_id: int,
    ):
        pass


    @abstractmethod
    async def get_server(
        self,
        server_id: int,
    ):
        pass


    @abstractmethod
    async def list_servers(
        self,
    ):
        pass
