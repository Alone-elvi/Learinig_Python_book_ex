# -*- coding: utf-8 -*-

filename = 'alice.txt'

try:
    with open(filename) as file_object:
        print(file_object.read())
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)