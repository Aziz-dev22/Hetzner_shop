"""
Hetzner Shop
Web Package
"""

from fastapi import APIRouter



from web.routes import router as web_router

from web.dashboard import router as dashboard_router



web_router_group = APIRouter()



web_router_group.include_router(

    web_router

)



web_router_group.include_router(

    dashboard_router

)



__all__ = [

    "web_router_group",

]
