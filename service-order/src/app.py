# -*- coding: utf-8 -*-

from fastapi import FastAPI

app = FastAPI(debug=True)

from api import api
