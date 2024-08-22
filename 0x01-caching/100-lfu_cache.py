#!/usr/bin/env python3
"""Implements LFU cache replacement policy"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Represents an LFU caching object/system"""
    def __init__(self):
        """initialize an LFUCache"""
        super().__init__()
        self.use_freq = {}
        self.newest_key = ''

    def get(self, key):
        """retrieves an item value bounded to key"""
        if key is None or key not in self.cache_data:
            return
        if key in self.cache_data:
            # Track how many times the key:value pair is accessed
            self.use_freq[key] += 1
            # Move the accessed key:value pair to the end
            self.cache_data[key] = self.cache_data.pop(key)
        return self.cache_data.get(key)

    def put(self, key, item):
        """
        - Binds item value to key in cache.
        - Removes the LFU key:item pair from the cache if
          the cache size is exceeded and if there isn't a tie.
        - Removes the LRU key:item pair if there is a tie
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.use_freq[key] += 1
        else:
            self.use_freq[key] = 1

        self.cache_data[key] = item
        self.newest_key = key

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # omit newest key from being prematurely evicted
            new_val = self.use_freq.pop(self.newest_key)

            # identify the least frequently used key(s)
            min_val = min(self.use_freq.values())
            min_val_keys = [
                k for k, v in self.use_freq.items() if v == min_val]

            # Re-dd newest key
            self.use_freq[self.newest_key] = new_val

            if len(min_val_keys) == 1:
                lfu_key = min_val_keys[0]
            else:
                # Tie Case: Find the LRU among the tieing LFU keys
                lfu_key = next(k for k in self.cache_data if k in min_val_keys)

            self.cache_data.pop(lfu_key)
            self.use_freq.pop(lfu_key)
            print(f'DISCARD: {lfu_key}')
