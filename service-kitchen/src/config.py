# -*- coding: utf-8 -*-


class BaseConfig:
    API_TITLE = "Kitchen API"
    API_VERSION = "V1"

    OPENAPI_VERSION = "3.1.0"
    OPENAPI_JSON_PATH = "openapi/kitchen.json"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_REDOC_PATH = "/redoc"
    OPENAPI_REDOC_URL = (
        "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"
    )
    OPENAPI_SWAGGER_UI_PATH = "/docs/kitchen"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
