# -*- coding: utf-8 -*-

from unittests.employee.employee import Employee

employee = Employee('Джураев', 'Алишер', 5000)
print(employee.give_raise())
print(employee.give_raise(2000))
