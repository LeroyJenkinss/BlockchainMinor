import socket

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004
print('Waiting for connection response')


def getInput():
    question = input('What do you need?')
    return question


try:
    ClientMultiSocket.connect((socket.gethostbyname('localhost'), port))
except socket.error as e:
    print(str(e))
res = ClientMultiSocket.recv(1024)

while True:
    # Input = input('Hey there: ')
    Input = getInput()
    ClientMultiSocket.send(str.encode(Input))
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))
ClientMultiSocket.close()
