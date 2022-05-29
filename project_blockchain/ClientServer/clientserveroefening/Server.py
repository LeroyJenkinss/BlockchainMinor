from copyreg import pickle
import socket
import time
import pickle

# take the server name and port name
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 3125
# HEADERSIZE = 10
s.bind((socket.gethostname(), port))
print('Socket binded to port 3125')
s.listen(3)
print('socket is listening')
while True:
    conn, addr = s.accept()
    print(f"Connection from {addr} has been established!")

    d = conn.recv(80000)
    print(d)
    msg = pickle.loads(d)
    print(msg)
    if msg.is_valid():
        print("Valid transaction is validated")
    else:
        print("invalid transaction is not validated")




