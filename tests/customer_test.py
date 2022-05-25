import unittest

from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Paul Smith", 100)

    def test_find_customer_by_name(self):
        self.assertEqual("Paul Smith", self.customer.name)
        
     
        #    customer
        # buy_drink(self, drink):
        #     drink = pub.sell_drinks()
        #     self.wallet -= drink.price
        #     return customer.


        # list = []
        # tuple = ()