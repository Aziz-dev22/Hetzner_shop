"""
Hetzner Shop
Database Tests
"""

from __future__ import annotations


import pytest



from database.base import Base


from database.session import engine



@pytest.mark.asyncio
async def test_database_connection():


    async with engine.begin() as connection:


        result = await connection.run_sync(

            lambda conn:

            conn.execute(

                Base.metadata.tables

            )

        )


        assert result is not None



def test_models_registered():


    tables = Base.metadata.tables.keys()


    assert "users" in tables

    assert "servers" in tables

    assert "orders" in tables

    assert "invoices" in tables

    assert "payments" in tables

    assert "subscriptions" in tables
