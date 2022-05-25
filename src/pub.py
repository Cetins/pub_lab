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

    def check_drunkness(self, drunkness, drink):
        if drunkness + drink.alcohol_level > 100:
            return False
        else:
            return True

    def sell_drink(self, drink, customer):
        if self.check_age(customer.age) and self.check_drunkness(customer.drunkness, drink):
            self.till += drink.price
            customer.buy_drink(drink.price, drink.alcohol_level)
            return drink.price

    