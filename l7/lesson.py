ls = [(i, j) for i in range(5) for j in range(1, 10, 2) if i % j == 1]
print(ls)

x = 1
class c:
    x = 2
    print('2', x)
    def m(self):
        print('3', x)
print('1', x)
i = c()
i.m()

class BaseClass:
    x = 1
    y = 1

class ChildBase(BaseClass):
    x = 111
    y = 111
    # prints self.y because BaseClass == self
    def mix(BaseClass):
        return BaseClass.y
c = ChildBase()
print(c.mix())

class Rectangle:
    _count = 0
    def __init__(self, point, w, h):
        self.x = point[0]
        self.y = point[1]
        self.w = w
        self.h = h
        Rectangle._count += 1

    @classmethod
    def get_count(cls):
        return cls._count

    @property
    def square(self):
        return self.w * self.h

    def __str__(self):
        return 'Прямоугольник ({}, {}), ширина = {}, высота = {}'.format(self.x, self.y, self.w, self.h)

rect1 = Rectangle([0, 0], 10, 5)
rect2 = Rectangle([5, 5], 20, 10)
print(rect1.square)
print(rect1)
print(rect1._count)