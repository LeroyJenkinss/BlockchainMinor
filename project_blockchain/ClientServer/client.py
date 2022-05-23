# echo-client.py
import socket
import time

TCP_IP = '145.137.16.126'
TCP_PORT = 5055
BUFFER_SIZE = 1024
MESSAGE = "TARIK IS VEGAN"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    while True:
        time.sleep(2)
        s.send(str(len(MESSAGE)).encode('utf-8') + str(64 - len(MESSAGE)).encode('utf-8'))
        s.send(MESSAGE.encode('utf-8'))
        data = s.recv(BUFFER_SIZE)
        # s.close()
        print("received data: {}".format(data))

print(f"Received {data!r}")
