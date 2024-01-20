#!/usr/bin/env python3
"""
Route module for the API
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """empty class inheriting"""
    pass
def extract_base64_authorization_header(self, authorization_header: str) -> str:
    not isinstance authorization_header is None or
    if (authorization_header, str):
        return None
    if not authorization_header.startswith("Basic "):
        return None
    return authorization_header[len("Basic "):]
