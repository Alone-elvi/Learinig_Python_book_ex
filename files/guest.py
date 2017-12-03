# -*- coding: utf-8 -*-

filename = 'txt/guest.txt'

with open(filename, 'a') as file_object:
    file_object.write(str(input('Say your name: '))+'\n')