"""
Hetzner Shop
Web Dashboard
"""

from __future__ import annotations


from fastapi import APIRouter


from fastapi.responses import HTMLResponse



router = APIRouter(

    prefix="/dashboard",

    tags=["Dashboard"]

)



@router.get(

    "/",

    response_class=HTMLResponse

)

async def dashboard():


    return """

    <html>

        <head>

            <title>

                Dashboard

            </title>

        </head>


        <body>


            <h1>

                Hetzner Shop Dashboard

            </h1>


            <hr>


            <p>

                Users: 0

            </p>


            <p>

                Servers: 0

            </p>


            <p>

                Orders: 0

            </p>


        </body>


    </html>

    """
