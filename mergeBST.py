'''
Merge 2 BST's to form a merged balanced BST
'''
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


def _getInfix(t, inl):
    if t:
        _getInfix(t.l, inl)
        inl.append(t.v)
        _getInfix(t.r, inl)


def getInfix(t):
    inl = []
    _getInfix(t.root, inl)
    return inl

def rec_merge(a, b, ai, bi, m, mi):
    if ai >= len(a):
        for x in range(bi, len(b)):
            m.append(b[x])
        return
    if bi >= len(b):
        for x in range(ai, len(a)):
            m.append(a[x])
        return
    if a[ai] <= b[bi]:
        m[mi] = a[ai]
        rec_merge(a, b, ai+1, bi, m, mi+1)
    else:
        m[mi] = b[bi]
        rec_merge(a, b, ai, bi+1, m, mi+1)
'''
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
'''

class BST:
    def __init__(self):
        self.root = Node()

def _sortedListToBST(a, start, end):
    if start > end:
        return None
    if start == end:
        t = BST()
        t.root.v = a[start]
        return t
    if start < end:
        t = BST()
        mid = (end+start)/2
        t.root.v = a[mid]
        t.root.l = _sortedListToBST(a, start, mid-1)
        t.root.r = _sortedListToBST(a, mid+1, end)
        return t

def sortedListToBST(a):
    return _sortedListToBST(a, 0, len(a)-1)

def printTreeBFS(t):
    q = []
    q.append(t)
    while len(q):
        popped = q.pop(0)
        if popped:
            print(popped.root.v)
            q.append(popped.root.l)
            q.append(popped.root.r)
        else:
            print(None)

t1 = BinaryTree()
root = t1.addRoot(50)
(l1,r1) = t1.addChildren(root, 20, 70)
(l2, r2) = t1.addChildren(l1, 10, 30)
(l3, r3) = t1.addChildren(r1, 60, 80)
infix_t1 = getInfix(t1)

t2 = BinaryTree()
root = t2.addRoot(55)
(l1,r1) = t2.addChildren(root, 18, 72)
(l2, r2) = t2.addChildren(l1, 9, 31)
(l3, r3) = t2.addChildren(r1, 65, 89)
infix_t2 = getInfix(t2)

#merge infix_t1 and infix_t2
mlen = len(infix_t1) + len(infix_t2) -1
merged = [None] * mlen

rec_merge(infix_t1, infix_t2, 0, 0, merged, 0)
print(merged)
mt = sortedListToBST(merged)
printTreeBFS(mt)


