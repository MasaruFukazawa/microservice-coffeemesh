# -*- coding: utf-8 -*-

import datetime
from pathlib import Path

import jwt
from cryptography.hazmat.primitives import serialization


def generate_jwt():
    """
    jwt トークン生成
    """
    now = datetime.datetime.now(datetime.UTC)

    payload = {
        "iss": "https://auth.coffeemesh.io/",
        "sub": "ec7bbccf-ca89-4af3-82ac-b41e4831a962",
        "aud": "http://127.0.0.1:8000/orders",
        "iat": now.timestamp(),
        "exp": (now + datetime.timedelta(hours=24)).timestamp(),
        "scope": "openid",
    }

    private_key_text = (
        Path(__file__).parent / "../secret_key/private_key.pem"
    ).read_text()

    private_key = serialization.load_pem_private_key(
        private_key_text.encode(), password=None
    )

    return jwt.encode(payload=payload, key=private_key, algorithm="RS256")


if "__main__" == __name__:

    print(generate_jwt())
