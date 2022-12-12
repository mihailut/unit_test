class Mini_Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return sum([self.a, self.b])

    def dif(self):
        return self.a - self.b

    def multi(self):
        return self.a * self.b

    def divi(self):
        return self.a / self.b
