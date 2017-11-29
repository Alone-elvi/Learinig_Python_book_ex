# -*- coding: utf-8 -*-
from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


sides_dict = [6, 10, 20]
for sid in range(3):
    die = Die(sides_dict[sid])
    print(sid+1, "<===================")
    for item in range(10):
        print(str(die.roll_die()))
