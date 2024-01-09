#!/usr/bin/env python3
"""Base caching"""

from BaseCaching import BaseCaching
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # LIFO: Remove the last item added to the cache
            last_key = list(self.cache_data.keys())[-1]
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}\n")

        # Add or update the item in the cache
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
