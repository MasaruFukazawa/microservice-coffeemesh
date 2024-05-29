# -*- coding: utf-8 -*-

import copy
from datetime import datetime

from ariadne import InterfaceType, ScalarType, UnionType

from web.data import INGREDIENTS

product_type = UnionType("Product")


@product_type.type_resolver
def resolve_product_type(obj, *_):
    if "hasFilling" in obj:
        return "Cake"

    return "Beverage"


product_interface = InterfaceType("ProductInterface")


@product_interface.field("ingredients")
def resolve_product_ingredients(product, _):
    recipe = [copy.copy(ingredient) for ingredient in product.get("ingredients", [])]

    for ingredient_recipe in recipe:
        for ingredient in INGREDIENTS:
            if ingredient["id"] == ingredient_recipe["ingredient"]:
                ingredient_recipe["ingredient"] = ingredient

    return recipe


datetime_scalar = ScalarType("Datetime")


@datetime_scalar.serializer
def serialize_datetime_scalar(date: datetime) -> str:
    return date.isoformat()


@datetime_scalar.value_parser
def parse_datetime_scalar(date: str) -> datetime:
    return datetime.fromisoformat(date)
