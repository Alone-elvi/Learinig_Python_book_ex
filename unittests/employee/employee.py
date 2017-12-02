# -*- coding: utf-8 -*-


class Employee:
    def __init__(self, f_name, s_name, gain):
        self.f_name = f_name
        self.s_name = s_name
        self.gain = gain

    def give_raise(self, e_raise=5000):
        gain = self.gain + e_raise
        return gain
