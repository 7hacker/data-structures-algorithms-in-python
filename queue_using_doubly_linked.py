class Node:
	def __init__(self):
		self.data = None
		self.next = None
		self.prev = None
		return

class Queue:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0
		return

	def enqueue(self,item):
		newNode = Node()
		newNode.data = item

		#Head and Tail are the same in Queue of size=1
		if self.size == 0:
			self.head  = self.tail = newNode
			self.size = 1
			return

		#Head and Tail separate when size=2
		if self.size == 1:
			self.head = newNode
			self.head.next = self.tail
			self.tail.prev = self.head
			self.size = 2
			return

		self.head.prev = newNode
		newNode.next = self.head
		self.head = newNode
		self.size = self.size + 1
		return

	def dequeue(self):
		if self.size == 0:
			return None
		if self.size == 1:
			popped = self.head.data
			self.head = self.tail = None
			self.size = 0
			return popped
		
		popped = self.tail.data
		self.tail = self.tail.prev
		self.tail.next = None
		self.size = self.size - 1
		return popped

	def get_size(self):
		return self.size

	def print_queue(self):
		if self.size == 0:
			print("Empty Queue")
			return

		traverse = self.head
		while traverse.next != None:
			print(traverse.data)
			traverse = traverse.next
		print(traverse.data)
		return

myQueue = Queue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)
#print(myQueue.get_size())
myQueue.print_queue()

myQueue.dequeue()
print("Dequeue: ")
print("Size of queue: " + str(myQueue.get_size()))
myQueue.print_queue()

myQueue.dequeue()
print("Dequeue: ")
print("Size of queue: " + str(myQueue.get_size()))
myQueue.print_queue()
myQueue.dequeue()
print("Dequeue: ")
print("Size of queue: " + str(myQueue.get_size()))
myQueue.print_queue()
myQueue.dequeue()
print("Dequeue: ")
print("Size of queue: " + str(myQueue.get_size()))
myQueue.print_queue()



