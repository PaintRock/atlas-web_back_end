#!/usr/bin/env python3
"""This is a Redis module """
import redis
from uuid import uuid4, UUID
from typing import Union, Optional, Callable
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Count call decorator"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper for decorator functionality"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """Create a class Cache"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Convert data back to the desired format"""
        data = self._redis.get(key)
        if fn:
            data = fn(data)

        return data

    def get_str(self, key: str) -> str:
        """"parameterize Cache with..."""
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> str:
        """...the correct conversion function"""
        return self.get(key, fn=int)
