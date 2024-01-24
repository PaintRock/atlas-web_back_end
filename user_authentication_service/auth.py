#!/usr/bin/env python3
"""Authentication Module"""
import bcrypt
from db import DB
from user import User
from bcrypt import hashpw, gensalt, checkpw
from sqlalchemy.orm.exc import NoResultFound
import uuid


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
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(
                email=email,
                hashed_password=hashed_password
            )
            return new_user

        else:
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """Checks validity of password"""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                password.encode('utf-8'), user.hashed_password
                )
        except NoResultFound:
            return False

    def _generate_uuid(self) -> str:
        """Generate a new UUID"""
        return str(uuid.uuid4())

    def __init__(self):
        """Init code"""
        self._db = DB()
