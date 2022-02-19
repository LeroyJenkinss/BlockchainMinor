class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, data):
        self.data = data
        
    def setNext(self,next):
        self.next = next

class LinkedList:    

    def __init__(self):
        self.head = None 
        self.tail = None
        self.len = 0

    def append(self, item):
        # This method should append an item to the end of the list
        if self.head == None:
            self.head = item
        if self.tail != None:
            self.tail.next = item
        self.tail = item
        self.len += 1
        

    def getLen(self):
        if self.head == None:
            return 0
        current_node = self.head
        counter = 1
        while current_node.next != None:
            current_node = current_node.next
            counter += 1 
        return counter

    def printAll(self):
        cur = self.head
        while cur.next != None:
            print(cur.getData())
            cur = cur.next
      
       