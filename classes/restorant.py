# -*- coding: utf-8 -*-


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name.title(), self.cuisine_type.title())

    def open_restaurant(self):
        print('restaurant is open'.title())

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, served):
        self.number_served += served


# restaurant = Restaurant('black jack', 'italian')
# r2 = Restaurant('Моромойка', 'русская')
#
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
#
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
#
# r2.describe_restaurant()
# r2.open_restaurant()
# print(r2.number_served)
# r2.set_number_served(14)
# print(r2.number_served)
# r2.increment_number_served(19)
# print(r2.number_served)
