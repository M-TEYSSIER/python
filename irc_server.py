#!/usr/bin/env python3
# -*- coding: utf-8

import socket, os

SOCKET_LINK = "/home/maxime/irc.socket"
server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

class IRC_Server:
    def __init__():
        if os.path.exists(SOCKET_LINK):
            os.remove(SOCKET_LINK)
    
    def __disconnect__():
        server.close()
        print("Disconnected")

    def __socket__(server):
        server.bind(SOCKET_LINK)
        server.listen(5)

    def client(self):
        client, _ = self.accept()
        datagram = client.recv(1024)
        print("-" * 20)
        print(datagram.decode('utf-8'))
        print("-" * 20)

def main():
    irc = IRC_Server
    irc.__init__()
    irc.__socket__(server)
    while True:
        try:
            irc.client(server)
        except ValueError:
            print("Problem with client !")
            irc.__disconnect__()

if __name__ == "__main__":
    main()