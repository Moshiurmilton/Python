class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
    
    @property # Now code below is read only.
    def pineapple_allowed(self):
        return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True # This line will not be executed. because @property makes pineapple_allowed attribute read only.
