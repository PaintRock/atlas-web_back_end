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

    def create_session(self, user_id=None):
        """Creation session database"""
        session_id = super().create_session(user_id)

        if session_id is None:
            return None

        kwargs = {'user_id': user_id, 'session_id': session_id}
        user_session = UserSession(**kwargs)
        user_session.save()
        UserSession.save_to_file()

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns User ID based on a Session's ID
        Args:
            session_id (str, optional): The session ID. Defaults to None.
        Returns:
            str: The User ID.
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def destroy_session(self, request=None):
        """Remove Session from Database"""
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)

        if not user_id:
            return False

        user_session = UserSession.search({
            'session_id': session_id
        })

        if not user_session:
            return False

        user_session = user_session[0]

        try:
            user_session.remove()
            UserSession.save_to_file()
        except Exception:
            return False

        return True
