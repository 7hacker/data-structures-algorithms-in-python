#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache
#
# Hard (16.56%)
# Total Accepted:    115573
# Total Submissions: 694929
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
# 
# 
# 
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
# 
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# 
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# 
# 
#
class LRUCache(object):
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None

    class Dlist:
        def __init__(self, capacity):
            self.size = 0
            self.capacity = capacity
            self.head = None
            self.tail = None

        def _printlist(self):
            import sys
            t = self.head
            while t:
                sys.stdout.write("key:" + str(t.key) + ",value:" + str(t.value) + " -> ")
                t = t.next


        def _deleteold(self):
            #self._printlist()
            if self.tail:
                print "DELETEING : " + str(self.tail.key)
                old = self.tail
                self.tail = old.prev
                if self.tail:
                    self.tail.next = None
                old = None

        def _insertashead(self, n):
            n.next = self.head
            self.head.prev = n
            self.head = n


        def addnew(self, newn):
            keytodelete = None
            if self.size < self.capacity:
                if not self.head:
                    self.head  = newn
                    self.tail  = newn
                else:
                    self._insertashead(newn)
                self.size = self.size + 1
            else:
                keytodelete = self.tail.key
                self._deleteold()
                self._insertashead(newn)
                return keytodelete

        def makerecent(self, rn):
            if rn.prev:
                rn.prev.next = rn.next
            if rn.next:
                rn.next.prev = rn.prev
            rn.prev = None
            rn.next = None
            self._insertashead(rn)



    def __init__(self, capacity):
        """
        :type capacity: int
        """
        print "INIT : Size=" + str(capacity)
        self.dl = self.Dlist(capacity)
        self.map = {}
        

    def get(self, key):
        """
        :type key: int
        :rtype: int

        """
        print "START GET : " + str(key)
        if key in self.map:
            rn = self.map[key]
            self.dl.makerecent(rn)
            print "END GET : " + str(rn.value)
            return rn.value
        else:
            print "END GET : -1"
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        print "START PUT: " + str(key) + "," + str(value)
        if key in self.map:
            _ = self.get(key)
        else:
            newn = self.Node(key, value)
            oldkey = self.dl.addnew(newn)
            if oldkey:
                del self.map[oldkey]
            self.map[key] = newn
        return

    def statlist(self):
        self.dl._printlist()
        print "\n"

    def statmap(self):
        print self.map

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
lc = LRUCache(2)
lc.put(1,1)
lc.put(2,2)
lc.statlist()
print lc.get(1)
lc.statlist()
lc.put(3,3)
lc.statlist()
lc.get(2)
lc.put(4,4)



