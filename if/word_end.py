# -*- coding: utf-8 -*-

numbers = [num for num in range(1, 10)]
ending = ''
for item in numbers:
    if item == 1:
        ending = 'st'
    elif item == 2:
        ending = 'nd'
    elif item == 3:
        ending = 'rd'
    else:
        ending = 'th'
    print (str(item) + str(ending))
