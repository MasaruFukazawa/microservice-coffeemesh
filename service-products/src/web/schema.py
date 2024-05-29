# -*- coding: utf-8 -*-

from pathlib import Path

from ariadne import make_executable_schema

from web.mutations import mutation
from web.queries import query
from web.types import datetime_scalar, product_interface, product_type

schema = make_executable_schema(
    (Path(__file__).parent / "products.graphql").read_text(),
    [query, product_type, mutation, datetime_scalar, product_interface],
)
