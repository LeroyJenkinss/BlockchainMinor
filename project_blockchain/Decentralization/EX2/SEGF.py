def computeHash(self):
    prefixZeros = 2
    prefix = '0' * prefixZeros
    variablelist = []
    for a in range(0, 255):
        variablelist += str(a)
    if self.previousBlock is not None:
        self.previousHash = self.previousBlock.currentHash
    for i in range(100000000):
        self.Nonce = i
        digest = str(self.data) + str(i)
        if self.previousBlock is not None and digest[2] in variablelist:
            digest += str(self.previousHash)
        digest = sha256(digest)
        if digest is not None and digest.startswith(prefix):
            print(digest)
            self.currentHash = digest
            return self.Nonce