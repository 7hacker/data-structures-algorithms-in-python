'''
Build an inverted index using a Trie
'''
from cmd import Cmd
import sys
import re


class Node:
	def __init__(self, name):
		self.entry = False #if True, a word can be formed following path from root to this node
		self.nodes = {} #dictionary of nodes that exist at this node, with key = letter
		self.name = name #letter at this node
		self.position = [] #position array for this node: contains position value for this word if the entry is True

class Trie:
	def __init__(self):
		self.root = Node("root")

	def add_word_withPosition(self, word, position):
		trav = self.root
		for i in range(len(word)):
			if word[i] in trav.nodes:
				trav = trav.nodes[word[i]]
			else:
				trav.nodes[word[i]] = Node(word[i])
				trav = trav.nodes[word[i]]
		trav.entry = True
		trav.position.append(position)

	def add_word(self, word):
		trav = self.root
		for i in range(len(word)):
			if word[i] in trav.nodes:
				trav = trav.nodes[word[i]]
			else:
				trav.nodes[word[i]] = Node(word[i])
				trav = trav.nodes[word[i]]
		trav.entry = True

	def _get_suggestion(self, n, ret, path):
		if not n:
			return
		if n.entry:
			ret.append(path)
		if n.nodes:
			for k in n.nodes:
				self._get_suggestion(n.nodes[k], ret, path + n.nodes[k].name)

	def get_suggestion(self, preword):
		trav = self.root
		ret = []
		path = ""
		for i in range(len(preword)):
			if preword[i] in trav.nodes:
				trav = trav.nodes[preword[i]]
				path = path + trav.name
		self._get_suggestion(trav, ret, path)
		return ret

	def get_position(self, word):
		trav = self.root
		for i in range(len(word)):
			if word[i] in trav.nodes:
				trav = trav.nodes[word[i]]
		if trav.entry:
			return trav.position

	def _print_trie(self, n, path):
		if not n:
			return
		else:
			if n.entry:
				print(path + n.name)
			if len(n.position):
				print(path + n.name + " found at : " + str(n.position))
			for k in n.nodes:
				tmp = path
				self._print_trie(n.nodes[k], tmp + n.name)

	def print_trie(self):
		for r in self.root.nodes:
			self._print_trie(self.root.nodes[r], "")
		return

def add_dictionaryWords(t, dictionarypath):
	fl = open(dictionarypath)
	lines = fl.readlines()
	for l in lines:
		t.add_word(l.rstrip())


def getWords(text):
    return re.sub(r'[^a-z0-9]',' ',text.lower()).split()

def add_book(t, bookpath):
	fl = open(bookpath)
	fr = fl.read()
	words=getWords(fr)
	for pos, word in enumerate(words):
		t.add_word_withPosition(word, pos)
	fl.close()

	#for w in fr.split():
	#	print(w)
	#	print(fl.tell())

class MyPrompt(Cmd):
	def do_quit(self, args):
		"""Quits the program."""
		print "Quitting."
		raise SystemExit

	def do_maketrie(self, args):
		"""Makes a trie with /usr/share/dict/words"""
		add_dictionaryWords(t, "/usr/share/dict/words")
		print("Done creating Trie!")

	def do_insert(self,args):
		"""Insert a word into a trie"""
		if len(args) != 0:
			for w in args.split():
				t.add_word(w.rstrip())

	def do_seeTrie(self, args):
		"""See your Trie. Warning:if you have a large trie, expect a large output!"""
		t.print_trie()

	def do_addBook(self, args):
		"""Create a reverse index of a large text file. Word and position will be added to the Trie"""
		if len(args) != 0:
			add_book(t, args)

	def do_getPosition(self, args):
		"""Lookup reverse index stored in Trie. For a word, get back the positions it exists"""
		if len(args) != 0:
			pl = []
			for w in args.split():
				pl = t.get_position(w.rstrip())
			for p in pl:
				print(p)

	def do_suggest(self, args):
		"""Ask the trie for suggestions by inputing some prefix"""
		if len(args) != 0:
			l = t.get_suggestion(args)
			for suggestion in l:
				print(suggestion)

	def complete_suggest(self, text, line, start_index, end_index):
		if text:
			return t.get_suggestion(text)
		else:
			return []

t = Trie()
if __name__ == '__main__':
	prompt = MyPrompt()
	prompt.prompt = '> '
	prompt.cmdloop('Starting Trie Shell...')
