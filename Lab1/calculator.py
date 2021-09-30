import lab1 as l

class FooCalculator:

    def __init__(self):
        pass
    
    def sum(self, m, n):
        return l.sum(m, n)

    def divide(self, m, n):
        return l.divide(m, n)


c = FooCalculator()
print(c.sum(2,2))
