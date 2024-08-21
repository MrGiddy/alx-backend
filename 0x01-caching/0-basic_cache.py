#!/usr/bin/env python3
"""Defines a simple caching system class"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Represents an object that uses a dictionary for caching"""
    def get(self, key):
        """get an item by key from the cache"""
        if key is None:
            return None
        if key not in self.cache_data:
            return None
        return self.cache_data.get(key)

    def put(self, key, item):
        """add an item bounded to key in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
