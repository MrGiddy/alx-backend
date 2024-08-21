#!/usr/bin/env python3
"""Implements MRU cache replacement policy"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Represents an MRU caching object/system"""
    def __init__(self):
        """initialize an MRUCache"""
        super().__init__()

    def get(self, key):
        """retrieves an item value bounded to key"""
        if key is None:
            return
        # Move the accessed key:value pair to the end
        if key in self.cache_data:
            self.cache_data[key] = self.cache_data.pop(key)
        return self.cache_data.get(key, None)

    def put(self, key, item):
        """
        binds item value to key in cache,
        and removes the most recently used key:item pair
        from the cache if the cache size is exceeded
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_key = list(self.cache_data.keys())[-2]
            self.cache_data.pop(mru_key)
            print(f'DISCARD: {mru_key}')
