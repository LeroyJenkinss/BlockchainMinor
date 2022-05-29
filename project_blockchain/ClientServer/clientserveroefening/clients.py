import socket
import pickle



class Clients:

    def sendMethod(self,msg):
        # HEADERSIZE = 10

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = 3125
        s.connect((socket.gethostname(), 3125))
        z = pickle.dumps(msg)

        s.sendall(z)

