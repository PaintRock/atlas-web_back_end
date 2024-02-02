#!/usr/bin/env python3
"""This is a Redis module """
import redis
import uuid
from typing import Union


class Cache:
    """Create a class Cache"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis = redis.flusdb()
        
    def store(data: Union[str, bytes, int, float])->str:
        key = str(uuid.uudi4())
        self._redis.set(key, data)
        return key
