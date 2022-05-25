import unittest

from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Burger", 15, 50)
    
    def test_food_has_name(self):
        self.assertEqual("Burger", self.food.name)
