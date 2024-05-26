# -*- coding: utf-8 -*-

from marshmallow import EXCLUDE, Schema, fields, validate


class OrderItemSchema(Schema):

    class Meta:
        unknown = EXCLUDE

    product = fields.String(require=True)
    size = fields.String(
        require=True, validate=validate.OneOf(["small", "medium", "big"])
    )
    quantity = fields.Integer(
        require=True, validate=validate.Range(1, min_inclusive=True)
    )


class ScheduleOrderSchema(Schema):

    class Meta:
        unknown = EXCLUDE

    order = fields.List(fields.Nested(OrderItemSchema), require=True)


class GetScheduledOrderSchema(ScheduleOrderSchema):

    id = fields.UUID(required=True)
    scheduled = fields.DateTime(required=True)
    status = fields.String(
        require=True,
        validate=validate.OneOf(["pending", "progress", "cancelled", "finished"]),
    )


class GetScheduledOrdersSchema(Schema):

    class Meta:
        unknown = EXCLUDE

    schedules = fields.List(fields.Nested(GetScheduledOrderSchema), require=True)


class ScheduleStatusSchema(Schema):

    class Meta:
        unknown = EXCLUDE

    status = fields.String(
        require=True,
        validate=validate.OneOf(["pending", "progress", "cancelled", "finished"]),
    )


class GetKitchenScheduleParameters(Schema):

    class Meta:
        unknown = EXCLUDE

    # URLクエリパラメータのフィールドを定義
    progress = fields.Boolean()
    limit = fields.Integer()
    since = fields.DateTime()
