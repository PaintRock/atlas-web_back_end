#!/usr/bin/env python3
"""Authentication Module"""
from db import DB
from user import User
from bcrypt import hashpw, gensalt, checkpw


def _hash_password(password: str) -> bytes:
    """Takes a pasword and returns bytes"""
    return hashpw(password.encode('utf-8'), gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """
    def register_user(self, email: str, password: str) -> User:
        """Registers and returns new user if email not listed"""
        try:
            existing_user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # If no user found, proceed with registration
            hashed_password = self._hash_password(password)
            new_user = self._db.add_user
            (email=email, hashed_password=hashed_password)
            return new_user

    def __init__(self):
        self._db = DB()
