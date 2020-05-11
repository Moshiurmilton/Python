class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def bark(self):
        print("woof!")
        
fido = Dog("Fido", "brown")
print(fido.name)
fido.bark() # Dog.bark(fido) একই ফলাফল দেবে।
