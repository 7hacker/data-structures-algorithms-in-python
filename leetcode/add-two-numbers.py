#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers
#
# Medium (26.81%)
# Total Accepted:    255607
# Total Submissions: 953443
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
#class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        t1 = l1
        t2 = l2
        carry = False
        newHead = None
        newTail = None
        while t1 or t2:
            a = 0 if not t1 else t1.val
            b = 0 if not t2 else t2.val
            c = a + b #add the two vals at current loc
            c = c + 1 if carry else c + 0

            v = c % 10 #only get last digit

            newNode = ListNode(v) #make the new node
            
            if c > 9: #for next op
                carry = True
            else:
                carry = False
            
            if not newHead:
                newHead = newNode
                newTail = newNode
            else:
                newTail.next = newNode
                newTail = newNode
            t1 = t1.next if t1 else None
            t2 = t2.next if t2 else None
        
        if carry:
            newNode = ListNode(1)
            newTail.next = newNode
            newTail = newNode

        return newHead
'''
if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    result = Solution().addTwoNumbers(a, b)
    print "{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val)
'''