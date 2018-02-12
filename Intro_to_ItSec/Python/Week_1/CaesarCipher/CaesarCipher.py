#!/bin/python

import json


def main():
    print("Hello, there!")

    choice = int(input("\n1) Encrypt message\n2) Decrypt message\n3) Show log\n\n0) Exit\n\n> "))

    if choice == 1:
        clear_text = input("Write clear-text message: ")
        key = int(input("Please type in the key: "))
        print(encrypt(clear_text, key))
    elif choice == 2:
        cipher_text = input("Write encrypted message: ")
        key = int(input("Please type in the key: "))
        print(decrypt(cipher_text, key))
    elif choice == 3:
        show_log()
    elif choice == 0:
        print("Exiting...")
        exit(0)


def encrypt(clear, key):
    tmp = ""
    for l in clear:
        nl = chr(ord(l) + key)
        tmp = tmp + nl
    
    save_log(clear, tmp, key, "Encrypt")
    return tmp


def decrypt(cipher, key):
    tmp = ""
    for l in cipher:
        nl = chr(ord(l) - key)
        tmp = tmp + nl

    save_log(cipher, tmp, key, "Decrypt")
    return tmp


def save_log(text, result, key, mode):
    string = [{"Before": text,
        "After": result,
        "Key": key,
        "Mode": mode}]
    
    try:
        with open("ciphers.json", "w") as f:
            json.dump(string, f)
    except:
        print("save_log: Failed.")


def show_log():
    try:
        with open("ciphers.json") as f:
            print(json.load(f))
    except:
        print("show_log: failed")


main()

