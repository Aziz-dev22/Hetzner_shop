"""
Hetzner Shop
Subscription Manager Service
"""

from __future__ import annotations


from datetime import datetime, timezone, timedelta



from sqlalchemy.ext.asyncio import AsyncSession



from models.subscription import Subscription



class SubscriptionManager:



    async def create_subscription(

        self,

        db: AsyncSession,

        user_id: int,

        server_id: int,

        plan: str,

        days: int = 30,

    ):


        now = datetime.now(

            timezone.utc

        )


        subscription = Subscription(

            user_id=user_id,

            server_id=server_id,

            plan=plan,

            status="active",

            started_at=now,

            expires_at=(

                now +

                timedelta(

                    days=days

                )

            ),

        )


        db.add(subscription)


        await db.commit()


        await db.refresh(subscription)


        return subscription



    async def check_expiration(

        self,

        subscription: Subscription,

    ):


        now = datetime.now(

            timezone.utc

        )


        if subscription.expires_at <= now:


            subscription.status = "expired"


            return True



        return False



    async def renew_subscription(

        self,

        db: AsyncSession,

        subscription: Subscription,

        days: int = 30,

    ):


        subscription.expires_at += timedelta(

            days=days

        )


        subscription.status = "active"


        await db.commit()


        return subscription



subscription_manager = SubscriptionManager()
