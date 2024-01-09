#!/usr/bin/env python3
"""FIFO Caching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class created and the init
    """

    def __init__(self):
        """Calling parent init
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add or update the item in the cache"""
        if key is None or item is None:
            return

        """Update the order if the key already exists"""
        if key in self.cache_data:
            """Update the value for an existing key"""
            self.cache_data[key] = item
            """Remove the existing key from the queue"""
            self.queue.remove(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                """Remove the oldest key from the queue"""
                discarded_key = self.queue.pop(0)
                print(f"DISCARD: {discarded_key}")
                """Discard the oldest key-value pair"""
                del self.cache_data[discarded_key]

        """Add or update the item in the cache"""
        self.cache_data[key] = item
        """Append the new key to the end of the queue"""
        self.queue.append(key)

    def get(self, key):
        """If key is none return none """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
