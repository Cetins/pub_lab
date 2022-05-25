class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
        
    def increase_till(self, amount):
        self.till += amount

    def sell_drink(self, drink_price):
        self.till += drink_price
        return drink_price