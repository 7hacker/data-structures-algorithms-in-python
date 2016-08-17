'''
Clone a binary tree and return the root of the cloned tree
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


def cloneTree(original):
    if not original:
        return None
    else:
        clonedNode = Node(original.v)
        if original.l:
            clonedNode.l = cloneTree(original.l)
        if original.r:
            clonedNode.r = cloneTree(original.r)
        return clonedNode

def printFromRoot(n):
    q = [n]
    while len(q):
        elem = q.pop(0)
        if elem:
            print(elem.v)
            q.append(elem.l)
            q.append(elem.r)


t = BinaryTree()
root = t.addRoot(6)
(l1,r1) = t.addChildren(root, 3, 4)
(l2, r2) = t.addChildren(l1, 7, 5)
(l3, r3) = t.addChildren(r1, 8, 9)
t.printTree()
print("----")
clonedTree = cloneTree(t.root)
printFromRoot(clonedTree)


