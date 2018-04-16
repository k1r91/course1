import math

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    for num in [n, m]:
        if not isinstance(num, int):
            raise ValueError('n and m must be integers.')
    if n <= 0:
        raise ValueError('n must be greater than 0.')
    if not isinstance(m, int) or m <= 0:
        raise ValueError('m must be greater than 0.')
    if n == m == 1:
        return [1]
    elif m < n:
        raise ValueError('m must be greater than n.')
    num1 = 1
    num2 = 1
    result = [num1, num2]
    for i in range(2, m):
        fib_number = num1 + num2
        result.append(fib_number)
        num1 = num2
        num2 = fib_number
    return result[n - 1:]

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    i = 0
    while i < len(origin_list):
        j = i
        while j < len(origin_list):
            if origin_list[i] > origin_list[j]:
                origin_list[i], origin_list[j] = origin_list[j], origin_list[i]
            j += 1
        i += 1
    return origin_list


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(func, ls):
    '''
    Analog of python 'filter' function.
    :param func:
    :param ls:
    :return:
    '''
    if not callable(func):
        raise TypeError('func must be a function.')
    if not isinstance(ls, (tuple, list, set)):
        raise TypeError('ls must be tuple, list or set.')
    result = []
    for item in ls:
        if func(item):
            result.append(item)
    return result


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def is_parallelogram(a1, a2, a3, a4):

    def line_length(c1, c2):
        return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)
    len1 = len(a1, a2)
    len2 = len(a2, a3)
    len3 = len(a3, a4)
    len4 = len(a4, a1)
    if 0 in [len1, len2, len3, len4]:
        return False
    if len1 == len3 and len2 == len4:
        return True
    return False


if __name__ == '__main__':
    fiblist = [(0, 1), (1, 1), (1, -2), (7, 4), (2, 5), ('asd', 5),
               (125, 130), (298, 300), (1000, 1001)]
    for start, end in fiblist:
        try:
            print(fibonacci(start, end))
        except ValueError as e:
            print(e)

    print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

    print(my_filter(lambda x: x > 0, [1, 2, 3, -5, 6]))
    try:
        print(my_filter('asd', [1, 2, 3, -5, 6]))
    except Exception as e:
        print(e)
    try:
        print(my_filter(lambda x: x**2, 'asd'))
    except Exception as e:
        print(e)
    examples = [((3, 2), (6, 6), (9, 6), (6, 2)),
                ((3, 2), (6, 6), (9, 6), (6, 1)),
                ((0, 0), (0, 0), (0, 0), (0, 0)),
                ((-3, -2), (6, 6), (9, 6), (6, 2)),]
    for figure in examples:
        print('Figure {} is parallelogram: {}'.
              format(figure, is_parallelogram(figure)))
