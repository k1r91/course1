# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз


def format_list(data):
    count = 1
    max_len = len(max(data, key=len)) + 1
    for item in data:
        line = ''.join([
            str(count),
            '.',
            item.rjust(max_len)
        ])
        count += 1
        print(line)


def format_list2(data):
    count = 1
    for item in data:
        print('{}. {:>6}'.format(count, item))
        count += 1
# Подсказка: воспользоваться методом .format()


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

def clear_list(list1, list2):
    for item in list2:
        if item in list1:
            list1 = [i for i in list1 if i != item]
    return list1

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


def some_operations(data):
    result = []
    for item in data:
        print(item)
        if item % 2 == 0:
            result.append(item / 4)
        else:
            result.append(item * 2)
    return result

if __name__ == '__main__':
    format_list(['яблокоjjjjjjjjjjj', 'банан', 'киви','арбуз'])
    format_list2(['яблокоjjjjjjjjjjjjjj', 'банан', 'киви', 'арбуз'])
    print(clear_list([1, 2, 3, 4, 4, 4, 5, 6], [4, 5, 5, 7, 9]))
    print(some_operations([1, 2, 3, 4, 5, 6]))