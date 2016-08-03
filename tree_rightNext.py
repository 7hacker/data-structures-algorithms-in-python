'''
Given a Full binary tree Populate the nextRight pointers in each node: http://www.geeksforgeeks.org/connect-nodes-at-same-level/
'''
import sys

class Node:
	def __init__(self, val=None, l=None, r=None):
		self.v = val
		self.l = l
		self.r = r
		self.nextRight = None


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

	def phase1(self, n):
		q = list()
		q.append(n)
		while len(q):
			node = q.pop(0)
			leftChild = node.l
			rightChild = node.r
			if leftChild and rightChild:
				leftChild.nextRight = rightChild
				q.append(leftChild)
				q.append(rightChild)

	def phase2(self, n):
		if not n:
			return
		else:
			if n.nextRight:
				if n.r:
					n.r.nextRight = n.nextRight.l
			self.phase2(n.l)
			self.phase2(n.r)


	def showRightNext(self, n):
		if not n:
			return
		else:
			if n.nextRight:
				print("My value is : " + str(n.v))
				print("My nextRight value is: " + str(n.nextRight.v))
			self.showRightNext(n.l)
			self.showRightNext(n.r)


	def fillRightNext(self):
		self.phase1(self.root)
		self.phase2(self.root)
		self.showRightNext(self.root)

t = BinaryTree()
root = t.addRoot(6)
(l1,r1) = t.addChildren(root, 3, 4)
(l2, r2) = t.addChildren(l1, 7, 5)
(l3, r3) = t.addChildren(r1, 8, 9)
t.printTree()
t.fillRightNext()

