# -*- coding: utf-8 -*-

from pathlib import Path

import jwt
from cryptography.x509 import load_pem_x509_certificate

public_key_text = (
    Path(__file__).parent.parent.parent / "secret_key/public_key.pem"
).read_text()

public_key = load_pem_x509_certificate(public_key_text.encode()).public_key()


def decode_and_validate_token(access_token):
    """
    アクセストークンを検証。トークンが有効な場合はトークンペイロードを返す
    """
    return jwt.decode(
        access_token,
        key=public_key,
        algorithms=["RS256"],
        audience=["http://127.0.0.1:8000/orders"],
    )
