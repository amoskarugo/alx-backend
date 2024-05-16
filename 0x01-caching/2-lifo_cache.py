#!/usr/bin/env python3

"""module containing a class
to implement lifo caching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """implement fifo caching operations"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) < BaseCaching.MAX_ITEMS:
            self.cache_data[key] = item
        else:
            item_key = list(self.cache_data.items())[-1][0]
            self.cache_data.pop(item_key)
            print(f'DISCARD: {item_key}')
            self.cache_data[key] = item

    def get(self, key):
        """get item by key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data[key]
