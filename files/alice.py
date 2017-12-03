# -*- coding: utf-8 -*-
import urllib.request


def count_words(filename):
    try:
        with urllib.request.urlopen(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        # pass
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    except Exception as e:
        pass
        # print(e)

    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
              " words.")

filenames = ['http://syncertech.com/xduoo-x10-hi-fi-audiopleer-s-topovym-zhelezom-i-ochen-priyatnym-tsennikom/',
             'http://syncertech.com/xduoo-x3-novyj-hit-portativnogo-zvuka-real/',
             'moby_dick.txt',
             'little_women.txt']
for filename in filenames:
    count_words(filename)



