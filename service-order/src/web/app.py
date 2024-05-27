# -*- coding: utf-8 -*-

from pathlib import Path

import yaml
from fastapi import FastAPI

app = FastAPI(debug=True, openapi_url="/openapi/order.json", docs_url="/docs/orders")
oas_doc = yaml.safe_load(Path("/docs/oas.yaml").read_text())
app.openapi = lambda: oas_doc

from api import api
