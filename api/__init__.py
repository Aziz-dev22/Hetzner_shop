"""
Hetzner Shop
API Router Package
"""

from fastapi import APIRouter


from api.auth import router as auth_router

from api.users import router as users_router

from api.servers import router as servers_router

from api.orders import router as orders_router

from api.admin import router as admin_router



api_router = APIRouter()



api_router.include_router(

    auth_router

)


api_router.include_router(

    users_router

)


api_router.include_router(

    servers_router

)


api_router.include_router(

    orders_router

)


api_router.include_router(

    admin_router

)
