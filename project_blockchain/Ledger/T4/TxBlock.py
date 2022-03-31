from BlockChain import CBlock
from Signature import generate_keys, sign, verify
from Transaction import *
from Transaction import Tx

class TxBlock (CBlock):
    
    def __init__(self, previousBlock):
        self.data = ''
        self.previousBlock = previousBlock
        super().__init__(self.data, previousBlock)
        self.tx = []

    def addTx(self, Tx_in):
        self.tx.append(Tx_in)
    
    def is_valid(self):
        invalid = []
        for a in self.tx:
            if (a.is_valid()):
                print('valid')
            else:
                invalid.append(a.is_valid())
        return len(invalid) == 0
