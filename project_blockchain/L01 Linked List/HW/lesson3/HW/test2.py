import hashlib

def sha256(message):
    return hashlib.sha256(message.encode('UTF-8')).hexdigest()


def mine(message, difficulty=1):
   
   prefix = '1' * difficulty
   for i in range(1000):
      digest = sha256(str(hash(message)) + str(i))
      print('hello')
      if digest.startswith(prefix):
          print('hi')
          print ("after " + str(i) + " iterations found nonce: "+ digest)
          return digest

print(mine("test message", 2))