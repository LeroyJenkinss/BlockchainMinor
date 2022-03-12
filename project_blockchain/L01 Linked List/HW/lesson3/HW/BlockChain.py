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
        

        if self.previousBlock != None:
            self.previousHash = self.sha256(self.previousBlock.data)
        if self.data != None:
            self.CurrentHash = self.sha256(self.data)

    def sha256(self,message):
        return hashlib.sha256(message.encode('UTF-8')).hexdigest()

    def mine(self, leading_zeros):
        self.leadingNumbers = leading_zeros
        prefix = '0' * self.leadingNumbers
        for i in range(1000):
            if self.previousBlock == None:
                digest = self.sha256(str(self.data) + str(i))    
            else:
                digest = self.sha256(str(self.previousBlock.data) + str(i))
            if digest.startswith(prefix):
                print ("after " + str(i) + " iterations found nonce: "+ digest)
                digest = self.CurrentHash
                return digest


    def is_valid_hash(self):
         
#  B1 = CBlock('data1', Gn)
        if self.previousBlock.data != None:
            if CBlock(self.previousBlock.data,self.previousBlock) == self.previousBlock.CurrentHash:
                
                return True
            return False
        