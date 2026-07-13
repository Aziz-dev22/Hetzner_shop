"""
Hetzner Shop
Main Application
"""

from __future__ import annotations


from fastapi import FastAPI


from core.config import settings


from api import (

    auth,

    users,

    servers,

    orders,

    admin,

)



app = FastAPI(

    title=settings.APP_NAME,

    version="1.0.0",

    description="Hetzner Cloud VPS Management Platform",

)



@app.get("/")

async def root():

    return {

        "status": "online",

        "application": settings.APP_NAME,

        "version": "1.0.0",

    }



@app.get("/health")

async def health_check():

    return {

        "status": "healthy"

    }



# API Routers


app.include_router(

    auth.router,

    prefix="/api/auth",

    tags=["Authentication"]

)



app.include_router(

    users.router,

    prefix="/api/users",

    tags=["Users"]

)



app.include_router(

    servers.router,

    prefix="/api/servers",

    tags=["Servers"]

)



app.include_router(

    orders.router,

    prefix="/api/orders",

    tags=["Orders"]

)



app.include_router(

    admin.router,

    prefix="/api/admin",

    tags=["Admin"]

)
