
from hashlib import blake2b


# Read the text file "names.txt" 
file =  open('names.txt', 'r')
   
# Ask the user to enter a name
name = input("Enter your name: ")
# Compute the hash of the input using blake2b (hash size = 1 byte)

hashsize = 2
check = blake2b(name.encode('UTF-8'),digest_size=hashsize).hexdigest()
# Check the names in the file to see if you can find a collision
countCol = 0
for a in file:
    output = a.rstrip()
    
    col = blake2b(output.encode('UTF-8'),digest_size=hashsize).hexdigest()
    if col == check:

        print(f"{col} + {output}: {check}")
        countCol += 1 
        
print('number of collisions ' + str(countCol))
