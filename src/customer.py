class Customer:
    def __init__(self, name, wallet, age, drunkness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkness = drunkness

    def buy_drink(self, drink_price, alcohol_level):
        self.wallet -= drink_price
        self.drunkness += alcohol_level
        
    def buy_food(self, food):
        self.wallet -= food.price
        self.drunkness -= food.rejuvenation_level