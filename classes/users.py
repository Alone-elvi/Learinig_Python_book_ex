# -*- coding: utf-8 -*-

from classes.user import User
from classes.admin import Admin
from classes.privilegies import Privileges

# class User:
#     """Пользователь"""
#     def __init__(self, first_name, last_name, age):
#         """Передаём параметры пользователя, Имя, Фамилию и возраст"""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.login_attempts = 0
#
#     def describe_user(self):
#         """Выводим информацию о пользователе"""
#         print('Information about user:\n')
#         print('First name is:' + self.first_name.title())
#         print('Second name is:' + self.last_name.title())
#         print('user is ' + str(self.age) + ' years old.\n')
#
#     def greet_user(self):
#         """Приветствуем пользователя"""
#         print('Hello ' + self.first_name.title() + ' ' + self.last_name.title())
#
#     def increment_login_attempts(self):
#         """Увеличивает колтичество входа пользователя"""
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         """Сбрасывает счётчик посещений"""
#         self.login_attempts = 0



ad1 = Admin('Ivan', 'Pronin', '33', 4)
ad1.privileges.show_privileges()

u1 = User('Kabaeva', 'Alina', 35)
u2 = User('Natasha', 'Kopilova', 41)

u1.greet_user()
u1.describe_user()

u2.greet_user()
u2.describe_user()
u2.increment_login_attempts()
u2.increment_login_attempts()
u2.increment_login_attempts()
u2.increment_login_attempts()
print(u2.login_attempts)
u2.reset_login_attempts()
print(u2.login_attempts)
