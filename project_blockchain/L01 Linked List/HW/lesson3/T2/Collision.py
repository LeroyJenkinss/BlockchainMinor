from hashlib import blake2b
from opcode import hasname
import string
import random


def gen_random_string(n):
    randomString = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))
    return blake2b(randomString.encode('UTF-8'),digest_size=hashsize).hexdigest()

hashsize = 1

# Ask the user to enter a name
name = input("Enter your name: ")

# Compute the hash of the input using blake2b (hash size = 1 byte)
hasName = blake2b(name.encode('UTF-8'),digest_size=hashsize).hexdigest()

# use gen_random_string() to see if you can find a collision
countCol = 0
for _ in range(100000):

   randomResult =  gen_random_string(8).rstrip()
   
   if randomResult == hasName:
       print(gen_random_string(_) + ' ' +  gen_random_string(_).rstrip() + ' ' + randomResult+ ' '+ hasName)

       countCol += 1

print('number of collisions ' + str(countCol))



