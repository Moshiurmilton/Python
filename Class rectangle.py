class Rectang:
    def __init__(self, a):
        self.a = a
    def __mul__(self, other):
        c = self.a * other.a
        print("Are of Rectangle:", c)
        
width = Rectang(20)
height = Rectang(10)
width * height
