#!/usr/bin/env python3
"""Implements a LIFO cache replacement policy"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Represents a LIFO caching object/system"""
    def __init__(self):
        """initialize a LIFOCache"""
        super().__init__()

    def get(self, key):
        """retrieves an item value bounded to key"""
        if key is None:
            return None
        return self.cache_data.get(key, None)

    def put(self, key, item):
        """
        binds item value to key in cache,
        and removes last key:item pair entered/updated in cache
        if the cache size is exceeded
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # pop and reinsert updated key:value pair
            # so that it can move to the end of the dict
            self.cache_data[key] = self.cache_data.pop(key)
        else:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-2]
            del self.cache_data[last_key]
            print(f'DISCARD: {last_key}')
