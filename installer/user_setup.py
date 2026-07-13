"""
Hetzner Shop
Initial Admin Setup
"""

from __future__ import annotations


import asyncio


from getpass import getpass



from app.infrastructure.database.session import (
    SessionFactory,
)


from app.database.models import (
    User,
    UserRole,
)


from app.core.security import (
    hash_password,
)



async def create_admin():


    print(
        "Creating admin user..."
    )


    username = input(

        "Admin username: "

    )


    email = input(

        "Admin email: "

    )


    password = getpass(

        "Admin password: "

    )



    async with SessionFactory() as session:


        admin = User(

            username=username,

            email=email,

            password_hash=(
                hash_password(password)
            ),

            role=UserRole.ADMIN,

            is_active=True,

        )


        session.add(
            admin
        )


        await session.commit()



    print(
        "Admin created successfully"
    )



def setup_admin():


    asyncio.run(
        create_admin()
    )



if __name__ == "__main__":

    setup_admin()
