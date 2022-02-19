
class SongNode:
    def __init__(self, song_title=None, next = None, prev = None):
        self.song_title = song_title
        self.next = next
        self.prev = prev
    
   

class SongList:
    def __init__(self):  
        self.head = None
        self.tail = None
        self.count = 0
        

    def printSongs(self):
        current_node = self.head
        while current_node.next != None:
            print(current_node.song_title)
            current_node = current_node.next
        

    def AddNewSong(self, new_song_title):
        if self.head == None:
            self.head = SongNode(new_song_title)
            self.tail = self.head
        node = self.head
        while node.next != None:
            node = node.next
        node.next = SongNode(new_song_title,None,node)
        