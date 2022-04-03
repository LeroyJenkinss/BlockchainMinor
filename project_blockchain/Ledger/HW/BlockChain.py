import pickle
class CBlock:
    previousHash = None
    currentHash = None
    previousBlock = None
    data = None

    def computeHash(self):
        hashIn = str(pickle.dumps(self.data))
        if self.previousHash is not None:
            hashIn = hashIn + str(self.previousHash)
        return hash(hashIn)
