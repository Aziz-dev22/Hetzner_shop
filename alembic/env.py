from __future__ import annotations

import asyncio

from logging.config import fileConfig

from sqlalchemy import pool

from sqlalchemy.ext.asyncio import (
    async_engine_from_config,
)

from alembic import context


from app.core.config import (
    get_settings,
)

from app.infrastructure.database.base import (
    Base,
)


from app.database.models import *


config = context.config


if config.config_file_name:

    fileConfig(
        config.config_file_name
    )


target_metadata = Base.metadata



def run_migrations_offline():

    settings = get_settings()

    context.configure(
        url=settings.DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
    )


    with context.begin_transaction():

        context.run_migrations()



async def run_async_migrations():

    connectable = async_engine_from_config(
        {
            "sqlalchemy.url":
                get_settings()
                .DATABASE_URL
        },
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )


    async with connectable.connect() as connection:

        await connection.run_sync(
            do_run_migrations
        )


    await connectable.dispose()



def do_run_migrations(connection):

    context.configure(
        connection=connection,
        target_metadata=target_metadata,
    )


    with context.begin_transaction():

        context.run_migrations()



def run_migrations_online():

    asyncio.run(
        run_async_migrations()
    )


if context.is_offline_mode():

    run_migrations_offline()

else:

    run_migrations_online()
