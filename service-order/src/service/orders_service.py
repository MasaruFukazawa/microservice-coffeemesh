# -*- coding: utf-8 -*-

from ..repository.orders_repository import OrderRepository
from .exceptions import OrderNotFoundError


class OrderService:
    """
    注文サービス
    """

    def __init__(self, orders_repository):
        self.orders_repository = orders_repository

    def place_order(self, item):
        # データベースレコードを作成して注文を実行
        return self.orders_repository.add(item)

    def get_order(self, order_id):
        order = self.orders_repository.get(order_id)

        if order is not None:
            return order

        raise OrderNotFoundError(f"{self.id}の注文が見つかりません。")

    def update_order(self, order_id, items):
        order = self.orders_repository.get(order_id)

        if order is None:
            raise OrderNotFoundError(f"{self.id}の注文が見つかりません。")

        return self.orders_repository.update(order_id, {"items": items})

    def list_orders(self, **filters):
        limit = filters.pop("limite", None)
        return self.orders_repository.list(limit, **filters)

    def pay_order(self, order_id):
        order = self.orders_repository.get(order_id)

        if order is None:
            raise OrderNotFoundError(f"{self.id}の注文が見つかりません。")

        order.pay()

        schedule_id = order.schedule()

        return self.orders_repository.update(
            order_id, status="progress", schedule_id=schedule_id
        )

    def cancel_order(self, order_id):
        order = self.orders_repository.get(order_id)

        if order is None:
            raise OrderNotFoundError(f"{self.id}の注文が見つかりません。")

        order.cancel()

        return self.orders_repository.update(order_id, status="cancelled")
