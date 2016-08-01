'''
Given a binary tree is it a Binary search tree?
'''
import sys

class Node:
	def __init__(self, val=None, l=None, r=None):
		self.v = val
		self.l = l
		self.r = r


class BinaryTree:
	def __init__(self):
		self.root = None
		self.size = 0

	def addRoot(self, val):
		if self.root == None:
			self.root = Node(val)
		return self.root

	def addChildren(self,n, leftV, rightV):
		leftNode = Node(leftV)
		rightNode = Node(rightV)
		n.l = leftNode
		n.r = rightNode
		return (leftNode, rightNode)

	def printTree(self):
		q = [self.root]
		while len(q) != 0:
			elem = q.pop(0)
			if elem is not None:
				print(elem.v)
				q.append(elem.l)
				q.append(elem.r)

	def _isBST(self, t, mx, mn):
		if t is None:
			return True
		if t.v >= mn and t.v <= mx :
			return (self._isBST(t.l, t.v, mn) and self._isBST(t.r, mx, t.v))
		else:
			return False

	def isBST(self):
		treeMax = sys.maxint
		treeMin = - sys.maxint -1 
		return (self._isBST(self.root.l, self.root.v, treeMin) and self._isBST(self.root.r, treeMax, self.root.v))

t = BinaryTree()
root = t.addRoot(3)
(l1,r1) = t.addChildren(root, 2, 5)
(l2, r2) = t.addChildren(l1, 1, 4)
t.printTree()
print(t.isBST())

