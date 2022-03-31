from Signature import *
import pickle
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend



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

    def save_keys(keys_file_name, keys, pw):
    
        
        keysOutput = ()
        
        (private_key, public_key)  = keys 
        private_keyOutput = private_key.private_bytes(
            encoding = serialization.Encoding.PEM, format = serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm = serialization.BestAvailableEncryption(str.encode(pw))
        )

        public_keyOutput = public_key.public_bytes(
            encoding = serialization.Encoding.PEM,
            format = serialization.PublicFormat.SubjectPublicKeyInfo
        )
        keysOutput = (private_keyOutput, public_keyOutput)
        savefile = open(keys_file_name, "wb")
        pickle.dump(keysOutput, savefile)
        savefile.close()
    

    def load_keys(key_names, pw):
    
        loadfile = open(key_names, "rb")
        keys = pickle.load(loadfile)
        loadfile.close()

        private_key = keys[0]
        public_key  = keys[1]
        
        try:
            private_key = serialization.load_pem_private_key(private_key,password=str.encode(pw), backend=default_backend())
        except ValueError:
            raise Exception("Incorrect password")
        public_key = serialization.load_pem_public_key(public_key)

        keys = (private_key,public_key)
        return keys

    def is_valid(self):
        for a in self.sigs:
            if a == self.sigs[0]:
                return verify(self.concateLists(), a, self.inputs[0][0])
                
  