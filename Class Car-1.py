#class Car:
#    name = "Premio"
#    color = "white"
#
#    def start():
#        print("Starting the engine")


#print("Name of the car:", Car.name)
#print("Color:", Car.color)

#Car.start()
# উপরের প্রোগ্রামটিকে বিভিন্ন ভাবে মোডিফাই করে দেখি।

#class Car:
#    def __init__(self, name, color):
#        self.name = name
#        self. color = color
        
#    def start(self):
#        print("Starting the engine")

#Car.name = "Corolla"
#Car.color = "Black"
#print("Name of the car:", Car.name)
#print("Color:", Car.color)

#Car.start("Corolla")

class Car:
    def __init__(self, n, c):
        self.name = n
        self.color = c

    def start(self):
        print("name: ", self.name)
        print("color: ", self.color)
        print("Starting the engine")

my_car = Car("Corolla", "White")
my_car.start()
