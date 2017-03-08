'''
given a linked list and a value K, generate a linked list such that upto K elements are reversed. example for input 1,2,3,4,5,6,7,8 and k=5 the output list is: 5,4,3,2,1,8,7,6
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        return

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        return
    
    def append(self,n):
        #adds to tail
        self.size = self.size + 1
        if self.head == None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n
    
    def pushAtHead(self,n):
        #adds at head, by making a new head and moving current head forward
        #can be used to reverse a list, since it behaves like a stack
        self.size = self.size + 1
        if self.head == None:
            self.head = n
            self.tail = n
        else:
            n.next = self.head
            self.head = n

    def getSize(self):
        return self.size
    
    def printList(self):
        trav = self.head
        while trav != None:
            print(trav.data)
            trav = trav.next

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail


    def revKList(self, k):
        trav = self.head
        allLists = [] #List of LinkedLists
        
        #make reversed lists of size k : till you cant make them anymore
        while(trav != None):
            iL = LinkedList()
            count = 0
            while count < k and trav != None:
                n = trav
                trav = trav.next
                iL.pushAtHead(n)
                count = count + 1
            iL.getTail().next = None
            allLists.append(iL)
        
        #stitch up the reversed k-sized lists
        for i in range(len(allLists)):
            if i != len(allLists) -1 :
                allLists[i].getTail().next = allLists[i+1].getHead()
            else:
                pass

        #reset the head
        self.head = allLists[0].getHead()

        return





myList = LinkedList()
myList.append(Node(1))
myList.append(Node(2))
myList.append(Node(3))
myList.append(Node(4))
myList.append(Node(5))
myList.append(Node(6))
myList.append(Node(7))
myList.append(Node(8))

myList.revKList(5)
myList.printList()

