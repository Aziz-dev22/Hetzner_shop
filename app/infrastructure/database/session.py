"""
Hetzner Shop
Database Session Manager
"""

from __future__ import annotations


from sqlalchemy.ext.asyncio import (
    create_async_engine,
)

from sqlalchemy.ext.asyncio import (
    AsyncSession,
)

from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
)


from app.core.config import (
    get_settings,
)



settings = get_settings()



engine = create_async_engine(

    settings.DATABASE_URL,

    echo=settings.DEBUG,

    pool_pre_ping=True,

)



SessionFactory = async_sessionmaker(

    bind=engine,

    class_=AsyncSession,

    expire_on_commit=False,

)



async def get_session():

    async with SessionFactory() as session:

        try:

            yield session


        finally:

            await session.close()
