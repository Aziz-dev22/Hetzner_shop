"""
Hetzner Shop
Main Application Entry
"""

from __future__ import annotations


from contextlib import asynccontextmanager


from fastapi import FastAPI



from core.config import settings



@asynccontextmanager
async def lifespan(
    app: FastAPI,
):

    print(
        "Starting Hetzner Shop..."
    )


    # Startup tasks:
    # - Database connection
    # - Cache connection
    # - Worker initialization


    yield


    print(
        "Stopping Hetzner Shop..."
    )


    # Shutdown tasks:
    # - Close connections
    # - Cleanup resources



app = FastAPI(

    title=settings.APP_NAME,

    version="1.0.0",

    lifespan=lifespan,

)



@app.get("/")
async def root():


    return {

        "app": settings.APP_NAME,

        "status": "running",

        "version": "1.0.0",

    }



@app.get("/health")
async def health():


    return {

        "status": "healthy"

    }
