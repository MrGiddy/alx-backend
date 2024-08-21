#!/usr/bin/env python3
"""Implements LRU cache replacement policy"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Represents an LRU caching object/system"""
    def __init__(self):
        """initialize an LRUCache"""
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
        and removes the least recently used key:item pair
        from the cache if the cache size is exceeded
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            self.cache_data.pop(first_key)
            print(f'DISCARD: {first_key}')
