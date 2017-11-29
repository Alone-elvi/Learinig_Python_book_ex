# -*- coding: utf-8 -*-

file_to_read = 'txt/guest_book.txt'
file_to_write = 'txt/why_do_you_like_programming.txt'

with open(file_to_read) as file_object_read:
    lines = file_object_read.readlines()
    for line in lines:
        question = input('Hello '+line+' type why do you like programming (or Q/q to quit) : ')
        if question == 'Q' or question =='q':
            break
        else:
            with open(file_to_write, 'a') as file_object_write:
                file_object_write.write(question)

