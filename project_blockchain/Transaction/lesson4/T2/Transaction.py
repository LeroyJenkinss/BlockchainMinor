from Signature import *
from Transaction_t import *

class Tx:
    inputs = None
    outputs = None
    keysList = None

    def __init__(self):
        pass

    
    def add_input(self, from_addr, amount):
        if self.inputs is None:
            self.inputs = []
        self.inputs.append([from_addr, amount])

    def add_output(self, to_addr, amount):
        if self.outputs is None:
            self.outputs = []
        self.outputs.append([to_addr, amount])


    
