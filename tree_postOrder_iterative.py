'''
Given a binary tree, print the post-order traversal without using recursion
'''
import sys
from stack import Stack


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

	def _printPostOrderRecursive(self, n):
		if n:
			self._printPostOrderRecursive(n.l)
			self._printPostOrderRecursive(n.r)
			print(n.v)


	def printPostOrderRecursive(self):
		return self._printPostOrderRecursive(self.root)


	def printPostOrderIterative(self):
		inS = Stack()
		outS= Stack()
		inS.push(self.root)
		while inS.size():
			topNode = inS.pop()
			if topNode.l:
				inS.push(topNode.l)
			if topNode.r:
				inS.push(topNode.r)
			outS.push(topNode)

		while outS.size():
			print(outS.pop().v)

		return


t = BinaryTree()
root = t.addRoot(3)
(l1,r1) = t.addChildren(root, 2, 5)
(l2, r2) = t.addChildren(l1, 1, 4)
(l3, r3) = t.addChildren(r1, 7, 8)
t.printTree()
print("Post order Recursive:")
t.printPostOrderRecursive()
print("Post order Iterative:")
t.printPostOrderIterative()


