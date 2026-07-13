"""
Hetzner Shop
Health Check System
"""

from __future__ import annotations


import subprocess
import asyncio



from sqlalchemy import text


from app.infrastructure.database.session import (
    SessionFactory,
)



async def check_database():

    try:

        async with SessionFactory() as session:

            await session.execute(
                text("SELECT 1")
            )


        print(
            "Database: OK"
        )


        return True


    except Exception as error:

        print(
            f"Database: FAILED - {error}"
        )


        return False



def check_service():


    result = subprocess.run(

        [

            "systemctl",

            "is-active",

            "hetzner-shop",

        ],

        capture_output=True,

        text=True,

    )


    if result.stdout.strip() == "active":

        print(
            "Service: OK"
        )


        return True



    print(
        "Service: FAILED"
    )


    return False



async def health_check():


    print(
        "Running health check..."
    )


    database = await (
        check_database()
    )


    service = (
        check_service()
    )


    if database and service:

        print(
            "System Healthy"
        )

        return True



    print(
        "System Problem Detected"
    )

    return False



if __name__ == "__main__":

    asyncio.run(
        health_check()
    )
