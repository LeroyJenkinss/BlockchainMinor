
import string
import cryptography



from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512, SHA384, SHA256, SHA, MD5
from Crypto import Random
from base64 import b64encode, b64decode
class key:
    
    def reverseCipher(self,inputString):
        outputString = ''
        index = len(inputString) - 1

       
        for i in range(len(inputString)-1, -1, -1):
            outputString += inputString[i]
        return outputString

    def encryptCeasar(self, text, s):
        result = ''
        for i in range(len(text)):
            char  = text[i]

            if (char.isupper()):
                result += chr((ord(char) + s-65) % 26 + 65)
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
                
        return result

    def decrypt(self, inputMessage, key):
        outputMessage = ''
        alphabet = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"

        for c in inputMessage:
            if c in alphabet:
                position = alphabet.find(c)
                new_position = (position - key) % 26
                new_character = alphabet[new_position]
                outputMessage += new_character
            else:
                outputMessage += c
        return outputMessage
    
    def generateKey(keysize):
        
        random_generator = Random.new().read
        key = RSA.generate(keysize, random_generator)
        private, public = key, key.publickey()
        return public, private
def importKey(externKey):
   return RSA.importKey(externKey)
