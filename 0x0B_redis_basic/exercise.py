#!/usr/bin/env python3
"""This is a Redis module """
import redis
from uuid import uuid4, UUID
from typing import Union
import uuid

class Cache:
    """Create a class Cache"""
    
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uudi4())
        self._redis.set(key, data)
        return key
