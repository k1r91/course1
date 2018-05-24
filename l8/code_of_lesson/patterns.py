
import json

class Wall():
    pass


class House():
    pass


class HouseFabric():
    def __init__(self, *args):
        pass

    def make_house(self):   
        pass
        pass 
        return House(Wall(), Basement(), Roof())


class WorkerBuilder:
    def __init__(self, attr_dict):
        for key, value in attr_dict.items():
            setattr(self, key, value)

    def make_wall(self, material):
        return Wall(material)

    def make_roof(self, *args):
        return Roof(*args)    

    def make_basement(self, *args):
        return Basement(*args)    

    def __str__(self):
        if hasattr(self, 'name') and hasattr(self, 'surname'):
            return '{0} {1[0]}.'.format(self.surname, self.name)
        else:
            return 'Просто Рабочий'            


# with open('data.json', encoding='utf-8') as f:
#     for line in f:
#         data = json.loads(line.strip())
#         worker = WorkerBuilder(data)
#         # print(data, type(data))
#         print(worker, worker.__dict__)



class Wrapper():
    def __init__(self, obj):
        self.wrapped = obj

    def __getattr__(self, attrname):
        print('Log: ', attrname)
        return getattr(self.wrapped, attrname)

    def __str__(self):
        return str(self.wrapped)  

    def __getitem__(self, index):
        if hasattr(self.wrapped, '__getitem__'):
            if self.wrapped[index] == 11:
                return 5555
            else:
                return self.wrapped[index]    



x = Wrapper([11, 22, 33]) 
x.append(44)

x.insert(2, 777)

print(x[0])

# x = Wrapper({11:'adsf', 22:'adsf', 33:'werq'})
# print(x.keys()) 



class WinnerException(Exception):
    """
        Исключение для игрока
    """
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return 'Игрок {} выиграл миллион!'.format(self.name)


cards = [[1,2,3], [4,6,7,], [], [7,8,9,90,45]]        
while True:
    try:
        for card in cards:
            if not card:
                raise WinnerException('Человек')
    except WinnerException as we:
        print(we)            
        break

print('Game Over!')        


        