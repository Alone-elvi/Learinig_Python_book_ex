# -*- coding: utf-8 -*-

guests = ['Obama', 'Trump', 'Reign', 'Putin', 'Von Braun']


def print_list_of_guests(guests):
    print ('List of guests:')
    for item in guests:
        print ('\t ' + item)


print_list_of_guests(guests)
print ('-------------------------')
print (guests[3] + ' can\'t meet us')

guests[3] = 'Medvedev'

guests.insert(0, 'Lavrov')
guests.insert(4, 'Karimov')
guests.append('Lopirieva')
print_list_of_guests(guests)

i = len(guests)
while i != 2:
    popped_item = guests.pop()
    print('Mr. ' + popped_item + ' we are very sorry, but ou can\'t come to us dinner.')
    i = i - 1

print_list_of_guests(guests)
del guests[0:]

print(guests)