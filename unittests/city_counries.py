# -*- coding: utf-8 -*-

from unittests.city_functions import get_city_country

print("Enter 'q' at any time to quit.")
while True:
    city = input("\nPlease give me a city name: ")
    if city == 'q':
        break
    country = input("\nPlease give me a country name: ")
    if country == 'q':
        break

    formatted_data = get_city_country(city, country)
    print("\tYour city and country is : " + formatted_data + '.')