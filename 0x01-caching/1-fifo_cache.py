#!/usr/bin/env python3
"""Implements a FIFO cache replacement policy"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Represents a FIFO caching object/system"""
    def __init__(self):
        """initialize a FIFOCache"""
        super().__init__()

    def get(self, key):
        """retrieves an item value bounded to key"""
        if key is None:
            return None
        return self.cache_data.get(key, None)

    def put(self, key, item):
        """
        binds item value to key in cache
        and removes first item entered in cache if cache size is exceeded
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print(f'DISCARD: {first_key}')
