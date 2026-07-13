"""
Hetzner Shop
Application Scheduler
"""

from __future__ import annotations


from apscheduler.schedulers.asyncio import (
    AsyncIOScheduler,
)


from app.workers import (
    ProvisionWorker,
    SyncWorker,
)



class AppScheduler:


    def __init__(
        self,
        session_factory,
    ):

        self.scheduler = (
            AsyncIOScheduler()
        )

        self.session_factory = (
            session_factory
        )



    def start(
        self,
    ):


        self.scheduler.add_job(

            self.run_provision,

            "interval",

            seconds=60,

        )


        self.scheduler.add_job(

            self.run_sync,

            "interval",

            minutes=10,

        )


        self.scheduler.start()



    async def run_provision(
        self,
    ):


        async with (
            self.session_factory()
            as session
        ):

            worker = (
                ProvisionWorker(
                    session
                )
            )


            await worker.run()



    async def run_sync(
        self,
    ):


        async with (
            self.session_factory()
            as session
        ):

            worker = (
                SyncWorker(
                    session
                )
            )


            await worker.run()
