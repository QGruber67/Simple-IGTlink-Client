"""
MIT License

Copyright (c) 2019 Gruber Quentin

"""

import socket, time
from threading import Thread


class SocketReceiverThread(Thread):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listeners = set()

    def __init__(self, sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)):
        Thread.__init__(self)
        self.sock = sock

    def addListener(self, listener):
        self.listeners.add(listener)

    def removeListener(self, listener):
        self.listeners.remove(listener)


class OpenIGTClient:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientResponseHandler = SocketReceiverThread()

    def __init__(self, serverIp="127.0.0.1", serverPort=18944):
        self.socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
        self.serverIp = serverIp
        self.serverPort = serverPort

        self.sock.connect((self.serverIp, self.serverPort))
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, 1)

        clientResponseHandler = SocketReceiverThread(self.sock)
        clientResponseHandler.setDaemon(True)
        clientResponseHandler.start()

        while True:
            time.sleep(0.1)
            pass
            clientResponseHandler.join()

    def addOpenIGTListener(self, Listener):
        self.clientResponseHandler.addListener(Listener)


OpenIGTClient()
