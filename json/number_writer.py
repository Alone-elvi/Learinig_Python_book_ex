# -*- coding: utf-8 -*-
import json

filename = '../files/txt/numbers.json'

numbers = [2, 3, 5, 7, 11, 13]
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
