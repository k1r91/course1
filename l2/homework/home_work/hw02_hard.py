# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
import math

class EquationException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def parse_equation(expression, x):
    index = expression.find('x')
    if index > 0:
        pos = index
        mult = ""
        const = ""
        while expression[pos] != ' ':
            pos -= 1
            if expression[pos].isdigit() or expression[pos] in '+-.':
                mult = ''.join([mult, expression[pos]])
            elif expression[pos] != ' ':
                raise EquationException('Error in equation definition at x')
        mult = mult[::-1]
        try:
            mult = float(mult)
        except ValueError:
            raise EquationException('Error in x- multiplayer defining')
        try:
            const = ''.join([expression[index + 2]])
            if const not in '+-':
                raise EquationException('Const sign must be + or -')
        except:
            raise EquationException('Error in const sign')
        if expression[index + 3] != ' ':
            raise EquationException('Missing whitespace after const sign')
        for i in range(index + 4, len(expression)):
            const = ''.join([const, expression[i]])
        try:
            const = float(const)
        except ValueError:
            raise EquationException("Error in const definition")
        print('{}*{}{} = '. format(mult, x, const))
    else:
        raise EquationException("Can't find x")
    return mult * x + const
# вычислите и выведите y


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'


def parse_date(date):
    print('{} is correct - '.format(date))
    if len(date) != 10:
        return False
    day = date[:2]
    month = date[3:5]
    year = date[-4:]
    for num in [day, month, year]:
        if not num.isdigit():
            return False
    day, month, year = int(day), int(month), int(year)
    if year < 1 or year > 9999:
        return False
    if month < 1 or month > 12:
        return False
    february_days = 28
    if year % 400 == 0:
        february_days = 29
    else:
        if year % 100 != 0 and year % 4 == 0:
            february_days = 29
    day_in_months = {1: 31, 2: february_days, 3: 31, 4: 30, 5: 31, 6: 30,
                     7: 31, 8:31, 9: 30, 10: 31, 11: 30, 12: 31}
    if day < 1 or day > day_in_months[month]:
        return False
    return True

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3


def lift(room_number):
    if room_number < 1 or room_number > 2000000000:
        return 0, 0
    if room_number == 1:
        return 1, 1
    floor = 1
    step = 2
    i = 1
    while i < room_number:
        i += step * step
        floor += step - 1
        step += 1
    square = step - 1
    room = i - square*square + 1
    for x in range(square):
        position = 1
        for y in range(square):
            if room == room_number:
                return floor, position
            position += 1
            room += 1
        floor += 1
    return 1, 1


if __name__ == '__main__':
    print(parse_equation('y = 2x - 4', 2.5))
    print(parse_date('28.02.9999'))
    print(parse_date('01.22.1001'))
    print(parse_date('1.12.1001'))
    print(parse_date('-2.10.3001'))
    print(lift(27))
    print('Done!')