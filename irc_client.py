#!/usr/bin/env python3
# -*- coding: utf-8

from compte import compte
import socket
import argparse
import logging

SOCKET_LINK = "/home/maxime/irc.socket"

class IRC_client:
    def __init__(client):
        #TODO: Why problem pop during connection on IF condition
        if client.connect(SOCKET_LINK):
            print("Connected to server")
        else:
            print("Problem to connect")
        
    def Sending_data(client, data):
        client.send(data.encode("utf-8"))
        client.close()

    def message(user, msg):
        data = user.pseudo + "(" + user.nom + "_" + user.prenom + "_" + str(user.age) + ")" + ": " + msg
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
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--message", help="Message to send to IRC server")
    parser.add_argument("-u", "--username", help="Username identification")
    parser.add_argument("-ln", "--last-name", help="Last name of writer")
    parser.add_argument("-fn", "--first-name", help="First name of writer")
    parser.add_argument("-a", "--age", help="Age of writer", type=int)
    args=parser.parse_args()
    msg = args.message

    user = compte(
                args.username, 
                args.last_name,
                args.first_name, 
                args.age)

    main(user, msg)