import unittest
from src.drink import Drink
from src.pub import Pub
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100, [])
        self.drink1 = Drink("Martini", 7, 45, 11)
        self.drink2 = Drink("Beer", 3, 45, 32)
        self.drink3 = Drink("Whiskey", 20, 45, 3)
        self.drinks_stock = [self.drink1, self.drink2, self.drink3]
        self.customer1 = Customer("Paul Smith", 100, 80, 60)
        self.customer2 = Customer("Jane Fonda", 150, 16, 0)
        self.customer3 = Customer("Oscar Wilde", 80, 21, 20)
        self.food = Food("Burger", 15, 50)
        
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
    
    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)
        
    def test_increase_till(self):
        self.pub.increase_till(50)
        self.assertEqual(150, self.pub.till)

    def test_sell_drink(self):
        self.pub.sell_drink(self.drink1, self.customer3)
        self.assertEqual(107, self.pub.till)
        self.assertEqual(73, self.customer3.wallet)
        self.assertEqual(65, self.customer3.drunkness)
        self.assertEqual(10, self.drink1.stock)

    def test_check_age__True(self):
        age = self.customer1.age
        self.assertEqual(True, self.pub.check_age(age))

    def test_check_age__False(self):
        age = self.customer2.age
        self.assertEqual(False, self.pub.check_age(age))

    def test_check_drunkness__True(self):
        drunkness = self.customer1.drunkness
        self.assertEqual(False, self.pub.check_drunkness(drunkness, self.drink1))

    def test_check_drunkness__False(self):
        drunkness = self.customer3.drunkness
        self.assertEqual(True, self.pub.check_drunkness(drunkness, self.drink1))
 
    def test_sell_food(self):
        self.pub.sell_food(self.customer1,self.food)
        self.assertEqual(115, self.pub.till)
        self.assertEqual(85, self.customer1.wallet)
        self.assertEqual(10, self.customer1.drunkness)
        
    def test_add_drink(self):
        self.pub.add_drink(self.drinks_stock)
        self.assertEqual(self.pub.drinks, self.drinks_stock)

    def test_stock_value(self):
        self.pub.add_drink(self.drinks_stock)
        stock = self.pub.stock_value(self.pub.drinks)
        self.assertEqual(233, stock)