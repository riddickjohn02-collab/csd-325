
# Name: Robert Cuevas
# Date: November 24, 2026
# Assignment: CSD-325 Module 7 - Unit Tests
# Purpose: Test that the city_country function formats
# city and country names correctly.

import unittest
from city_functions import city_country


class TestCities(unittest.TestCase):

    # Test the city and country formatting.
    def test_city_country(self):
        formatted_city = city_country("Santiago", "Chile")
        self.assertEqual(formatted_city, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()
