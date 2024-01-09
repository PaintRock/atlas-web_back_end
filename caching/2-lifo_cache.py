#!/usr/bin/env python3
"""Lifo caching"""

from BaseCaching import BaseCaching
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """created class LIFO"""
    def __init__(self):
        """Calling parent"""
        super().__init__()

    def put(self, key, item):
        """Set the key"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            """ LIFO: Remove the last item added to the cache"""
            last_key = list(self.cache_data.keys())[-1]
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}\n")

        """ Add or update the item in the cache """
        .6355
        self.cache_data[key] = item

    def get(self, key):
        """ return the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
