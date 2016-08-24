'''
A skip list implemented in python borrowing from the fantastic explanation here: https://kunigami.wordpress.com/2012/09/25/skip-lists-in-python/
'''
from cmd import Cmd
from random import randint, seed
import sys


class SkipNode:
    """A node in a skip list"""    
    def __init__(self, height = 0, elem = None):
        self.elem = elem
        self.next = [None]*height

class SkipList:
    def __init__(self, maxHeight):
        #sentinel is a HEAD node with NONE element and 0 height when started
        self.head = SkipNode()
        self.maxHeight = maxHeight

    def getRandomHeight(self):
        return randint(0,self.maxHeight)

    def updateList(self, elem):
        #This routine returns a node per level that is the node with Greatest Value smaller than elem
        update = [None] * len(self.head.next)
        x = self.head
        for i in reversed(xrange(len(self.head.next))):
            while x.next[i] != None and x.next[i].elem < elem:
                x = x.next[i]
            update[i] = x
        return update

    def findList(self, elem, updateL=None):
        #this routine finds an element in a skip list, by getting an update list and then navigating it
        if not updateL:
            updateL = self.updateList(elem)
        if len(updateL):
            candidate = updateL[0].next[0]
            if candidate != None and candidate.elem == elem:
                return candidate
        return None

    def insertList(self,elem):
        #create a new Node
        newNode = SkipNode(self.getRandomHeight(), elem)
        print("Inserting till height: " + str(len(newNode.next)))
        #update sentinel's levels if its smaller
        while len(newNode.next) > len(self.head.next):
            self.head.next.append(None)

        updateL = self.updateList(elem)
        if self.findList(elem, updateL) == None:
            for i in xrange(len(newNode.next)):
                newNode.next[i] = updateL[i].next[i]
                updateL[i].next[i] = newNode

    def showList(self):
        x = self.head
        for i in reversed(xrange(len(self.head.next))):
            y = x.next[i]
            sys.stdout.write("\nLEVEL: " + str(i) + "\n")
            while y.next != None:
                sys.stdout.write(str(y.elem) + " ")
                y = y.next
            sys.stdout.write(str(y.elem) + " ")






class MyPrompt(Cmd):
    def do_quit(self, args):
        """Quits the program."""
        print "Quitting."
        raise SystemExit

    def do_insert(self,args):
        """Insert an integer into a skiplist"""
        if len(args) != 0:
            for w in args.split():
                sl.insertList(int(w.rstrip()))

    def do_seeSkipList(self, args):
        """See your Skip List"""
        sl.showList()


sl = SkipList(6)
if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = '> '
    prompt.cmdloop('Starting SkipList Shell...')
