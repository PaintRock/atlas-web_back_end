#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """this is the class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for the given path."""
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        """Ensure slash tolerance by handling paths with and
        without trailing slashes"""
        normalized_path = path.rstrip('/') + '/'

        return normalized_path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """Get the authorization header from the request."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current user from the request."""
        return None
