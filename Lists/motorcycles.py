# -*- coding: utf-8 -*-

motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)

motorcycles[0] = 'ducati'
print (motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print (motorcycles)

del motorcycles[-1]
print (motorcycles)

popped_motorcycles = motorcycles.pop(-2)
print (motorcycles)
print (popped_motorcycles)

motorcycles.remove('ducati')
print(motorcycles)
