# -*- coding: utf-8 -*-

str_1 = 'String_1'
str_2 = 'String_2'
num_1 = 10
num_2 = 20
num_3 = 31

list_1 = ['String_1', 'String_2', 10, 20, 31]
print(str_1 == str_2)
str_2 = 'String_1'
print(str_1 == str_2)
str_2 = 'String_2'
print(str_1.lower() == 'string_1')

if num_2 > num_1:
    print(True)
else:
    print(False)

if num_2 < num_1:
    print(True)
else:
    print(False)

if num_2 >= num_3:
    print(True)
else:
    print(False) 

if num_2 <= num_3:
    print(True)
else:
    print(False)

if (num_1 < num_2 < num_3) or num_3 < num_1:
    print(True)

if num_1 in list_1:
    print(True)

if 50 not in list_1:
    print(True)
