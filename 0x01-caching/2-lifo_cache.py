#!/usr/bin/env python3
"""Basic dictionary"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Cache Class"""
    def __init__(self):
        """Iniitialization"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Puts data into cache using the FIFO system"""
        if (key is None or item is None):
            pass
        else:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                if self.cache_data.get(key) is None:
                    del_item = self.cache_data.popitem()
                    print("DISCARD: {}".format(del_item[0]))
                else:
                    del self.cache_data[key]
            self.cache_data[key] = item

    def get(self, key):
        """Gets from the cache"""
        return self.cache_data.get(key)
