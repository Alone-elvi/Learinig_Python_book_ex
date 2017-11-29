# -*- coding: utf-8 -*-

filename = 'txt/learinig_python.txt'

lines_out = []

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)
    file_object.seek(0)
    lines = file_object.readlines()
    file_object.seek(0)
    lines_out = file_object.readlines()
    for line in lines:
        print(line)

for line in lines_out:
    print(line.replace('Python', 'C'))