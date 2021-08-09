#!/usr/bin/env python3
# -*- coding: utf-8

import socket, os, sys
from compte import compte

SOCKET_LINK = "/home/maxime/irc.socket"

class IRC_client:
    def __init__(client):
        if client.connect(SOCKET_LINK):
            print("Connected to server")
        else:
            print("Problem to connect")

    def Sending_data(client, data):
        client.send(data.encode("utf-8"))
        client.close()

    def message(user, msg):
        data = user.pseudo + ": " + msg
        print(data)
        return data

def main(user, msg):
    client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        IRC_client.__init__(client)
    except ValueError:
        print("Problem during connection to server")
    message = IRC_client.message(user, msg)
    IRC_client.Sending_data(client, message)


if __name__ == "__main__":
    user = compte("Riesjack", "TEYSSIER", "Maxime", 26)
    msg = str(sys.argv[1:]).replace("['","").replace("']","")
    main(user, msg)