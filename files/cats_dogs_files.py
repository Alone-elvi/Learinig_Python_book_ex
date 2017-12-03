# -*- coding: utf-8 -*-

dogs_file = 'txt/dogs.txt'
cats_file = 'txt/cats.txt'


def try_ot_read_file(filename):
    try:
        with open(filename) as file_object:
            file_content = file_object.read()
    except FileNotFoundError:
        pass
        # print('File ' + filename + ' not found')
    else:
        print(file_content)


try_ot_read_file(dogs_file)
try_ot_read_file(cats_file)
