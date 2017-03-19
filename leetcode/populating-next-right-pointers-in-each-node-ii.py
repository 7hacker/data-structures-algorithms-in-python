#
# [117] Populating Next Right Pointers in Each Node II
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii
#
# Medium (33.60%)
# Total Accepted:    88691
# Total Submissions: 263974
# Testcase Example:  '{}'
#
# Follow up for problem "Populating Next Right Pointers in Each Node".
# What if the given tree could be any binary tree? Would your previous solution
# still work?
# 
# Note:
# You may only use constant extra space.
# 
# 
# For example,
# Given the following binary tree,
# 
# 1
# /  \
# 2    3
# / \    \
# 4   5    7
# 
# 
# 
# After calling your function, the tree should look like:
# 
# 1 -> NULL
# /  \
# 2 -> 3 -> NULL
# / \    \
# 4-> 5 -> 7 -> NULL
# 
# 
#
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
    	if not root:
    		return
    	q = [(root, 0)]
    	while len(q):
    		node, level = q.pop(0)
    		if node.left:
    			q.append((node.left, level+1))
    		if node.right:
    			q.append((node.right, level+1))
    		if len(q) and level == q[0][1]:
    			node.next = q[0][0]