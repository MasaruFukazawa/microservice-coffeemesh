# -*- coding: utf-8 -*-

from copy import deepcopy
from itertools import islice

from ariadne import QueryType

from web.data import INGREDIENTS, PRODUCTS

query = QueryType()


def get_page(items, item_per_page, page):
    page = page - 1

    start = item_per_page * page if page > 0 else page
    stop = start + item_per_page

    return list(islice(items, start, stop))


@query.field("allIngredients")
def resolve_all_ingredients(*_):
    return INGREDIENTS


@query.field("allProducts")
def resolve_all_products(*_):

    products_with_ingredients = [deepcopy(product) for product in PRODUCTS]

    # for product in products_with_ingredients:
    #    for ingredient_recipe in product["ingredients"]:
    #        for ingredient in INGREDIENTS:
    #            if ingredient["id"] == ingredient_recipe["ingredient"]:
    #                ingredient_recipe["ingredient"] = ingredient

    return products_with_ingredients


@query.field("products")
def resolve_products(*_, input=None):

    filtered_products = [product for product in PRODUCTS]

    if input is None:
        return filtered_products

    filtered_products = [
        product
        for product in filtered_products
        if product["available"] is input["available"]
    ]

    if input.get("minPrice") is not None:
        filtered_products = [
            product
            for product in filtered_products
            if product["price"] >= input["minPrice"]
        ]

    if input.get("maxPrice") is not None:
        filtered_products = [
            product
            for product in filtered_products
            if product["price"] <= input["maxPrice"]
        ]

    filtered_products.sort(
        key=lambda product: product.get(input["sortBy"], 0),
        reverse=input["sort"] == "DESCENDING",
    )

    return get_page(filtered_products, input["resultsPerPage"], input["page"])
