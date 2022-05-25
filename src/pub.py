class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
        
    def increase_till(self, amount):
        self.till += amount

    def sell_drink(self, drink_price, customer):
        self.till += drink_price
        customer.buy_drink(drink_price)
        return drink_price