from cryptography.hazmat.primitives import hashes
import hashlib 



# compute the hash of original.png using SHA256
hashsize = 1
with open('original.png', 'rb') as f:
    bytes = f.read()
    readable_hash = hashlib.sha256(bytes).hexdigest()

for _ in range(1,5):
    filename = f"copy({_}).png"
    print('this is the filename '+filename)
    with open(filename, 'rb') as g:
        bytes = g.read()
        readable_copy = hashlib.sha256(bytes).hexdigest()
    if readable_hash == readable_copy:
        print('The original is the same as ' + filename)
# compute hash of file copy(1).png, copy(2).png, copy(3).png, and copy(4).png
# and test which of these files is/are equal to the original file 

