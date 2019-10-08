"""
MIT License

Copyright (c) 2019 Gruber Quentin

"""

import socket
import time
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

    def __init__(self, serverIp="192.168.131.129", serverPort=18944):
        self.socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
        self.serverIp = serverIp
        self.serverPort = serverPort

        self.sock.connect((self.serverIp, self.serverPort))

        while True:
            time.sleep(0.1)
            data = self.sock.recv(1024)
            print(repr(data))
            with open("log.txt", "a+") as file:
                file.write(repr(data) + "\n")


OpenIGTClient()
