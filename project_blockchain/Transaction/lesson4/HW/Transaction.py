
class Tx:
    inputs = None
    outputs =None
    sigs = None
    reqd = None
    def __init__(self):
        pass
    def add_input(self, from_addr, amount):
        pass
    def add_output(self, to_addr, amount):
        pass
    def sign(self, private):
        pass        
    def is_valid(self):
        return False