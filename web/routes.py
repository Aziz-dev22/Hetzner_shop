"""
Hetzner Shop
Web Routes
"""

from __future__ import annotations


from fastapi import APIRouter, Request


from fastapi.responses import HTMLResponse



router = APIRouter(

    prefix="/web",

    tags=["Web"]

)



@router.get(

    "/",

    response_class=HTMLResponse

)

async def home(

    request: Request,

):


    return """

    <html>

        <head>

            <title>

                Hetzner Shop

            </title>

        </head>


        <body>

            <h1>

                Hetzner Shop Dashboard

            </h1>


            <p>

                Web Panel Running

            </p>

        </body>


    </html>

    """
