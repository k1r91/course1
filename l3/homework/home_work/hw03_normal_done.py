# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

import math

def fibonacci(n, m):
    '''
    return fibonacci, starts with zero element
    :param n:
    :param m:
    :return:
    '''
    num1 = 1
    num2 = 1
    result = [num1, num2]
    for i in range(m):
        result.append(num1 + num2)
        num1 = num2
        num2 = result[-1]
    return result[n:m + 1]

print(fibonacci(0, 5))
print(fibonacci(25, 26))
print(fibonacci(3,6))
print ("*" * 40)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    result = []
    i = 0
    while i < len(origin_list) - 1:
        j = i
        while j < len(origin_list):
            if (origin_list[j] >= origin_list[i]):
                origin_list[j], origin_list[i] = origin_list[i], origin_list[j]
            j += 1
        i += 1
    return origin_list
print(sort_to_max([1, 2, 3, 4, 5]))

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(function, iterable):
    result = []
    if function:
        for item in iterable:
            if function(item):
                result.append(item)
    else:
        for item in iterable:
            if item:
                result.append(item)
    return result
print ("*" * 40)
print(my_filter(lambda x: x <= 0, range(-6, 6)))
print ("*" * 40)
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def is_parallelogram(x1, y1, x2, y2, x3, y3, x4, y4):
    '''
    Проверка проводится по свойству: если противоположные стороны
    четырёхугольника попарно равны, то он является параллелограммом
    при условии, что точки располагаются последовательно по (или против)
    часовой стрелки
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :param x3:
    :param y3:
    :param x4:
    :param y4:
    :return:
    '''


    def line_length(x1, y1, x2, y2):
        '''
        определяет длину отрезка по координатам
        :param x1:
        :param y1:
        :param x2:
        :param y2:
        :return:
        '''
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    line1 = line_length(x1, y1, x2, y2)
    line2 = line_length(x2, y2, x3, y3)
    line3 = line_length(x3, y3, x4, y4)
    line4 = line_length(x4, y4, x1, y1)
    if 0 in [line1, line2, line3, line4]:
        return False
    if line1 == line3 and line2 == line4:
        return True
    else:
        return False
print(is_parallelogram(3, 2, 6, 6, 9, 6, 6, 2))
print(is_parallelogram(3, 2, 6, 6, 9, 6, 6, 1))
print(is_parallelogram(0, 0, 0, 0, 0, 0, 0, 0))
print(is_parallelogram(-3, -2, 6, 6, 9, 6, 6, 2))