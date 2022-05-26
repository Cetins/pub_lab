class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = []
        
        
    
    def add_drink(self, drinks):
        for drink in drinks:
            self.drinks.append(drink)
        return self.drinks
        
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
            drink.stock -= 1
            customer.buy_drink(drink.price, drink.alcohol_level)
            return drink.price

    def sell_food(self, customer, food):
        self.increase_till(food.price)
        customer.buy_food(food)

    def stock_value(self, drinks):
        self.add_drink(drinks)
        stock = 0
        for drink in self.drinks:
            stock += (drink.price * drink.stock)
        return stock