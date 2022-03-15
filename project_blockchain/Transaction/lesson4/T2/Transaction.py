from Signature import *
from Transaction_t import *
class Tx:
    inputs = None
    outputs = None

    def __init__(self):
        pass

    def add_input(self, from_addr, amount):
        if self.inputs == None:
            self.inputs = []
        for a in keys_list:
            b = 0
            if self.decrypt(from_addr) == keys_list[b]:
                self.inputs.append((decrypt(from_addr), amount))
            b+1

    def add_output(self, to_addr, amount):
        if self.outputs == None:
            self.outputs = []
        self.outputs.append((to_addr, amount))

    signedArray = []

    for a in keys_list:
        signedMessage = sign(a.encode('UTF-8'),alex_prv)
        output = verify(a.encode(), signedMessage, alex_pbc)
    
    print(output)

def encrypt(message, public_key):
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def decrypt(ciphertext, private_key):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )