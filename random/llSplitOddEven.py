'''
given a linked list with integers rearrange it such that even numbers are in the first half and odd numbers in the second half
'''
from linkedlist import Node,LinkedList


def splitEvenOdd(h):
	if not len(h):
		return
	eh = LinkedList()
	oh = LinkedList()
	t = h.getHead()
	while t != None:
		m = t
		t = t.next
		if m.data % 2 == 0:
			eh.append(m)
		else:
			oh.append(m)
	eh.tail.next = oh.head
	eh.tail = oh.tail
	return eh



iL = LinkedList()
iL.append(Node(4))
iL.append(Node(8))
iL.append(Node(10))
iL.append(Node(13))
iL.append(Node(7))
iL.append(Node(1))
iL.append(Node(5))
iL.append(Node(12))
iL.append(Node(19))
iL.append(Node(22))
iL.printList()
iL = splitEvenOdd(iL)
iL.printList()