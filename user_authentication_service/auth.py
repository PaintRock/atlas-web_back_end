#!/usr/bin/env python3
"""Authentication Module"""
from db import DB
from user import User
from bcrypt import hashpw, gensalt, checkpw


def _hash_password(password: str) -> bytes:
    """Takes a pasword and returns bytes"""
    return hashpw(password.encode('utf-8'), gensalt())
