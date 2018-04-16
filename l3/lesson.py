import sys

from functools import reduce

ls = [1, 2, 3, 4, 5]
ls += 'spisok'
print(ls)

f = open('test.txt')
for line in f:
    print(line, end='')
d = {
    'Иванов': [3, 5, 2, 4, 2, 5],
    'Петров': [4, 5, 4, 4, 3, 5],
    'Сидоров': [5, 5, 5, 5, 5, 5],
    'Черкасов': [4, 5, 3, 4, 4, 5],
    'Пукин': [4, 5, 4, 4, 4, 5],
}
print()
with open('test2.csv', 'w+', encoding = 'cp1251') as f2:
    for fio, marks in sorted(d.items()):
        f2.write(';'.join([fio, ';'.join(str(i) for i in marks)]) + '\n')
    print(f2.tell())

# ternary operator
x = 13
y = 5 if x > 0 else -5
print(y)
x = -13
y = 5 if x > 0 else -5
print(y)

# ternary operator in list comprehension

ls = [x**2 if x%2 == 0 else x/2 for x in range(20)]
print(ls)

# set coprehension

ls = {x**2 if x%2 == 0 else x/2 for x in range(20)}
print(type(ls), ls)

# create dictionary

dict = {str(x): x**2 for x in range(20)}
print(type(dict), dict)

# any amount of arguments: tuple in functioon arguments

def summ(*args, **kwargs):
    s = 0
    for arg in args:
        s += arg
    return '{}, {}, {}, {}, {}'.format(s, type(args), args, type(kwargs), kwargs)

print(summ(5, 7, 9, check=True, maxi=25))

# visible area of the variables

some_var = 44
print('in top = ', some_var)
def some_func():
    some_var = 77
    print('in {} = '.format(sys._getframe().f_code.co_name), some_var)
    def some_sub_func():
        some_var = 88
        print('in {} = '.format(sys._getframe().f_code.co_name), some_var)
    some_sub_func()
    print('after {} = '.format(sys._getframe().f_code.co_name), some_var)
some_func()
print('after {} = '.format(sys._getframe().f_code.co_name), some_var)
print('*' * 40)
some_var = 44
print('in top = ', some_var)
def some_func_nonlocal():
    some_var = 77
    print('in {} = '.format(sys._getframe().f_code.co_name), some_var)
    def some_sub_func_nonlocal():
        nonlocal some_var # !!! change some_var area visibility to upper function some_func_1 area
        some_var = 88
        print('in {} = '.format(sys._getframe().f_code.co_name), some_var)
    some_sub_func_nonlocal()
    print('after {} = '.format(sys._getframe().f_code.co_name), some_var)
some_func_nonlocal()
print('after {} = '.format(sys._getframe().f_code.co_name), some_var)
print('*' * 40)

some_var = 44
print('in top = ', some_var)
def some_func_global():
    global some_var  # change visibility area to global
    some_var = 77
    print('in {} = '.format(sys._getframe().f_code.co_name), some_var)
    def some_sub_func():
        some_var = 88
        print('in {} = '.format(sys._getframe().f_code.co_name), some_var)
    some_sub_func()
    print('after {} = '.format(sys._getframe().f_code.co_name), some_var)
some_func_global()
print('after {} = '.format(sys._getframe().f_code.co_name), some_var)
print('*' * 40)


print('lambda: {}'.format((lambda x,y: x*y)(11, 13)))

# sort by last key
ls = [[2, 4], [3, 2, -1], [1, 5], [6, 9, -50]]

print(sorted(ls, key = lambda x: x[-1]))

# map
print(list(map(lambda x: x**x, range(1, 10))))

# sum, map
print(sum(map(int, '123456')))

# filter
print(list(filter(lambda x: x > 0, [-1, 2, 3, 4, -5])))

# reduce

print(reduce(lambda x, y: x*y, [1, 2, 3, 4]))

#lambda with *args

# x * sum([3,4,5,6])
print((lambda x, *args: x * sum(args))(2, 3, 4, 5, 6))

def bad_append(item, a_list=[]):
    a_list.append(item)
    return a_list

print(bad_append('one'))
print(bad_append('two'))
