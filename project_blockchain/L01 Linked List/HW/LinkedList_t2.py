from LinkedList import *

llist = LinkedList()

llist.insertBeg(2)
llist.insertEnd(1)
llist.insertBeg(3)
llist.insertEnd(4)
llist.insertEnd(4)
llist.insertAfter(4, 5)     # This call will insert 4 after the first occurrence 2 (if there are more than one 2)
                            # Linked List: 3 2 4 1 4
llist.deleteIndex(2)
llist.printList()

