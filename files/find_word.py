# -*- coding: utf-8 -*-

filename = 'txt/find_word.txt'


def try_ot_read_file(filename):
    try:
        with open(filename) as file_object:
            file_content = file_object.readlines()
    except FileNotFoundError:
        pass
        # print('File ' + filename + ' not found')
    else:
        return file_content


lines = try_ot_read_file(filename)

word_count = 0
counted_word = 'the'

for line in lines:
    word_count += int(line.lower().count(counted_word))

print(word_count)
