class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insertBeg(self, new_data):    
        if self.head == None:
            new_node = Node(new_data, None, None)
            self.head = new_node
            self.tail = self.head
            self.count += 1
        else:
            node = self.head
            new_node(new_data,node,None)
            self.head = new_node  
            self.count += 1 

        
    
        
    # Insert at the end
    def insertEnd(self, new_data):
        pass

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
        if current_node != None and current_node.next == None:
            print(current_node.data)
        else:
            while current_node.next != None:
                print(current_node.data)
                current_node = current_node.next

    