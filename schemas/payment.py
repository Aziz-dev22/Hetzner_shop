"""
Hetzner Shop
Payment Schemas
"""

from __future__ import annotations


from datetime import datetime


from pydantic import BaseModel



class PaymentBase(BaseModel):

    gateway: str

    amount: int

    currency: str = "EUR"



class PaymentCreate(
    PaymentBase
):

    invoice_id: int



class PaymentResponse(
    PaymentBase
):

    id: int

    invoice_id: int

    transaction_id: str

    status: str

    created_at: datetime



    class Config:

        from_attributes = True
