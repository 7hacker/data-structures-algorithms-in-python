'''
A priority Queue
'''
class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        return

class PriorityQueue:
    def __init__(self):
        self.plist = [] #root of tree will be self.plist[0], last_item will be self.plist[len(self.plist)-1]
        return

    def get_parent(self, i):
        return (i - 1)/2 if i-1 >= 0 else 0

    def get_children(self, i):
        last_item_index = len(self.plist) -1 
        #return (left child,right child) tuple
        return (
                (2*i + 1) if ((2*i + 1) <= last_item_index) else None ,
                (2*i + 2) if ((2*i + 2) <= last_item_index) else None
            )

    def swap(self, i, j):
        #swaps data of items at index i and j in the plist
        tempNode = Node(self.plist[i].data, self.plist[i].priority)
        self.plist[i].data = self.plist[j].data
        self.plist[i].priority = self.plist[j].priority
        self.plist[j].data = tempNode.data
        self.plist[j].priority = tempNode.priority
        return

    def bubble_heap(self):
        #called when element is added and element must bubble up to its correct priority position
        last_item_index = len(self.plist) - 1
        parent_index = self.get_parent(last_item_index)
        
        if parent_index == 0 and self.plist[last_item_index].priority > self.plist[parent_index].priority:
            self.swap(last_item_index, 0)
            return

        while self.plist[last_item_index].priority > self.plist[parent_index].priority:
            self.swap(last_item_index, parent_index)
            last_item_index = parent_index
            parent_index = self.get_parent(last_item_index)
        return


    def add_element(self, item, priority):      
        newNode = Node(item, priority)
        self.plist.append(newNode)
        self.bubble_heap()
        return

    def is_leaf(self, index):
        #leaf node has no children
        (cl, cr) = self.get_children(index)
        if cl is None and cr is None:
            return True
        else:
            return False

    def who_is_max(self, index, lc, rc):
        #will be called on a node which has atleast a left-child guaranteed
        index_priority = self.plist[index].priority
        lc_priority = self.plist[lc].priority
        rc_priority = None

        if rc is not None:
            rc_priority = self.plist[rc].priority
            if index_priority > lc_priority and index_priority > rc_priority:
                return index
            if lc_priority > index_priority and lc_priority > rc_priority:
                return lc
            return rc

        else:
            #there is no right child
            return index if index_priority > lc_priority else lc

    def trickle_heap(self):
        #called only if the heap has more than 1 element so no need to check that here

        #special condition if size == 2
        if len(self.plist) == 2:
            #only 2 items exist in the whole tree
            if self.plist[1].priority > self.plist[0].priority:
                self.swap(0,1)
                return
            else:
                return
        else:
            #both left and right child exist. tree could be size 3 or more
            continue_index = 0
            (cl,cr) = self.get_children(continue_index)
            done = False
            #keep doing this until you are a leaf or you are greater than children
            while not self.is_leaf(continue_index) and not done:
                max_index = self.who_is_max(continue_index, cl, cr)
                if max_index == continue_index:
                    #i am the highest
                    done = True
                else:
                    self.swap(continue_index, max_index)
                    continue_index = max_index
                    (cl, cr) = self.get_children(continue_index)
        return



    def remove_element(self):
        if len(self.plist) == 0:
            #if list is empty return nothing
            return(None,None)

        if len(self.plist) == 1:
            #if list has only 1 item, return it and empty the list
            popped = self.plist[0].data
            popped_priority = self.plist[0].priority
            self.plist = []
            return (popped, popped_priority)
            
        #save return data
        popped = self.plist[0].data
        popped_priority = self.plist[0].priority
        
        #reduce list by 1 item after moving last item to root
        last_item_index = len(self.plist) - 1
        self.swap(0,last_item_index)
        self.plist.pop()

        #call trickle_heap to trickle the root down to its proper position
        self.trickle_heap()

        return (popped, popped_priority)

    def get_size(self):
        return self.size

    def print_queue(self):
        i = 0
        for item in self.plist:
            print "plist[" + str(i) + "]: Priority :" + str(item.priority) + " Data : " + str(item.data)
            i = i + 1
        return

mypq = PriorityQueue()
mypq.add_element('a', 26)
mypq.add_element('b', 37)
mypq.add_element('c', 76)
mypq.add_element('d',8)
mypq.add_element('e',18)
mypq.add_element('f',74)
mypq.add_element('g', 29)
mypq.add_element('h', 39)
mypq.add_element('i', 20)
mypq.add_element('j',32)
mypq.add_element('k',89)
mypq.add_element('l',28)
mypq.add_element('m',66)
#mypq.print_queue()
mypq.add_element('n',100)
mypq.print_queue()
print("Dequeue:")
print(mypq.remove_element())
mypq.print_queue()

print("Dequeue:")
print(mypq.remove_element())
mypq.print_queue()

print("Dequeue:")
print(mypq.remove_element())
mypq.print_queue()

print("Dequeue:")
print(mypq.remove_element())
mypq.print_queue()

print("Dequeue:")
print(mypq.remove_element())
mypq.print_queue()

print("Dequeue:")
print(mypq.remove_element())
mypq.print_queue()


print("Dequeue:")
print(mypq.remove_element())
mypq.print_queue()


print("Dequeue:")
print(mypq.remove_element())
mypq.print_queue()


print("Dequeue:")
print(mypq.remove_element())
mypq.print_queue()


print("Dequeue:")
print(mypq.remove_element())
mypq.print_queue()


print("Dequeue:")
print(mypq.remove_element())
mypq.print_queue()


print("Dequeue:")
print(mypq.remove_element())
mypq.print_queue()


print("Dequeue:")
print(mypq.remove_element())
mypq.print_queue()


print("Dequeue:")
print(mypq.remove_element())
mypq.print_queue()


print("Dequeue:")
print(mypq.remove_element())
mypq.print_queue()


