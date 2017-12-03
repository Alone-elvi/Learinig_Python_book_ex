# -*- coding: utf-8 -*-


def get_city_country(city, country, population=''):
    """Ввод и форматирования города, страны и населения"""
    if population:
        return (city + ' ' + country + ' — ' + population).title()
    else:
        return (city + ' ' + country).title()
