# -*- coding: utf-8 -*-

squares = [value ** 3 for value in range(1, 11)]
print(squares)

# mill = [val for val in range(1, (10**6)+1)]
# print (mill)
# print(min(mill))
# print(max(mill))
# print (sum(mill))

#  Генератор чисел кратных 3
trio = [val * 3 for val in range(3, 30)]
print (trio)

# Create generator of cube :)
cube = [val ** 3 for val in range(2, 10)]
print (cube)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])