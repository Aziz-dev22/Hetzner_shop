"""
Hetzner Shop
Dependency Injection Container
"""

from __future__ import annotations


from sqlalchemy.ext.asyncio import (
    AsyncSession,
)


from app.repositories import (
    UserRepository,
    ProductRepository,
    OrderRepository,
    ServerRepository,
    PaymentRepository,
)


from app.services.user_service import (
    UserService,
)



class Container:


    def __init__(
        self,
        session: AsyncSession,
    ):

        self.session = session


        self._user_repository = (
            UserRepository(
                session
            )
        )


        self._product_repository = (
            ProductRepository(
                session
            )
        )


        self._order_repository = (
            OrderRepository(
                session
            )
        )


        self._server_repository = (
            ServerRepository(
                session
            )
        )


        self._payment_repository = (
            PaymentRepository(
                session
            )
        )



    @property
    def users(
        self,
    ):

        return self._user_repository



    @property
    def products(
        self,
    ):

        return self._product_repository



    @property
    def orders(
        self,
    ):

        return self._order_repository



    @property
    def servers(
        self,
    ):

        return self._server_repository



    @property
    def payments(
        self,
    ):

        return self._payment_repository



    def user_service(
        self,
    ):

        return UserService(
            self.session
        )
