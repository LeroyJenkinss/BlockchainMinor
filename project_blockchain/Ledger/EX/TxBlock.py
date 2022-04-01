from BlockChain import CBlock
from Signature import generate_keys, sign, verify
from Transaction import Tx

class TxBlock (CBlock):
    
    def __init__(self, previousBlock):
        self.previousBlock = previousBlock
        super().__init__(self.data, previousBlock)
        self.tx_list = []

    def addTx(self, Tx_in):
        self.new_tx = TxBlock(Tx_in)
        self.tx_list.append(self.new_tx)
    
    def is_valid(self):
        invalid = []
        for a in self.tx_list:
            if (Tx.is_valid(a.previousBlock)):
               if(super().is_valid_hash()):
                   invalid.append(True)
            else:
                invalid.append(False)
        for a in invalid:
            if a == False:
                return False
            return True
    