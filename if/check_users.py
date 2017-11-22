# -*- coding: utf-8 -*-

current_users = ['JOHN', 'jorge', 'jim', 'jimmy', 'joplin', 'joshua']

new_users = ['javelin', 'juk', 'jimmy', 'john', 'joanna']

for user in current_users:
    if user.lower() in new_users:
        print (user.lower().title() + ' you must take another name')
