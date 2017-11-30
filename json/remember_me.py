# -*- coding: utf-8 -*-

import json

# Программа загружает имя пользователя, если оно было сохранено ранее.
# В противном случае она запрашивает имя пользователя и сохраняет его.

filename = '../files/txt/username.json'


def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Запрашивает новое имя пользователя."""
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def check_usrname(username):
    checking_true = input("Does you name is "+username+" ? If yes, press any key. If not type \"n\" : ")
    if checking_true == "n":
        get_new_username()

def greet_user():
    """Приветствует пользователя по имени."""
username = get_stored_username()
if username:
    print("Welcome back, " + username + "!")
    check_usrname(username)
else:
    username = get_new_username()

greet_user()
