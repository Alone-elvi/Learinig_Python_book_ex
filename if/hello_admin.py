# -*- coding: utf-8 -*-

users = ['admin', 'arthur', 'anvar', 'akram', 'akmal', 'adam']

if not users:
    print ('We need to find some users!')
for user in users:
    if user in users[0]:
        print ('Hello ' + user.title() + ', would you like to see a status report?')
    else:
        print ('Hello ' + user.title() + ', thank you for logging in again')