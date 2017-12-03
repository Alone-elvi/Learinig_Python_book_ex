# -*- coding: utf-8 -*-

class Privileges:
    def __init__(self, privileges=0):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)
