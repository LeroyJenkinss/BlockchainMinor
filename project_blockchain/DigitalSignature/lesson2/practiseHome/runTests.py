from genarateKey import *

runningTrails =  key()

print(runningTrails.reverseCipher('hello'))

print(runningTrails.encryptCeasar('hallo', 2))
input = runningTrails.encryptCeasar('hallo', 2)
print(runningTrails.decrypt(input, 2))