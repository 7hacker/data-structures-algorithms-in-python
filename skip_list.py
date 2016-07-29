import random
from cmd import Cmd


class SkipNode:
	def __init__(self, data=None, height=0):
		self.data = data
		self.next = [None] * height

class SkipList:
	def __init__(self):
		self.head = SkipNode()



class MyPrompt(Cmd):

	def do_add(self, args):
		"""Add an item to SkipListy. Has to be an integer!"""
		if len(args) == 0:
			print "Give me a number!"
		arglist = args.split()
		for a in arglist:
			if not int(a):
				print a + " is not an Integer! "
			else:
				sl.add_item(int(a))
				print "Added " + a

	def do_display(self, args):
		"""Show SkipListy"""
		sl.display()

	def do_hello(self, args):
		"""Says hello. If you provide a name, it will greet you with it."""
		if len(args) == 0:
		    name = 'stranger'
		else:
		    name = args
		print "Hello, %s" % name

	def do_quit(self, args):
		"""Quits the program."""
		print "Quitting."
		raise SystemExit


sl = SkipList()

if __name__ == '__main__':
	prompt = MyPrompt()
	prompt.prompt = '> '
	prompt.cmdloop('Welcome to SkipListy! Type help to get started..')