
import time

class Food():
    def __init__(self, name, ingr):
        self.name = name
        self.ingredients = ingr[:]

    def vzuhhh(self):
        print('Не знаю как готовить: ', self.name)

    def allo_pizza(self):
        print('Заказываем пиццу!')   

    def __str__(self):
        return 'Просто еда: {}'.format(self.name)
            
class Smile():
    def smile(self):
        print('Я умею улыбаться! :))))  Гыыыы')

    def allo_pizza(self):
        print('Не будет вам пиццы!')   


class Drink(Food):
    """docstring for ClassName"""
    def __init__(self, name):
        super().__init__(name, ['вода'])

    def __str__(self):
        return 'Напиток: {}'.format(self.name)          


class Beer(Drink):
    """Пиво"""
    def __init__(self, ingr, bochka):
        super().__init__('Пиво')          # super(ClassName, self).__init__()
        self.bochka = bochka
        self._vobla = 'Вобла...'

    def vzuhhh(self):
        print('Варись-варись', self.name)
        print('Теперь можно пить') 

    def friday(self):
        print('Пятницаааа! Ура!', self.name * 4)       

    def __str__(self):
        temp = super().__str__()
        return 'Вкусный' + temp
        

class TastySoup(Food, Smile):      # 
    ''' Документация на класс ВкусныйСуп
    '''

    count = 0

    def __init__(self, ingr=None, rules=None):
        ''' ingr - список ингедиенто
            rules - список функций готовки
        '''
        super().__init__('Суууп', ingr)
        self._x = 13
        self.__secure_x = 99
        self._state = 0
        '''
            0 - еще не начал готовить
            1 - готовлю
            2 - приготовил
        '''    
        if ingr is not None:
            self.water = ingr[0]
            self.potato = ingr[1]
            self.onion = ingr[2]
        else:
            self.water = 'Вода из крана'
            self.potato = 'Проросшая картоха'
            self.onion = 'простой лук'     
        self.rules = rules
        TastySoup.count += 1         # self.count = self.count + 1

    def vzuhhh(self):
        print('Готовлю суп...')
        self._state += 1
        print(self.water, self.potato, self.onion)
        if self.rules is not None:
            for func in self.rules:
                print(func())
                for i in range(10):
                    time.sleep(0.1)
                    print('*', end='')    
        else:
            # self.state += 1
            for func in ['Налить', 'Порезать', 'Вскипятить', 'Позвать жену...']:
                print(func)
                if func == 'Порезать':
                    break
                for i in range(5):
                    print('*', end='')    
                    time.sleep(0.1)
            else:        
                print('Ваш суп по умолчанию готов')     
                self._state += 1

    @property            
    def cost(self):        
        # print('Готовлю из того, что есть...')           
        return self.potato * 30 + self.onion * 25
                    

food = Food('Курица', [1,2,3])


ingr = [1, 1, 0.200]
soup = TastySoup(ingr)

ingr = ['солод', 'хмель', 'вода']
beer = Beer(ingr, 'Большая бочка')
# beer.friday()

print(food)
print(beer)

# ingr = ['Пиво', 'Чипсы', 'кольца кальмара']
ingr = [5, 3, 1]
soup_2 = TastySoup(ingr)

print(dir(soup))

soup.vzuhhh()
soup.smile()



soup.allo_pizza()

# print(soup._state)
# soup_2.vzuhhh()

# print(soup.potato)
# soup.potato = 'Картошка из супермаркета'
soup.p0tat0 = 'Картошка из супермаркета'
soup._x = 77
# print(soup.potato)

soup.beer = 'Жигули'

print('Всего супов: ', TastySoup.count, soup.count, soup_2.count)

# print(dir(soup))
# print(dir(soup_2))

# print(soup.__dict__)
# soup._TastySoup__secure_x = 0
# print(soup.__dict__)

print(soup.cost)
print(soup_2.cost)





'''

soup = {"potato":0, "cheeze":0, "boil":30}
soup_2 = {"potato":10, "cheeze":2, "boil":120}

kisel = {'berry':'klukva', 'krahmal':0.5, "boil":30}
wine = {'wine':'klukva', "boil":30}


def boil_soup(soup):
    print('Готовлю суп из:', soup)


def boil_kisel(drink):
    print('Готовлю напиток из:', drink)
    print('Ягода:', drink['berry'])
    print('Крахмал:', drink['krahmal'])
    print('Варить:', drink['boil'])


def boil_wine(drink):
    print('Готовлю напиток из:', drink)
    print('Вино:', drink['berry'])
    print('Варить:', drink['boil'])




boil_soup(soup)
boil_soup(soup_2)

boil_drink(kisel)

'''