# -*- coding: utf-8 -*-

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'al': 'php',

}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
