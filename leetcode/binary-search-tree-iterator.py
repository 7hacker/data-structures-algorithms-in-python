#
# [173] Binary Search Tree Iterator
#
# https://leetcode.com/problems/binary-search-tree-iterator
#
# Medium (39.81%)
# Total Accepted:    81824
# Total Submissions: 204811
# Testcase Example:  '[]'
#
# Implement an iterator over a binary search tree (BST). Your iterator will be
# initialized with the root node of a BST.
# 
# Calling next() will return the next smallest number in the BST.
# 
# Note: next() and hasNext() should run in average O(1) time and uses O(h)
# memory, where h is the height of the tree. 
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.st = []
        self.pushAll(root)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.st) > 0
        

    def next(self):
        """
        :rtype: int
        """
        p = self.st.pop(-1)
        rval = p.val
        self.pushAll(p.right)
        return rval

    def pushAll(self, r):
        while r:
            self.st.append(r)
            r = r.left
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
