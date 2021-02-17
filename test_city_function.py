import unittest
from city_function import *

class CityTestCase(unittest.TestCase):

    def test_city_country_name(self):
        detail = get_formatted_city_country('karachi','Pakistan')
        self.assertEqual(detail,'Karachi, Pakistan')

    def test_city_country_population_name(self):
        detail = get_formatted_city_country('karachi','Pakistan','2000')
        self.assertEqual(detail,'Karachi, Pakistan - Population 2000')

unittest.main()