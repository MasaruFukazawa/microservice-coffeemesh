# -*- coding: utf-8 -*-

from fastapi import FastAPI
from pathlib import Path
import yaml

app = FastAPI(debug=True, openapi_url="/openapi/order.json", docs_url="/docs/orders")
oas_doc = yaml.safe_load(Path("/docs/oas.yaml").read_text())
app.openapi = lambda: oas_doc

from api import api
