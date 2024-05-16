#!/usr/bin/env python3
"""
module containing a class for performing
cache operations.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    a class that implements some cache operations
    """
    def __init__(self):
        """method initialize the instance"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """get item by key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data[key]
