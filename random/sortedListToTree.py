'''
take a sorted list, and build a binary search tree
'''

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = Node()


def _sortedListToBST(a, start, end):
    if start > end:
        return None
    if start == end:
        t = BST()
        t.root.data = a[start]
        return t
    if start < end:
        t = BST()
        mid = (end+start)/2
        t.root.data = a[mid]
        t.root.left = _sortedListToBST(a, start, mid-1)
        t.root.right = _sortedListToBST(a, mid+1, end)
        return t

def sortedListToBST(a):
    return _sortedListToBST(a, 0, len(a)-1)

def printTreeBFS(t):
    q = []
    q.append(t)
    while len(q):
        popped = q.pop(0)
        if popped:
            print(popped.root.data)
            q.append(popped.root.left)
            q.append(popped.root.right)
        else:
            print(None)


a = [4,  7, 5, 6, 9, 2, 3, 1, 8]
a.sort()
print(a)
t = sortedListToBST(a)
printTreeBFS(t)
