#!/usr/bin/env python3
"""Basic dictionary"""
import time
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRU Cache Class"""
    def __init__(self):
        """Iniitialization"""
        super().__init__()
        self.order = {}

    def put(self, key, item):
        """Puts data into cache using the FIFO system"""
        if (key is None or item is None):
            pass
        else:
            sorted_order = sorted(self.order.items(), key=lambda x: x[1])
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                sorted_order = sorted(self.order.items(), key=lambda x: x[1])
                if self.cache_data.get(key) is None:
                    del_key = sorted_order[-1][0]
                    del self.cache_data[del_key]
                    del self.order[del_key]
                    print("DISCARD: {}".format(del_key))
                else:
                    del self.cache_data[key]
            self.cache_data[key] = item
            self.order[key] = time.time()

    def get(self, key):
        """Gets from the cache"""
        if self.cache_data.get(key) is not None:
            self.order[key] = time.time()
        return self.cache_data.get(key)
