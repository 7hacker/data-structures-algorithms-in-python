'''
Given a binary tree, return the number of Unival trees . Example is here: https://crazycoderzz.wordpress.com/count-the-number-of-unival-subtrees-in-a-binary-tree/
'''
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




t = BinaryTree()
root = t.addRoot(5)
(l1,r1) = t.addChildren(root, 5, 5)
(l2, r2) = t.addChildren(l1, 5, 5)
(l3, r3) = t.addChildren(r1, None, 5)
t.printTree()



