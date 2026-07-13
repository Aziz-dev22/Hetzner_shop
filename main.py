"""
Hetzner Shop
Main Application Entry
"""

from __future__ import annotations



from fastapi import FastAPI



from api import api_router


from web import web_router_group



from core.logger import logger



from core.config import settings



app = FastAPI(

    title=settings.APP_NAME,

    version="1.0.0",

)



# API Routes

app.include_router(

    api_router

)



# Web Routes

app.include_router(

    web_router_group

)



@app.on_event("startup")
async def startup_event():


    logger.info(

        "Hetzner Shop started"

    )



@app.on_event("shutdown")
async def shutdown_event():


    logger.info(

        "Hetzner Shop stopped"

    )



@app.get("/")
async def root():


    return {

        "application": settings.APP_NAME,

        "status": "running",

        "version": "1.0.0",

    }
