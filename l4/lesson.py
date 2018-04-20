import sys
import copy
import itertools
import re
import os
# named slices
D = slice(0, 2)
M = slice(3, 5)
Y = slice(6, 10)
date = '25.01.1987'
print('Day: {} Month: {} Year: {}'.format(date[D], date[M], date[Y]))

# links on objects:

a = 1
b = 1

print('a is b: {}'.format(a is b))

c = 'str'
d = 'str'

print('c is d: {}'.format(c is d))

c = 'str_veryverylong        asdasasd'
d = 'str_veryverylong        asdasasd'

print('c is d: {}'.format(c is d))

# amount of links to object

print(sys.getrefcount(a))
print(sys.getrefcount([23, 56, 2133, 546, 28]))

# links to lists
z = [1, 2, 3]
x = [1, 2, 3]
print(x is z)
print(id(x), id(z))
z = [1, 2, 3]
x = z
print(x is z)
print(id(x), id(z))
z.append(777)
print(x, z)

# copy nested lists

ls1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ls2 = ls1[:]
ls1[1].append(777)  # nested lists are links
print(ls1, ls2)

ls2 = copy.deepcopy(ls1)
ls1[1].append(888)
print(ls1, ls2)

# correct remove from list in for cycle
ls = list(range(10))
# incorrect:
for i in ls:
    if i < 5:
        ls.remove(i)
print(ls)
# correct:
ls = list(range(10))
for i in ls[:]:
    if i < 5:
        ls.remove(i)
print(ls)

# zip function:

print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9, 10])))

# transpose matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list(zip(*matrix)))

# create dictionaries from two lists

keys = ['one', 'two', 'three', 'for']
values = [1, 2, 3, 4]
print(dict(zip(keys, values)))

# create generator


def my_map(func, iterable):
    for i in iterable:
        yield func(i)
m = my_map(int, '123456897234')
print(type(m))


def foo(n):
    yield 'Hello'
    while n > 0:
        yield n
        n -= 1
    yield 'Goodbye'
print(foo(13))
print(list(foo(13)))
for i in foo(13):
    print(i)

def bar(n):
    print('Start of generator')
    yield 'Hello'
    print('Hello world')
    while n > 0:
        yield n
        n -= 1
    yield 'Goodbye'
    print('The end!')
gen = bar(13)
print(next(gen))    # 1
print(next(gen))    # 2
print(next(gen))    # 3
print(next(gen))    # 4
print(next(gen))    # 5
print(next(gen))    # 6
print(next(gen))    # 7
print(next(gen))    # 8
print(next(gen))    # 9
print(next(gen))    # 10
print(next(gen))    # 11
print(next(gen))    # 12
print(next(gen))    # 13
print(next(gen))    # 14
print(next(gen))    # 15
try:
    print(next(gen))
except StopIteration as ex:
    print("Exception StopIteration happend.")

# slice from generator

gen2 = bar(10)
slice_gen2 = itertools.islice(gen2, 0, 5)
print(list(slice_gen2))

# regular expressions

s = 'My email is cherkasov.kirill@gmail.com, my second email-2 is ' \
    'cherkasov.kirill-1@yandex.ru'
print(re.findall('email', s))
print(re.findall('(email)', s))

# recomend to use raw strings in patterns
print('\n\thello')
print(r'\n\thello')
print(re.findall(r'\s(email)\s', s))
print(re.findall(r'[l1]@', s))
# same as previous
print(re.findall(r'[a-zA-Z0-9-\.]+@[a-zA-Z0-9-\.]+', s))
print(re.findall(r'[\w\.-]+@[\w\.-]+', s))

# greedy regular expressions

s1 = 'cat cot dog dig dug carrot'

print(re.findall(r'c.*t', s1))

# not greedy
print(re.findall(r'c.*?t', s1))

# Exact amount of symbols

print(re.findall(r'c.{2,4}t', s1))

d_s = '12983728934563897456249837562948383838356982437569283412137128937689411'
# looking only to \d83\d occurences
print(re.findall(r'\d(83)\d', d_s))
print(re.findall(r'83', d_s))

# looking to all 83 occurences

print(re.findall(r'(?<=\d)(83)(?=\d)', d_s))

# correct way to set file paths

print(os.path.join('dir1', 'dir2', 'dir3', 'dir4'))