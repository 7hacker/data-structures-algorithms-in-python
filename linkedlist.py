'''
Linked lists in Python using a Node abstraction
'''
class Node():
	def __init__(self):
		self.data = None
		self.next = None

class LinkedList():
	def __init__(self):
		self.size = 0
		self.head = Node()
		return

	def add_element(self,element):
		newNode = Node()
		newNode.data = element

		if self.size == 0:
			#print("Added first element to linkedlist " + str(element))
			self.head.next = newNode
			self.size = self.size + 1
			return
		else:
			#print("Added element to linkedlist " + str(element))
			traverse = self.head
			while traverse.next != None:
				traverse=traverse.next
			traverse.next = newNode
			self.size = self.size + 1
		return

	def add_element_to_front(self,element):
		newNode = Node()
		newNode.data = element

		newNode.next = self.head.next
		self.head.next = newNode
		self.size = self.size + 1
		return

	def remove_element(self):
		traverse =  self.head
		previous = self.head

		if self.size == 0:
			return None
		if self.size == 1:
			popped = self.head.next.data
			self.head.next = None
			self.size = 0
			return popped

		traverse = traverse.next.next
		previous = previous.next

		while traverse.next != None:
			previous = previous.next
			traverse = traverse.next
		
		popped = traverse.data
		previous.next = None
		self.size = self.size -1
		return popped

	def remove_element_from_front(self):
		return

	def get_size(self):
		return self.size

	def print_list(self):
		traverse =  self.head
		if self.size == 0:
			print("Empty List")
			return
		#Head is an empty node so move one position	
		traverse=traverse.next
		while traverse.next != None:
			print(traverse.data)
			traverse = traverse.next
		print(traverse.data)
		return

myList = LinkedList()
#myList.print_list()
myList.add_element_to_front(1)
myList.add_element_to_front(2)
myList.add_element_to_front(3)
myList.add_element_to_front(4)
#print(myList.get_size())
#myList.print_list()
print("Full list")
myList.print_list()

myList.remove_element()
print("First remove")
myList.print_list()

myList.remove_element()
print("Second remove")
myList.print_list()

myList.remove_element()
print("Third remove")
myList.print_list()

myList.remove_element()
print("Fourth remove")
myList.print_list()
#print(myList.remove_element())
#print(myList.remove_element())
#print(myList.remove_element())
#print(myList.remove_element())

