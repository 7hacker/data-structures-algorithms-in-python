#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists
#
# Hard (26.38%)
# Total Accepted:    133938
# Total Submissions: 507650
# Testcase Example:  '[]'
#
# 
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq
class Heap:
    def __init__(self):
        self._h = []
        return

    def push(self, priority, item):
        heapq.heappush(self._h, (priority, item))
        return

    def pop(self):
        item = heapq.heappop(self._h)[1]
        return item

    def __len__(self):
        return len(self._h)

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = len(lists)
        h = Heap()
        mergedH = None
        mergedT = None
        
        for i in xrange(k):
            head = lists[i]
            if head:
                h.push(head.val, head)

        while len(h):
            p = h.pop()
            if p.next:
                h.push(p.next.val, p.next)
            p.next  = None
            if not mergedH:
                mergedH = mergedT = p
            else:
                mergedT.next = p
                mergedT = mergedT.next
        return mergedH


        
