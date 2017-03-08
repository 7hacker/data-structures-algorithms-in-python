'''
implement a stack with the usual stack semantics but additionally also returns the Minimum value in the stack in O(1)
'''
class Stack(object):
    
    def __init__(self):
        self.stack = []
        self.minstack = []
        return
    
    
    def push(self, item):
        self.stack.append(item)
        if len(self.stack )== 1:
            self.minstack.append(item)
        else:
            if item < self.minstack[-1]:
                self.minstack.append(item)
            else:
                self.minstack.append(self.minstack[-1])
        return
    
    def pop(self):
        self.minstack.pop(-1)
        return self.stack.pop(-1)
    
    def getMin(self):
        if len(self.stack) == 0:
            return None
        return self.minstack[-1]
    
s = Stack()
s.push(1)
s.push(5)
s.push(3)
s.push(0)
s.push(5)
print(s.getMin())