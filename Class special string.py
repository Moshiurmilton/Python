class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(self.cont)     # I changed other.cont to self.cont as a is bigger than b below.
        return "\n".join([self.cont,  line, other.cont])
a = SpecialString("Moshiur")
b = SpecialString("Rahman")
print(a / b)
