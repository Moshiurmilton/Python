class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
first = Vector2D(5, 7)
sec = Vector2D(3, 9)
res = first + sec
print(res.x)
print(res.y)
