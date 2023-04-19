#!/usr/bin/env python3
"""Basic dictionary"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic Cache Class"""
    def __init__(self):
        """Iniitialization"""
        super().__init__()

    def put(self, key, item):
        """Puts data into cache"""
        if (key is None or item is None):
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Gets from the cache"""
        return self.cache_data.get(key)
