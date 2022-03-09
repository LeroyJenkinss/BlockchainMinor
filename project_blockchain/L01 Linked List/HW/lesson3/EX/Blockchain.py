from hashlib import blake2b
import hashlib
import string 

class CBlock:
    
    def __init__(self, data=None, previousBlock=None, hashsize=1, previousHash=None):
        self.data = data
        self.previousBlock = previousBlock
        self.hashsize = hashsize
        if self.previousBlock != None and self.previousBlock.data != None:
            if isinstance(self.previousBlock.data, str):
                self.previousHash = hashlib.sha256(self.previousBlock.data.encode()).hexdigest()
            elif isinstance(self.previousBlock.data, bytes):
                decodeData = self.previousBlock.data.decode('UTF-8')
                self.previousHash = hashlib.sha256(decodeData.encode('UTF-8')).hexdigest()
            elif isinstance(self.previousBlock.data, int):
                strInt = str(self.previousBlock.data)
                self.previousHash = hashlib.sha256(strInt.encode()).hexdigest()
            elif isinstance(self.previousBlock.data, object):
                self.previousHash = hash(self.previousBlock.data)     
    
    def computeHash(self):
        if  isinstance(self.data, str):
            return hashlib.sha256(self.data.encode('UTF-8')).hexdigest()
        elif isinstance(self.data, bytes):
            return hashlib.sha256(self.data).hexdigest()
