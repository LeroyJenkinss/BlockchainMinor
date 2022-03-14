# Tarik Ualit 0995543 dinf3


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
       

    def insertBeg(self, new_data):    
        if self.head == None:
            self.head = Node(new_data)
            self.tail = self.head
            return

        else:
            old_head = self.head
            self.head = Node(new_data)
            self.head.next = old_head
            
    
    # Insert at the end
    def insertEnd(self, new_data):
        if self.head == None:
            self.head = Node(new_data)
            self.tail = self.head
            return
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = Node(new_data)
            return
            
    # Insert after a node llist.insertAfter(2, 4)
    def insertAfter(self, data, new_data):
        if self.head == None:
            return
        current_node = self.head
        if current_node.data == data:
            nextNode = current_node.next
            current_node.next = Node(new_data)
            current_node.next.next = nextNode
            return
        while current_node.next != None or current_node.data == data:
            if current_node.data == data:
                nextNode = current_node.next
                current_node.next = Node(new_data,nextNode)
                return
            current_node = current_node.next  
            
    # Deleting a node at a specific index
    def deleteIndex(self, index):
        if index == 0:
            self.head = self.head.next
        count = 1
        current_node = self.head
        while current_node.next != None:
            if count == index:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
            count += 1
        
    # Search an element, index is 0 based

    def find(self, key):
        if self.head == None:
            return -1
        if self.head.data == key:
            return 0
        count = 0
        current_node = self.head
        while current_node.data != key:
            count += 1 
            current_node = current_node.next
        if current_node.data == key:
                return count
        return 99


    # Sort the linked list
    def sort(self, head):
       valuesArray = []
       current_node = head
       while current_node != None:
           valuesArray.append(current_node.data)
           current_node = current_node.next
       valuesArray.sort()
       self.head = Node(valuesArray[0])

       for val in valuesArray[1:len(valuesArray)-1]:
           current_node = self.head
           while current_node.next != None:
               current_node = current_node.next
           current_node.next = Node(val)

     # Print the linked list
    def printList(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next

