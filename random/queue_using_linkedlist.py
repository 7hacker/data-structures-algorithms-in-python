'''
A Queue using Linked List style Nodes
'''
class Node:
    def __init__(self):
        self.data = None
        self.next = None
        return

class Queue:
    def __init__(self):
        self.head = None #enqueue at head
        self.tail = None #dequeue at tail
        self.size = 0
        return

    def enqueue(self,item):
        newNode = Node()
        newNode.data = item

        #when queue has 1 element, head and tail point to it
        if self.size == 0:
            self.head = self.tail = newNode
            self.size = 1
            #print("size=1, head = " + str(self.head.data) + " tail = " + str(self.tail.data))
            return

        #when queue has 2 elements, head and tail separate
        if self.size == 1:
            self.head = newNode
            newNode.next = self.tail
            self.size = 2
            #print("size=2, head = " + str(self.head.data) + " tail = " + str(self.tail.data))
            return

        newNode.next = self.head
        self.head = newNode
        self.size = self.size + 1
        #print("size= " + str(self.size) + " head = " + str(self.head.data) + " tail = " + str(self.tail.data) + " head->next = " + str(self.head.next.data))

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
        traverse = self.head
        while traverse.next != self.tail:
            traverse = traverse.next
        
        traverse.next = None
        self.tail = traverse
        self.size = self.size -1
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

myqueue = Queue()
myqueue.enqueue(1)
myqueue.enqueue(2)
myqueue.enqueue(3)
myqueue.enqueue(4)
myqueue.enqueue(5)
myqueue.enqueue(6)
print("Size of queue: " + str(myqueue.get_size()))
myqueue.print_queue()

myqueue.dequeue()
print("Dequeue: ")
print("Size of queue: " + str(myqueue.get_size()))
myqueue.print_queue()

myqueue.dequeue()
print("Dequeue: ")
print("Size of queue: " + str(myqueue.get_size()))
myqueue.print_queue()

myqueue.dequeue()
print("Dequeue: ")
print("Size of queue: " + str(myqueue.get_size()))
myqueue.print_queue()

myqueue.dequeue()
print("Dequeue: ")
print("Size of queue: " + str(myqueue.get_size()))
myqueue.print_queue()

myqueue.dequeue()
print("Dequeue: ")
print("Size of queue: " + str(myqueue.get_size()))
myqueue.print_queue()

myqueue.dequeue()
print("Dequeue: ")
print("Size of queue: " + str(myqueue.get_size()))
myqueue.print_queue()
