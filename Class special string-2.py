class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont)+1):     # I changed other.cont to self.cont as a is bigger than b below.
            result = other.cont[:index] + ">" + self.cont
            result = result + ">" + other.cont[:index]
            print(result)
a = SpecialString("Moshiur")
b = SpecialString("Rahman")
a > b
