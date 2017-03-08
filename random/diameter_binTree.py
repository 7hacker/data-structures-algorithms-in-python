'''
The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two leaves in the tree.The max diameter need not pass through the root. see: http://www.geeksforgeeks.org/diameter-of-a-binary-tree/
'''

class Node:
    def __init__(self, v=None):
        self.val = v
        self.right = None
        self.left = None


def isLeaf(root):
    if not root.left and not root.right:
        return True
    else:
        return False

def Maxheight(root):
    if not root:
        return -1
    if isLeaf(root):
        return 0
    else:
        hl = 0
        hr = 0
        if root.left:
            hl = Maxheight(root.left)
        if root.right:
            hr = Maxheight(root.right)
        mh = max(hl, hr) + 1
        return mh

def treeDiameter(root):
    if not root:
        return 0
    else:
        myDiameter = Maxheight(root.left) + Maxheight(root.right) + 1
        myLeftChildDiameter = treeDiameter(root.left)
        myRightChildDiameter = treeDiameter(root.right)
        return max(myDiameter, myLeftChildDiameter, myRightChildDiameter)
    