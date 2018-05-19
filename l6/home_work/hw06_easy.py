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

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    @staticmethod
    def line_equation(p1, p2):
        coefficient_x = (p2[1] - p1[1]) / (p2[0] - p1[0])
        constant = (p2[0]*p1[1] - p2[1]*p1[0]) / (p2[0] - p1[0])
        return {'x': coefficient_x, 'const': constant}

    def is_isosceles(self):
        len_ac = Triangle.length(self.a, self.c)
        len_bd = Triangle.length(self.b, self.d)
        return len_ac == len_bd

    def sides(self):
        len1 = Triangle.length(self.a, self.b)
        len2 = Triangle.length(self.b, self.c)
        len3 = Triangle.length(self.c, self.d)
        len4 = Triangle.length(self.d, self.a)
        return len1, len2, len3, len4

    @property
    def square(self):
        if self.line_equation(self.a, self.b)['x'] == self.line_equation(self.c, self.d)['x']:
            bases = [(self.a, self.b), (self.c, self.d)]
        else:
            bases = [(self.a, self.d), (self.b, self.c)]
        # ax + by +c = 0
        x1 = bases[1][0][0]
        y1 = bases[1][0][1]
        x2 = bases[1][1][0]
        y2 = bases[1][1][1]
        a = y2 - y1
        b = x2 - x1
        c = x1*y2 - x2*y1
        x0 = bases[0][0][0]
        y0 = bases[0][0][1]
        h = math.fabs(a*x0 + b*y0 + c) / math.sqrt(a**2 + b**2)
        side1 = Triangle.length(bases[0][0], bases[0][1])
        side2 = Triangle.length(bases[1][0], bases[1][1])
        s = h * (side1 + side2) / 2
        return s

    def perimeter(self):
        return sum(self.sides())

    def __str__(self):
        return "Trapezoid with coordinates: {} {} {} {}".format(self.a, self.b, self.c, self.d)

trap_1 = Trapezoid((0, 0), (1, 2), (3, 2), (4, 0))
trap_2 = Trapezoid((0, 0), (1, 2), (3, 2), (6, 0))
trap_3 = Trapezoid((0, 0), (1, 3), (3, 3), (9, 0))
traps = [trap_1, trap_2, trap_3]

for trap in traps:
    print(trap)
    if trap.is_isosceles():
        print('Равнобочная')
    else:
        print('Неравнобочная')    
    print('Длины сторон:', trap.sides())
    print('Площадь:', trap.square)
    print('Периметр:', trap.perimeter())
