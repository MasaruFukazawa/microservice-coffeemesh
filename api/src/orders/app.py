# -*- coding: utf-8 -*-

from fastapi import FastAPI

app = FastAPI(debug=True)

from orders.api import api
