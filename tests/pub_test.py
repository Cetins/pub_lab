import unittest
from src.drink import Drink
from src.pub import Pub
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100, "Martini")
        self.drink = Drink("Martini", 7)
        self.customer = Customer("Paul Smith", 100)
        
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
    
    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)
        
    def test_increase_till(self):
        self.pub.increase_till(50)
        self.assertEqual(150, self.pub.till)

    def test_sell_drink(self):
        self.pub.sell_drink(7)
        self.assertEqual(107, self.pub.till)

    