import time
(lambda x, y, z: print('*-' + x.replace(y, z) + '-*'))\
    ('I like Python', 'Python', 'ice-cream')
print(time.time())


def work(x):
    tt = str(time.time())
    if tt.split('.')[0][-1] == '0' and int(x) > 5:
        res = 'Arbaiten'
    else:
        res = '2x Arbaiten'
    return res * int(x)

print(work('6'))
print(list(map(work, '123456')))
print(list(map(print, '12345678')))


def avg(ls):
    return (sum(ls) / len(ls)) * 2
print(avg([1, 2, 3, 4, 5, 6]))

# create dynamic functions

funcs = []
for i in range(7):
    funcs.append(lambda x=i: '*' * x)
for f in funcs:
    print(f())


class TastySoup:

    def __init__(self, ingr=None, rules=None):
        '''
        ingr - list of all ingridients
        rule - list of all rules
        :param ingr:
        :param rule:
        '''
        self.x = 13
        if ingr is not None:
            self.water = ingr[0]
            self.potato = ingr[1]
            self.onion = ingr[2]
        else:
            self.water = 'Вода из крана'
            self.potato = 'Проросшая картошка'
            self.onion = 'Простой лук'
        self.rules = rules

    def vzuhhh(self):
        print('Готовлю суп...')
        print(self.water, self.potato, self.onion)
        if self.rules is not None:
            for func in self.rules:
                print(func())
                for i in range(10):
                    time.sleep(.1)
                    print('*', end='')
        else:
            for func in ['Налить', 'Порезать', 'Вскипятить', 'Позвать жену']:
                print(func)
                for i in range(5):
                    time.sleep(.1)
                    print('*', end='')
ingridients = ['ключевая вода', 'деревенская картошка', 'свежий лук']
soup = TastySoup(ingridients)
soup.vzuhhh()
#view lesson at 2:24