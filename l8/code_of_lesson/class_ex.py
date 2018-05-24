

class Mul():
    ''' Умножитель
    '''
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return x * self.n


mul_5 = Mul(5)        
print(mul_5(11))
print(mul_5(111))
print(mul_5(22))