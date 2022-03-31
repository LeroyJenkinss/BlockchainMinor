from BlockChain import CBlock
from Signature import generate_keys, sign, verify
from Transaction import Tx

class TxBlock (CBlock):
    
    def __init__(self, previousBlock):
        pass

    def addTx(self, Tx_in):
        pass
    
    def is_valid(self):
        pass