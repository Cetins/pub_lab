class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
        
    def increase_till(self, amount):
        self.till += amount
        
    def check_age(self, age):
        if age >= 18:
            return True
        else:
            return False

    def sell_drink(self, drink, customer):
        if self.check_age(customer.age):
            self.till += drink.price
            customer.buy_drink(drink.price, drink.alcohol_level)
            return drink.price