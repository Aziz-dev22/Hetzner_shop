"""
Hetzner Shop
Celery Worker Configuration
"""

from __future__ import annotations


from celery import Celery



from core.config import settings



celery_app = Celery(

    "hetzner_shop",

    broker=(

        f"redis://"

        f"{settings.REDIS_HOST}:"

        f"{settings.REDIS_PORT}/0"

    ),

    backend=(

        f"redis://"

        f"{settings.REDIS_HOST}:"

        f"{settings.REDIS_PORT}/1"

    ),

)



celery_app.conf.update(

    task_serializer="json",

    accept_content=["json"],

    result_serializer="json",

    timezone=settings.SERVER_TIMEZONE,

)
