import unittest

from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Paul Smith", 100)

    def test_find_customer_by_name(self):
        self.assertEqual("Paul Smith", self.customer.name)
        
    def test_buy_drink(self):
        self.customer.buy_drink(7)
        self.assertEqual(93, self.customer.wallet)
        