import math

# Задача-1: Написать класс для фигуры-треугольника,
# заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

# Пример использования класса треугольника:


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def length(p1, p2):
        length = math.sqrt((p1[0] - p2[0])**2 +
                             (p1[1] - p2[1])**2)
        return length

    def height_a(self):
        return 2 * self.square / self.length(self.a, self.b)

    def height_b(self):
        return 2 * self.square / self.length(self.b, self.c)

    def height_c(self):
        return 2 * self.square / self.length(self.a, self.c)

    def perimeter(self):
        p = self.length(self.a, self.b) + self.length(self.a, self.c) + \
            self.length(self.b, self.c)
        return p

    @property
    def square(self):
        return math.fabs((self.a[0]-self.c[0])*(self.b[1]-self.c[1]) -
                         (self.b[0] - self.c[0])*(self.a[1] - self.c[1])) * 1/2

    def __str__(self):
        return "Triangle with coordinats: {} {} {}".format(self.a,
                                                           self.b,
                                                           self.c)


tr_1 = Triangle((1, 2), (7, 9), (5, 0))
print(tr_1)
print('Площадь:', tr_1.square)
print('Высота к стороне a:', tr_1.height_a())
print('Высота к стороне b:', tr_1.height_b())
print('Высота к стороне c:', tr_1.height_c())
print('Периметр:', tr_1.perimeter())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы для:
#  - проверки, является ли фигура равнобочной трапецией;
#  - вычисления: длины сторон, периметр, площадь.

# Пример использования класса трапеции:

class Trapezoid:
    pass

trap_1 = Trapezoid((0, 0), (1, 2), (3, 2), (4, 0))
trap_2 = Trapezoid((0, 0), (1, 2), (3, 2), (6, 0))
traps = [trap_1, trap_2]

for trap in traps:
    print(trap)
    if trap.is_isosceles():
        print('Равнобочная')
    else:
        print('Неравнобочная')    
    print('Длины сторон:', trap.sides())
    print('Площадь:', trap.square())
    print('Периметр:', trap.perimeter())
