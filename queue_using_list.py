'''
A Queue using Python Lists
'''
class Queue:
    def __init__(self):
        self.items = list()
        return

    def enqueue(self, item):
        self.items.insert(0,item)
        return

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def printq(self):
        print(self.items)
        return

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.printq()
print(q.dequeue())
print(q.dequeue())
q.printq()