from Signature import *
class Tx:
    inputs = None
    outputs =None
    sigs = None
    reqd = None
    def __init__(self):
        self.inputs     = []
        self.outputs    = []
        self.sigs       = []
        self.reqd       = []

    def add_input(self, from_addr, amount):
        self.inputs.append([from_addr,amount])

    def add_output(self, to_addr, amount):
        self.outputs.append([to_addr, amount])

    def add_reqd(self, req):
            self.reqd.append(req)

    def sign(self, private):
        in_outputs =self.conCatInOUtputs()
        self.sigs.append(sign(in_outputs, private))

    def is_valid(self):
        returnVal = False
        for a in self.sigs:
            if a == self.sigs[0]:
                returnVal = verify(self.conCatInOUtputs(), a, self.inputs[0][0])
            if len(self.sigs) > 1 and a == self.sigs[1]:
                returnVal = verify(self.conCatInOUtputs(), a, self.reqd)
                print(verify(self.conCatInOUtputs(), a, self.reqd))

        if len(self.reqd) != 0 and len(self.sigs) <= 1:
            returnVal = False
        
        if len(self.inputs) < len(self.sigs):
            returnVal = False
        
        outAmount = 0
        inAmount = 0
        negativeIn = False
        negativeOut = False

        for a in range(len(self.outputs)):
            outAmount += self.outputs[a][1]
            if self.outputs[a][1] < 0:
                negativeOut = True
        for a in range(len(self.inputs)):
            inAmount += self.inputs[a][1]
            if self.inputs[a][1] < 0:
                negativeIn = True
        
        if( outAmount > inAmount or negativeIn == True or negativeOut == True):
            returnVal = False
        
        return returnVal

    def conCatInOUtputs(self):
        return [*self.inputs, *self.outputs]
    