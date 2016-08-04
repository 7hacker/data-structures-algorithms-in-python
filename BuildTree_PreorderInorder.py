'''
Given the inorder and preorder traversal's of a tree in an array, build a tree . : http://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/
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


def printFromRoot(n):
	q = [n]
	while len(q):
		elem = q.pop(0)
		if elem:
			print(elem.v)
			q.append(elem.l)
			q.append(elem.r)

def makeTree(inL, preL):
	if not preL:
		return
	if len(preL) == 1:
		root = Node(preL[0])
		return root
	else:
		root = Node(preL[0])
		i = 0
		while inL[i] != preL[0]:
			i = i + 1
		preListLeft = preL[1:len(preL)/2 + 1]
		preListRight = preL[len(preL)/2 + 1: len(preL)]
		inListLeft = inL[0: i]
		inListRight = inL[i+1: len(inL)]
		root.l = makeTree(inListLeft, preListLeft)
		root.r = makeTree(inListRight, preListRight)
		return root


ino = [8, 1, 20, 2, 9, 7, 5]
preo = [2, 1, 8, 20, 7, 9, 5]
r = makeTree(ino, preo)
printFromRoot(r)


