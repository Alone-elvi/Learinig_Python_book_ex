# -*- coding: utf-8 -*-
import json

filename = '../files/txt/username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")