"""
Hetzner Shop
Invoice Schemas
"""

from __future__ import annotations


from datetime import datetime


from pydantic import BaseModel



class InvoiceBase(BaseModel):

    amount: int

    currency: str = "EUR"



class InvoiceResponse(
    InvoiceBase
):

    id: int

    order_id: int

    user_id: int

    invoice_number: str

    status: str

    created_at: datetime



    class Config:

        from_attributes = True
