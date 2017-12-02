# -*- coding: utf-8 -*-

import unittest
from unittests.employee.employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('Джураев', 'Алишер', 5000)
        self.e_raise = 2000
        self.response = [10000, 7000]

    def test_gave_default_raise(self):
        # self.employee.give_raise()
        self.assertEqual(self.response[0], self.employee.give_raise())

    def test_give_custom_raise(self):
        # self.employee.give_raise(2000)
        self.assertEqual(self.response[1], self.employee.give_raise(self.e_raise))


if __name__ == 'main':
    unittest.main()
