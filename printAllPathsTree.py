'''
Given a binary tree, print out all of its root-to-leaf paths one per line
'''
import sys

class Node:
	def __init__(self, val=None, l=None, r=None):
		self.v = val
		self.l = l
		self.r = r


	def isLeaf(self):
		if self.l is None:
			if self.r is None:
				return True
		return False


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



	def _printAllPaths(self, n, path):
		if n.isLeaf():
			print(path + " " + str(n.v))
			return
		else:
			if n.l:
				self._printAllPaths(n.l, path + " " + str(n.v))
			if n.r:
				self._printAllPaths(n.r, path + " " + str(n.v))


	def printAllPaths(self):
		self._printAllPaths(self.root, "")


t = BinaryTree()
root = t.addRoot(3)
(l1,r1) = t.addChildren(root, 2, 5)
(l2, r2) = t.addChildren(l1, 1, 4)
t.printTree()
t.printAllPaths()
