import hashlib

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes


class CBlock:

    def __init__(self, data, previousBlock):
        self.data = data
        self.previousBlock = previousBlock
        self.currentHash = None
        pass

    def computeHash(self):
        prefixZeros = 5
        prefix = '0' * prefixZeros
        variablelist = []
        for a in range(0, 255):
            variablelist += str(a)
        if self.previousBlock is not None:
            self.previousHash = self.previousBlock.currentHash
        for i in range(100000000):
            self.Nonce = i
            digest = str(self.data) + str(i)
            if self.previousBlock is not None and digest[5] in variablelist:
                digest += str(self.previousHash)
            digest = sha256(digest)
            if digest is not None and digest.startswith(prefix):
                print(digest)
                self.currentHash = digest
                return self.Nonce

    def is_valid(self):
        currentBlock = self
        check = True
        while currentBlock is not None:
            digest = str(currentBlock.data) + str(currentBlock.Nonce)
            if currentBlock.previousBlock is not None:
                digest += str(currentBlock.previousHash)
            newHash = sha256(digest)
            if newHash != currentBlock.currentHash:
                check = False
            currentBlock = currentBlock.previousBlock
        return check


def sha256(message):
    return hashlib.sha256(message.encode('UTF-8')).hexdigest()