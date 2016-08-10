'''
A 4 leve skip list in python
'''
from cmd import Cmd
import random
import sys


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class SkipList:
	def __init__(self):
		self.levels = [None] * 4

	def get_coinToss(self):
		return random.randint(0,1)

	def _insert_at_Level(self, level, node):
		node.next = None
		print("Inserting " + str(node.data) + " at level : " + str(level))
		if not self.levels[level]:
			self.levels[level] = node
		else:
			trav = self.levels[level]
			if trav.data > node.data:
				node.next = trav
				self.levels[level] = node
				return
			else:
				while trav.next:
					if trav.next.data > node.data:
						node.next = trav.next
						trav.next = node
						break
					trav = trav.next
				if not node.next:
					trav.next = node

	def insert(self, data):
		newNode = Node(data)
		self._insert_at_Level(0, newNode)
		tryMore = True
		i = 1
		while tryMore and i <= 4:
			t = self.get_coinToss()
			if t == 0:
				tryMore = False
			else:
				self._insert_at_Level(i, newNode)
				i = i + 1
		return


	def seeSkipList(self):
		#for each level print out the ordering
		for l in range(4):
			print("Level :" + str(l))
			trav = self.levels[l]
			if trav:
				while trav.next:
					print(trav.data)
					trav = trav.next
				print(trav.data)
		return


class MyPrompt(Cmd):
	def do_quit(self, args):
		"""Quits the program."""
		print "Quitting."
		raise SystemExit

	def do_insert(self,args):
		"""Insert an integer into a skiplist"""
		if len(args) != 0:
			for w in args.split():
				sl.insert(int(w.rstrip()))

	def do_seeSkipList(self, args):
		"""See your Skip List"""
		sl.seeSkipList()


sl = SkipList()
if __name__ == '__main__':
	prompt = MyPrompt()
	prompt.prompt = '> '
	prompt.cmdloop('Starting SkipList Shell...')
