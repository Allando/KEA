#!/bin/python

ip = "300.100.123.400"

for i in ip.split("."):
    if int(i) > 255 or int(i) < 0:
        print("fejl: ", i)
