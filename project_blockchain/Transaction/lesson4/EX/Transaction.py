from Signature import *

class Tx:
    inputs = None
    outputs =None
    sigs = None

    # def __repr__(self):
    #     return repr([self.inputs, self.outputs])

    def __init__(self):
        self.inputs = []
        self.outputs = []
        self.sigs = []

    def add_input(self, from_addr, amount):
        self.inputs.append([from_addr, amount])

    def add_output(self, to_addr, amount):
        self.outputs.append([to_addr, amount])

    def sign(self, private):
        allLists = self.concateLists()
        self.sigs.append(sign(allLists, private))

    def concateLists(self):
        result = [*self.inputs, *self.outputs]
        return result
