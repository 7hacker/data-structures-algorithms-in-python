'''
How to build a Shell-esque Prompt interface using python
'''
from cmd import Cmd

class MaxQueue:
    def __init__(self):
        self.q = []
        self.maxq = []

    def queue(self,item):
        self.q.append(item)
        if len(self.maxq):
            if item >= self.maxq[0]:
                while len(self.maxq):
                    self.maxq.pop()
            else:
                while item >= self.maxq[-1]:
                    self.maxq.pop()
        self.maxq.append(item)
        return

    def getMax(self):
        if len(self.maxq):
            return self.maxq[0]
        else:
            return None

    def dequeue(self):
        d = None
        if len(self.q):
            d = self.q.pop(0)
        if d:
            if d == self.maxq[0]:
                self.maxq.pop(0)
        return d


    def showQueue(self):
        import sys
        for item in self.q:
            sys.stdout.write(str(item)+ " ")
        sys.stdout.write("\n")
        sys.stdout.write("Current Max: " )
        sys.stdout.write(str(self.getMax()))
        sys.stdout.write("\n")

        return


class MyPrompt(Cmd):
    def do_queue(self,args):
        """Add to the queue"""
        if len(args) == 0:
            print "Nothing to add.."
        else:
            for i in args.split():
                myQueue.queue(int(i))
        myQueue.showQueue()

    def do_dequeue(self, args):
        """Delete from Queue"""
        print myQueue.dequeue()
        myQueue.showQueue()


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

myQueue = MaxQueue()
if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt...')
