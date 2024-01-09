#!/usr/bin/env python3
"""FIFOCache"""

from BaseCaching import BaseCaching
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # FIFO: Remove the first item added to the cache
            discarded_key, _ = next(iter(self.cache_data.items()))
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}\n")

        # Add or update the item in the cache
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
