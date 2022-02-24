import encodings
from cryptography.exceptions import *
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
import pickle

def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537,key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

def sign(message, private_key):
    input = message.encode()
    signature = private_key.sign(
        input,
        padding.PSS(
           mgf=padding.MGF1(hashes.SHA256()),
           salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def verify(message, signature, public_key):
    inputMessage = message.encode()
    try:
        public_key.verify(
            signature,
            inputMessage,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except:
        return False

def save_keys(keys_file_name, keys, pw):
    if pw == '1999':
        
        keysOutput = ()
        
        (private_key, public_key)  = keys 
        private_keyOutput = private_key.private_bytes(
            encoding = serialization.Encoding.PEM, format = serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm = serialization.BestAvailableEncryption(b'1999')
        )

        public_keyOutput = public_key.public_bytes(
            encoding = serialization.Encoding.PEM,
            format = serialization.PublicFormat.SubjectPublicKeyInfo
        )
        keysOutput = (private_keyOutput, public_keyOutput)
        savefile = open(keys_file_name, "wb")
        pickle.dump(keysOutput, savefile)
        savefile.close()
    else:
        return 'Wrong password'

def load_keys(key_names, pw):
    if pw == '1999':
        loadfile = open(key_names, "rb")
        keys = pickle.load(loadfile)
        loadfile.close()

        private_key = keys[0]
        public_key  = keys[1]
       
        
        private_key = serialization.load_pem_private_key(private_key,password=b'1999')
        public_key = serialization.load_pem_public_key(public_key)

        keys = (private_key,public_key)
        return keys
    return 'Wrong password'