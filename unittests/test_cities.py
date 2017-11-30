import unittest
from unittests.city_functions import get_city_country


class CityTestCase(unittest.TestCase):
    def test_get_city_country(self):
        city_country_name = get_city_country('mocsow', 'russia')
        self.assertEqual(city_country_name, 'Mocsow Russia')

    def test_get_city_country_populations(self):
        city_country_name = get_city_country('mocsow', 'russia', '50000')
        self.assertEqual(city_country_name, 'Mocsow Russia — 50000')

if __name__ == '__main__':
    unittest.main()
