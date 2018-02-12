#!/bin/python

import hashlib
import itertools
import socket
import string


def main():
    HOST = "127.0.0.1"
    PORT = 8888
    BUFF = 1024

    sock = socket.socket()
    print('Starting up on {}:{}'.format(HOST, PORT))
    sock.bind((HOST, PORT))

    sock.listen(1)

    while True:
        print("Waiting for connection")
        connection, client_address = sock.accept()

        try:
            while True:
                data = connection.recv(BUFF)

                print("Received {}".format(data))
                if data:
                    crack(data.decode())
                else:
                    print("No more data from {}".format(HOST))
                    break
        finally:
            connection.close()


def crack(uncracked_hash):
    alph = string.ascii_lowercase + string.digits

    for L in range(0, len(alph)):
        for subset in itertools.combinations(alph, L):
            word = ''.join(subset)
            hashed_word = hashlib.md5(word.encode('utf-8')).hexdigest()

            print(hashed_word)

            if uncracked_hash == hashed_word:
                print(word)
            elif word == "999":
                print("stop")
                exit(0)


if __name__ == '__main__':
    main()
