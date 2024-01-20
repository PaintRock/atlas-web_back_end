#!/usr/bin/env python3
""" Module of Session Authentication
"""
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """create a CLASS ATTRIBUTE initialize by
    an empty dictionary"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create an instance method that creates a
        Session ID for a user_ID (HUH?)"""
        if user_id is None or not isinstance (user_id, str):
            return None
