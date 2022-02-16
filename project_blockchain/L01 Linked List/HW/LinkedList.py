class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insertBeg(self, new_data):    
        if self.head == None:
            self.head = Node(new_data)
            self.tail = self.head
            self.count += 1
            return
        else:
            old_head = self.head
            self.head = Node(new_data)
            self.head.next = old_head
            self.count += 1 

        
    
        
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
            
    # Insert after a node
    def insertAfter(self, data, new_data):
        pass

    # Deleting a node at a specific index
    def deleteIndex(self, index):
        pass

    # Search an element
    def find(self, key):
        return -1

    # Sort the linked list
    def sort(self, head):
        pass

     # Print the linked list
    def printList(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next

