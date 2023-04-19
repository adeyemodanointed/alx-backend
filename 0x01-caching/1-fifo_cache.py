#!/usr/bin/env python3
"""Basic dictionary"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cache Class"""
    def __init__(self):
        """Iniitialization"""
        super().__init__()

    def put(self, key, item):
        """Puts data into cache using the FIFO system"""
        if (key is None or item is None):
            pass
        else:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                del_key = next(iter(self.cache_data))
                if self.cache_data.get(key) is None:
                    del self.cache_data[del_key]
                    print("DISCARD: {}".format(del_key))
            self.cache_data[key] = item

    def get(self, key):
        """Gets from the cache"""
        return self.cache_data.get(key)
