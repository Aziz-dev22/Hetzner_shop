"""
Hetzner Shop
Application Entry Point
"""

from __future__ import annotations


import asyncio


from app.core.logging import (
    setup_logging,
)


from app.infrastructure.database.session import (
    SessionFactory,
)


from app.scheduler import (
    AppScheduler,
)



logger = setup_logging()



async def startup():


    logger.info(
        "Starting Hetzner Shop..."
    )


    scheduler = AppScheduler(
        SessionFactory
    )


    scheduler.start()


    logger.info(
        "Scheduler started"
    )


    while True:

        await asyncio.sleep(
            3600
        )



async def shutdown():


    logger.info(
        "Application stopped"
    )



async def main():


    try:

        await startup()


    except KeyboardInterrupt:

        await shutdown()



if __name__ == "__main__":

    asyncio.run(
        main()
  )
