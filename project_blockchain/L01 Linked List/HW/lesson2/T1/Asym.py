import string

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def generate_keys():
    
    private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048)

    
    public_key = private_key.public_key()
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo)
        
    private = private_key
    public = public_key

    return private, public

def encrypt(message, key):
    try:
        ciphertext = key.encrypt(
        message,padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None))
        return ciphertext
    except:
        return False

def decrypt(ciphertext, key):
    try:
        plaintext = key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None))
        return plaintext
    except: 
        return False

