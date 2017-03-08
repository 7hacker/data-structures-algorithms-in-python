'''
Linked List library
'''
import sys

class Node:
    def __init__(self, d=None):
        self.data = d
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def append(self, node):
        node.next = None
        self.size = self.size + 1
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def printList(self):
        t = self.head
        while t != self.tail:
            sys.stdout.write(str(t.data) + " ")
            t = t.next
        sys.stdout.write(str(t.data) + "\n")

    def __len__(self):
        return self.size