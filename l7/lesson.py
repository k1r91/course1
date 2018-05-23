import datetime
import time
from functools import wraps

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

    @staticmethod
    def create_square(point, w):
        return Rectangle(point, w, w)

    def __str__(self):
        return 'Прямоугольник ({}, {}), ширина = {}, высота = {}'.format(self.x, self.y, self.w, self.h)

    def __repr__(self):
        return 'x={}, y={}, w={}, h={}'.format(self.x, self.y, self.w, self.h)

    def __len__(self):
        return 2 * (self.w + self.h)

    def __add__(self, other):
        r = Rectangle((self.x, self.y), self.w+other.w, self.h+other.h)
        return r


class Romb(Rectangle):
    _count = 0

    def __init__(self, point, w):
        super().__init__(point, w, w)
        Romb._count += 1

# DRY - don't repeat yourself

rect1 = Rectangle([0, 0], 10, 5)
rect2 = Rectangle([5, 5], 20, 10)
print(rect1.square)
print(rect1)
print(rect1._count)
print(Rectangle.get_count())
romb = Romb((0, 0), 13)
romb1 = Romb((0, 0), 14)
rect3 = rect1 + rect2
print(rect3)
print(romb._count)
print(Romb.get_count())
print(Rectangle.get_count())
print(Rectangle.create_square((0, 0), 25))
print(Rectangle.get_count())
print(Romb.get_count())
print(datetime.datetime.today())
print(type(datetime.datetime.today()))
print(datetime.datetime(year=2018, month=5, day=22))
rects = {1: rect1, 2: rect2, 3: romb, 4: romb1}
print(rects)
print('Периметр прямоугольника {} = {}'.format(rect1, len(rect1)))
print(rect1.__len__())


def log(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        res = func(*args, **kwargs)
        print('{}({}) = {}'.format(func.__name__, args, res))
        return res
    return decorated


def time_it(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        delta = time.time() - t1
        print('Function {} worked {} seconds'.format(func.__name__, delta))
        return res
    return decorated


@time_it
@log
def my_sum(a, b):
    res = a + b
    return res
# my_sum = log(my_sum)
print(my_sum(3, 4))
print(help(my_sum))


MAXI = 10000


@time_it
def str_concat(maxi):
    s = ''
    for i in range(maxi):
        s = s + ' ' + str(i)
    return s


@time_it
def str_join(maxi):
    nums = []
    for i in range(maxi):
        nums.append(str(i))
    return ' '.join(nums)

str_join(MAXI)
str_concat(MAXI)


class Reverse:

    def __init__(self, data):
        self.data = list(data)
        self.index = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if self.index >= 0:
            return self.data[self.index]
        else:
            raise StopIteration

rever = Reverse('Python - my love')
for r in rever:
    print(r)

# delegation


class Wrapper:
    def __init__(self, obj):
        self.wrapped = obj

    def __getattr__(self, item):
        print('Trace:', item)
        return getattr(self.wrapped, item)

    def __add__(self, other):
        if isinstance(self.wrapped, list) and isinstance(other, list):
            return self.wrapped + other

    def __getitem__(self, item):
        ''' support indexing '''
        if isinstance(self.wrapped, list):
            return self.wrapped[item]

ls = Wrapper([1, 2, 3])
ls.append(4)
d = ls.pop()
print(ls[2])
ls += [5, 6]
print(ls)
print(len(ls))
d = Wrapper({1: 55, 2: 66})
print(d.keys())
print(d.values())