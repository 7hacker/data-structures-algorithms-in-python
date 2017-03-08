import sys

class Node:
	def __init__(self, d=None):
		self.data = d
		self.next = None

def append(head, node):
	node.next = None
	if not head:
		head = node
	else:
		t = head
		while t.next != None:
			t = t.next
		t.next = node
	return

def printList(head):
	t = head
	while t.next != None:
		sys.stdout.write(str(t.data) + " ")
		t = t.next
	sys.stdout.write(str(t.data) + "\n")
	return

def addMarker(h):
	back = Node("#")
	#add marker to back
	t = h
	while t.next != None:
		t = t.next
	t.next = back
	return h

def removeMarker(h):
	t = h
	while t.next and t.next.data != '#':
		t = t.next
	t.next = None
	return h


def merge(h1, h2):
	h1 = addMarker(h1)
	h2 = addMarker(h2)
	mh = Node()
	t1 = h1
	t2 = h2
	while t1.data != "#" or t2.data != "#":
		if t1.data < t2.data:
			moveNode = t1
			t1 = t1.next
			append(mh, moveNode)
		else:
			moveNode = t2
			t2 = t2.next
			append(mh, moveNode)
	
	if t1.data == "#":
		while(t2.data != "#"):
			moveNode = t2
			t2 = t2.next
			append(mh, moveNode)
	else:
		while(t1.data != "#"):
			moveNode = t1
			t1 = t1.next
			append(mh, moveNode)
	h1 = removeMarker(h1)
	h2 = removeMarker(h2)
	mh = mh.next
	return mh

def getLength(a):
	if not a:
		return 0
	t = a
	count = 0
	while t != None:
		t = t.next
		count = count + 1
	return count

def split(h):
	fast = h
	slow = h
	if getLength(h) == 2:
		r = h.next
		h.next = None
		return(h, r)
	else:
		fast = slow.next.next
		while fast.next != None:
			fast = fast.next
			if fast.next != None:
				fast = fast.next
			slow = slow.next
		r = slow.next
		slow.next = None
		return (h, r)


def mergeSort(a):
	if getLength(a) == 1:
		return a

	(l, r) = split(a)
	mergeSort(l)
	mergeSort(r)
	m =  merge(l,r)
	#printList(l)
	#printList(r)
	printList(m)
	return m






#make two lists
hOne = Node(100)
append(hOne, Node(23))
append(hOne, Node(3))
append(hOne, Node(41))
append(hOne, Node(5))
append(hOne, Node(99))
t = mergeSort(hOne)
#printList(t)
#merge them
#hThree = merge(hOne, hTwo)
#printList(hThree)
