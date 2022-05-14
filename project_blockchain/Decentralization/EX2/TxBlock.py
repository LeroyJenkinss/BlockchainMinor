from BlockChain import CBlock
from Signature import generate_keys, sign, verify
from Transaction import Tx

reward = 25.0


class TxBlock (CBlock):

    def __init__(self, previousBlock):
        self.previousBlock = previousBlock
        super().__init__(self.data, previousBlock)

    def addTx(self, Tx_in):
        self.new_tx = TxBlock(Tx_in)
        self.tx_list = []
        self.tx_list.append(self.new_tx)

    def __count_totals(self):
        pass

    def is_valid(self):
        for i in self.tx_list:
            if Tx.is_valid(i.previousBlock):
                if super().is_valid():
                    return True
            else:
                return False

    def good_nonce(self):
        pass

    def find_nonce(self):
        pass
