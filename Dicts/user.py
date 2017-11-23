# -*- coding: utf-8 -*-

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print ('===================')
for name in favorite_languages.keys():
    print(name.title() + ", thank you for taking the poll.")

print ('===================')
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print ('===================')
print("The following languages have been mentioned:")
for language in sorted(favorite_languages.values()):
    print(language.title())

print ('===================')
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
