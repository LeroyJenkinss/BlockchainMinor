from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import hashlib
from hashlib import blake2b


class CBlock:
    def __init__(self,data,previousBlock = None, previousHash = None, CurrentHash = None, leadingNumbers = 2):
        self.data = data
        self.previousBlock = previousBlock
        self.previousHash = None
        self.CurrentHash = None
        self.leadingNumbers = leadingNumbers
        

    def sha256(self,message):
        return hashlib.sha256(message.encode('UTF-8')).hexdigest()

    def mine(self, leading_zeros):
        self.leadingNumbers = leading_zeros
        prefix = '0' * self.leadingNumbers
        digest = ''
        for i in range(1000):
            if self.previousBlock == None:
                digest = self.sha256(str(self.data) + str(i))   
            else:
                digest = self.sha256(str(self.previousHash) + str(i))
            if digest.startswith(prefix):
                if self.previousBlock != None:
                    self.previousHash = self.CurrentHash
                    self.CurrentHash = digest
                return digest


    def is_valid_hash(self):
        if self.previousBlock == None:
            return True
        if self.previousBlock != None:
            if self.previousHash == self.previousBlock.CurrentHash and self.previousHash != None and self.previousBlock.CurrentHash != None:
                return True
            return False
        