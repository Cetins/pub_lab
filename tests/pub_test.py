import unittest
from src.drink import Drink
from src.pub import Pub
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100, "Martini")
        self.drink = Drink("Martini", 7, 45)
        self.customer1 = Customer("Paul Smith", 100, 80, 60)
        self.customer2 = Customer("Jane Fonda", 150, 16, 0)
        self.customer3 = Customer("Oscar Wilde", 80, 21, 20)
        
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
    
    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)
        
    def test_increase_till(self):
        self.pub.increase_till(50)
        self.assertEqual(150, self.pub.till)

    def test_sell_drink(self):
        self.pub.sell_drink(self.drink, self.customer1)
        self.assertEqual(107, self.pub.till)
        self.assertEqual(93, self.customer1.wallet)

    def test_check_age__True(self):
        age = self.customer1.age
        self.assertEqual(True, self.pub.check_age(age))

    def test_check_age__False(self):
        age = self.customer2.age
        self.assertEqual(False, self.pub.check_age(age))
