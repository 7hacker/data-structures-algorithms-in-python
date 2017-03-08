'''
a prototype LRU-style KV store
'''
import collections

class LRUStore:
    def __init__(self, size):
        self.size = size
        self.cache = collections.OrderedDict()

    def get(self, key):
        #remove an item and reinsert it to update its timestamp
        try:
            v = self.cache.pop(key)
            self.cache[key] = v
            return v
        except KeyError:
            return -1

    def set(self, key, value):
        #if the item does not exist add it in
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.size:
                #the evict simply removes the FIFO order item in the ordered dict. only 1 item is removed, because why remove more?
                self.cache.popitem(last=False)
        self.cache[key] = value



