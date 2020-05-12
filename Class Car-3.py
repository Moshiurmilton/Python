class Car:
    def __init__(self, n, c):
        self.name = n
        self.color = c

    def start(self):
        print("Starting the engine")

car = Car("Corolla", "White")
car.year = 2020
print(car.name, car.color, car.year)
