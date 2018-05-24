import time
from functools import wraps


# decorator with params
def sleep(sec):
    def decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            t1 = time.sleep(sec)
            res = func(*args, **kwargs)
            print('Function {} was sleeping {} seconds'.format(func.__name__, sec))
            return res
        return decorated
    return decorator


# decorator
def time_it(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        delta = time.time() - t1
        print('Function {} was working {} seconds'.format(func.__name__, delta))
        return res
    return decorated


@time_it
@sleep(.2)
def my_sum(a, b):                 #time_it(sleep(1)(my_sum(a,b)))
    return a + b


class Mul:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return x * self.n


class Sleep:
    def __init__(self, n):
        self.n = n

    def __call__(self, func):
        def decorated(*args, **kwargs):
            time.sleep(self.n)
            print("Function {} was sleeping {} seconds".format(func.__name__, self.n))
            res = func(*args, **kwargs)
            return res
        return decorated


# class as decorator
@Sleep(.2)
def my_sum2(a, b):
    return a + b


class Wrapper:
    def __init__(self, obj):
        self.wrapped = obj

    def __getattr__(self, item):
        print('Log:', item)
        return getattr(self.wrapped, item)

    def __getitem__(self, item):
        if hasattr(self.wrapped, '__getitem__'):
            return self.wrapped[item]


if __name__ == '__main__':
    print(my_sum(5, 11))
    print(time_it(sleep(1)(my_sum(5,11))))
    mul_5 = Mul(5)
    print(mul_5(11))
    print(my_sum2(2, 8))
    wrapped_list = Wrapper([1, 2, 3, 4])
    print(wrapped_list[1])
    wrapped_list.append(999)