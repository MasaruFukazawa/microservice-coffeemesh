# -*- coding: utf-8 -*-

from typing import Any

import requests

from service.exceptions import APIIntegrationError, InvalidActionError


class OrderItem:
    """
    注文アイテムドメイン
    .. 1注文ごとのアイテムごとのデータ
    """

    def __init__(self, id, product, quantity, size) -> None:
        self.id = id
        self.product = product
        self.quantity = quantity
        self.size = size


class Order:
    """
    注文ドメイン
    .. 1注文ごとのデータと機能
    """

    kitchen_base_url = "http://localhost:3000/kitchen"
    payments_base_url = "http://localhost:3001/payments"

    def __init__(
        self, id, created, items, status, schedule_id=None, delivery_id=None, order=None
    ) -> None:

        self.order = order
        self.id = id
        self.created = created
        self.items = items
        self.status = status
        self.schedule_id = schedule_id
        self.delivery_id = delivery_id

    @property
    def id(self):
        return self.id or self.order.id

    @property
    def created(self):
        return self.created or self.order.created

    @property
    def status(self):
        return self.status or self.order.status

    def cancel(self):
        """
        注文キャンセル処理
        """
        # 注文が処理中の場合は、厨房 API を呼び出してスケジュールをキャンセル
        if self.status == "progress":

            response = requests.post(
                f"{self.kitchen_base_url}/schedules/self.schedule_id/cancel",
                json={
                    "order": [item.dict() for item in self.items],
                },
            )

            if response.status_code == 200:
                return

            raise APIIntegrationError(f"{self.id}の注文はキャンセルできませんでした。")

    def pay(self):
        """
        支払い処理
        """
        # 支払いAPIを呼び出して支払い処理を行う
        response = requests.post(
            f"{self.payments_base_url}",
            json={
                "order_id": self.id,
            },
        )

        if response.status_code == 201:
            return

        raise APIIntegrationError(f"{self.id}の注文の支払いができませんでした。")

    def schedule(self):
        """
        スケジュール処理
        """
        response = requests.post(
            f"{self.kitchen_base_url}/schedules",
            json={
                "order": [item.dict() for item in self.items],
            },
        )

        if response.status_code == 201:
            return response.json()["id"]

        raise APIIntegrationError(f"{self.id}の注文はスケジュールできませんでした。")
