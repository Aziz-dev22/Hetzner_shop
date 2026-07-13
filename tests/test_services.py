"""
Hetzner Shop
Services Tests
"""

from __future__ import annotations



from services.hetzner_api import HetznerAPI


from services.server_manager import ServerManager


from services.payment_service import PaymentService


from services.notification import NotificationService


from services.subscription_manager import SubscriptionManager




def test_hetzner_service_exists():


    service = HetznerAPI()


    assert service is not None



def test_server_manager_exists():


    manager = ServerManager()


    assert manager is not None



def test_payment_service_exists():


    service = PaymentService()


    assert service is not None



def test_notification_service_exists():


    service = NotificationService()


    assert service is not None



def test_subscription_manager_exists():


    manager = SubscriptionManager()


    assert manager is not None
