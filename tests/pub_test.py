import unittest

from src.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100)
        
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
    
    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)
        
    def test_increase_till(self):
        self.pub.increase_till(50)
        self.assertEqual(150, self.pub.till)