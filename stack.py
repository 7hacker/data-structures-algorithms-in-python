'''
Get a stack by using this Lib
'''
import sys

class Stack:
	def __init__(self):
		self.stack = list()
		return

	def push(self, item):
		self.stack.append(item)
		return

	def pop(self):
		return self.stack.pop(-1)

	def peek(self):
		return self.stack[-1]

	def size(self):
		return len(self.stack)

	def show(self):
		for item in self.stack:
			sys.stdout.write(str(item) + "->")
		sys.stdout.write("TOP\n")

