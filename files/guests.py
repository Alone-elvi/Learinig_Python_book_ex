# -*- coding: utf-8 -*-

filename = 'txt/guest_book.txt'

with open(filename, 'a') as file_object:
    while True:
        question = input('Type your name or \"Q\" or \"q\" to Exit : ')
        if question == 'Q' or question == 'q':
            break
        else:
            question = "Hello " + question + "\n"
            file_object.write(question)
