from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import hashlib
from hashlib import sha256


hash_func = lambda x: sha256(x.encode('utf-8')).hexdigest()
class CBlock:
    previousHash = None
    currentHash = None
    previousBlock = None
    data = None
    nonce = 0

    def __init__(self, data, previousBlock):
        self.data = data
        self.previousBlock = previousBlock
        self.CurrentHash = self.computeHash(str(data))
        self.nonce = 1
        if previousBlock is not None:
            self.previousHash = self.previousBlock
    
    def computeHash(self):
        global hash1
        try:
            hash1 = (str(self.data.string)+ str(self.previousHash))
        except:
            hash1 = str(self.data) + str(self.previousHash)
            if self.previousHash is not None:
                hash1 = hash1 + str(self.previousBlock.computeHash())
                return hash(hash1)

    def is_valid(self):
        currentBlock = self
        check = True
        while currentBlock is not None:
            coming_block = str(currentBlock.data) #+ str(currentBlock.nonce)
            if currentBlock.previousBlock is not None:
                coming_block += str(currentBlock.previousHash)
        newHash = hash_func(coming_block)
        if newHash != currentBlock.CurrentHash:
            check = False
        else:
            check = True
        currentBlock = currentBlock.previousBlock
        return check