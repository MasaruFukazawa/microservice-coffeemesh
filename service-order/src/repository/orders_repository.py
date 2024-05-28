# -*- coding: utf-8 -*-

from repository.models import OrderItemModel, OrderModel
from service.orders_domain import Order


class OrderRepository:

    def __init__(self, session) -> None:
        self.__session = session

    def _get(self, id):
        return self.__session.query(OrderModel).filter(OrderModel.id == str(id)).first()

    def get(self, id) -> Order | None:
        order = self._get(id)

        if order is not None:
            return Order(**order.dict())

        return None

    def list(self, limit: int = None, **filters) -> list[Order]:

        query = self.__session.query(OrderModel)

        if "cancelled" in filters:
            cancelled = filters.pop("cancelled")

            if cancelled:
                query = query.filter(OrderModel.status == "cancelled")
            else:
                query = query.filter(OrderModel.status != "cancelled")

        records = query.filter_by(**filters).limit(limit).all()

        return [Order(**record.dict()) for record in records]

    def add(self, items) -> Order:
        recode: OrderModel = OrderModel(item=[OrderItemModel(**item) for item in items])
        self.__session.add(recode)

        return Order(**recode.dict(), order=recode)

    def update(self, id: int, **payload) -> Order:
        record = self._get(id)

        if "item" in payload:

            for item in record.items:
                self.__session.delete(item)

            record.items = [OrderItemModel(**item) for item in payload.pop("items")]

        for key, value in payload.items():
            setattr(record, key, value)

        return Order(**record.dict())

    def delete(self, id) -> None:
        self.__session.delete(self._get(id))
