from classes.restorant import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors=[]):
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def print_flavors(self):
        if self.flavors:
            for item in self.flavors:
                print(str(item))
        else:
            print('No flavors there')



ic1 = IceCreamStand('Re', 'Pr')

ic1.describe_restaurant()
ic1.print_flavors()
