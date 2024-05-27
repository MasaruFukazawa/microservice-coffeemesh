# -*- coding: utf-8 -*-

import uuid
from datetime import datetime
from typing import Optional
from uuid import UUID

from fastapi import HTTPException
from starlette import status
from starlette.responses import Response

from ..app import app
from .schemas import CreateOrderSchema, GetOrderSchema, GetOrdersSchema

# orders = {
#    "id": "ff0f1355-e821-4178-9567-550dec27a373",
#    "status": "delivered",
#    "created": datetime.utcnow(),
#    "updated": datetime.utcnow(),
#    "order": [
#        {
#            "product": "cappuccino",
#            "size": "medium",
#            "quantity": 1,
#        }
#    ],
# }

ORDERS = []


@app.get("/orders", response_model=GetOrdersSchema)
def get_orders(cancelled: Optional[bool] = None, limit: Optional[int] = None):

    if cancelled is None and limit is None:
        return {"orders": ORDERS}

    query_set = [order for order in ORDERS]

    if cancelled is not None:
        query_set = [order for order in query_set if order["status"] == "cancelled"]
    else:
        query_set = [order for order in query_set if order["status"] != "cancelled"]

    if (limit is not None) and (len(query_set) > limit):
        return {"orders": query_set[:limit]}

    return {"orders": query_set}


@app.get("/orders/{order_id}", response_model=GetOrderSchema)
def get_order(order_id: UUID):

    for order in ORDERS:
        if order["id"] == order_id:
            return order

    raise HTTPException(status_code=404, detail=f"Order with ID {order_id} not found")


@app.post("/orders", status_code=status.HTTP_201_CREATED, response_model=GetOrderSchema)
def create_order(order_details: CreateOrderSchema):
    order = order_details.dict()

    order["id"] = uuid.uuid4()
    order["created"] = datetime.utcnow()
    order["status"] = "created"

    ORDERS.append(order)

    return order


@app.put("/orders/{order_id}", response_model=GetOrderSchema)
def update_order(order_id: UUID, order_details: CreateOrderSchema):

    for order in ORDERS:
        if order["id"] == order_id:
            order.update(order_details.dict())
            return order

    raise HTTPException(status_code=404, detail=f"Order with ID {order_id} not found")


@app.delete("/orders/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: UUID):

    for index, order in enumerate(ORDERS):
        if order["id"] == order_id:
            ORDERS.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Order with ID {order_id} not found")


@app.post("/orders/{order_id}/cancel", response_model=GetOrderSchema)
def cancel_order(order_id: UUID):

    for order in ORDERS:
        if order["id"] == order_id:
            order["status"] = "cancelled"
            return order

    raise HTTPException(status_code=404, detail=f"Order with ID {order_id} not found")


@app.post("/orders/{order_id}/pay", response_model=GetOrderSchema)
def pay_order(order_id: UUID):
    for order in ORDERS:
        if order["id"] == order_id:
            order["status"] = "progress"
            return order

    raise HTTPException(status_code=404, detail=f"Order with ID {order_id} not found")
