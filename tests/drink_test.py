import unittest

from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Martini", 7, 45, 11)

    def test_drink_has_name(self):
            self.assertEqual("Martini", self.drink.name)