# -*- coding: utf-8 -*-

from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, conint, conlist, validator


class SizeEnum(Enum):
    """列挙スキーマ"""

    small = "small"
    medium = "medium"
    big = "big"


class StatusEnum(Enum):
    create = "create"
    paid = "paid"
    progress = "progress"
    cancelled = "cancelled"
    dispatched = "dispatched"
    delivered = "delivered"


class OrderItemSchema(BaseModel):
    product: str
    size: SizeEnum
    quantity: Optional[conint(ge=1, le=1000000, strict=True)] = 1

    @validator("quantity")
    def quantity_non_nullable(cls, value):
        assert value is not None, 'quantity may not be None'
        return value


class CreateOrderSchema(BaseModel):
    order: conlist(OrderItemSchema, min_length=1)


class GetOrderSchema(CreateOrderSchema):
    id: UUID
    created: datetime
    status: StatusEnum


class GetOrdersSchema(BaseModel):
    orders: list[GetOrderSchema]
