"""
Hetzner Shop
Background Tasks
"""

from __future__ import annotations



from workers.celery_app import celery_app



@celery_app.task
def check_subscriptions():

    """
    بررسی اشتراک‌های منقضی شده
    """

    return {

        "task": "check_subscriptions",

        "status": "completed",

    }



@celery_app.task
def send_notification(

    message: str,

):

    """
    ارسال اعلان پس‌زمینه
    """

    return {

        "message": message,

        "status": "queued",

    }



@celery_app.task
def sync_hetzner_servers():

    """
    همگام‌سازی اطلاعات سرورها
    """

    return {

        "task": "sync_servers",

        "status": "completed",

    }
