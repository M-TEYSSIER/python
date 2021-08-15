#!/usr/bin/env python3
# -*- coding: utf-8

from compte import compte
import socket
import argparse
import logging

logging.basicConfig(level=logging.DEBUG)

SOCKET_LINK = "/home/maxime/irc.socket"

class IRC_client:
    def __init__(client):
        try:
            client.connect(SOCKET_LINK)
            logging.info("Established connection with server")
        except:
            logging.error("Connection failed to the server")
    def __close__(client):
        client.shutdown(socket.SOCK_STREAM)
        logging.info("Closed connection")

    def Sending_data(client, data):
        client.send(data.encode("utf-8"))
        logging.info("Sending datas")

    def create_data(args):
        data = "["
        if args.username is not None:
            data += args.username + " "
        if args.last_name is not None:
            data += args.last_name + " "
        if args.first_name is not None:
            data += args.first_name + " "
        if args.age is not None:
            data += str(args.age) + " "
        data = data.rstrip(data[-1]) + "]: "
        if args.message is not None:
            data += args.message
        elif args.message is None:
            data += input(">") 
        logging.info(" : {%s}" ,data)
        return data

def main(args):
    client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        IRC_client.__init__(client)
    except ValueError:
        logging.error("Problem during connection to server")
    try:
        msg = IRC_client.create_data(args)
        IRC_client.Sending_data(client, msg)
    except  KeyboardInterrupt:
        pass
    IRC_client.__close__(client)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--message", help="The message will be sent to the server")
    parser.add_argument("-u", "--username", help="Username to display")
    parser.add_argument("-ln", "--last-name", help="Last name to display")
    parser.add_argument("-fn", "--first-name", help="Name to display")
    parser.add_argument("-a", "--age", help="Age to display", type=int)
    parser.add_argument("-v", "--debug", help("Displays debug's information"))
    args = parser.parse_args()
    logging.info("Arguments: {%s}", args)
    main(args)