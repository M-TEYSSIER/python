#!/usr/bin/env python3
# -*- coding: utf-8

from compte import compte
import socket
import argparse
import logging

logging.basicConfig(level=logging.DEBUG)

SOCKET_LINK = "~/irc.socket"

class IRC_client:
    def __init__(client):
        try:
            client.connect(SOCKET_LINK)
            logging.info("Established connection with server")
        except:
            logging.error("Connection failed to the server")

    def Sending_data(client, data):
        client.send(data.encode("utf-8"))
        logging.info("Sending datas")
        client.shutdown(socket.SOCK_STREAM)
        logging.info("Closed connection")

    def message(user, msg):
        data = user.pseudo + "(" + user.nom + "_" + user.prenom + "_" + str(user.age) + ")" + ": " + msg
        logging.info(" : {%s}" ,data)
        return data

def main(user, msg):
    client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        IRC_client.__init__(client)
    except ValueError:
        logging.error("Problem during connection to server")
    message = IRC_client.message(user, msg)
    IRC_client.Sending_data(client, message)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--message", help="The message will be sent to the server")
    parser.add_argument("-u", "--username", help="Username to display")
    parser.add_argument("-ln", "--last-name", help="Last name to display")
    parser.add_argument("-fn", "--first-name", help="Name to display")
    parser.add_argument("-a", "--age", help="Age to display", type=int)
    args = parser.parse_args()
    msg = args.message
    logging.info("Arguments: {%s}", args)
    user = compte(args.username, args.last_name, args.first_name, args.age)
    main(user, msg)