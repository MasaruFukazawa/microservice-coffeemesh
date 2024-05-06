# -*- coding: utf-8 -*-

from datetime import datetime
from uuid import UUID

from starlette import status
from starlette.responses import Response

from orders.app import app

from .schemas import CreateOrderSchema

orders = {
    "id": "ff0f1355-e821-4178-9567-550dec27a373",
    "status": "delivered",
    "created": datetime.utcnow(),
    "order": [
        {
            "product": "cappuccino",
            "size": "medium",
            "quantity": 1,
        }
    ],
}


@app.get("/orders")
def get_orders():
    return {"order": [orders]}


@app.get("/orders/{order_id}")
def get_order(order_id: UUID):
    return orders


@app.post("/orders", status_code=status.HTTP_201_CREATED)
def create_order(order_details: CreateOrderSchema):
    return orders


@app.put("/orders/{order_id}")
def update_order(order_id: UUID, order_details: CreateOrderSchema):
    return orders


@app.delete("/orders/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order():
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.post("/orders/{order_id}/cancel")
def cancel_order(order_id: UUID):
    return orders


@app.post("/orders/{order_id}/pay")
def pay_order(order_id: UUID):
    return orders
