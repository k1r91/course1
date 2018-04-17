# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


def frac_calculator(expression):
    def noz(znams):
        '''
        calculate least common denominator
        :param znams:
        :return:
        '''
        znams = list(map(int, znams))
        max_denom = max(znams)
        noz = max_denom
        mult = 2
        flag = True
        while flag:
            for znam in znams:
                if noz % znam != 0:
                    flag = True
                    noz = max_denom * mult
                    mult += 1
                    break
                flag = False
        return noz

    fracs = expression.split()
    znam = []
    for frac in fracs:
        if '/' in frac:
            znam.append(frac.split('/')[1])
    expr_noz = noz(znam)  # least common denominator
    summ = 0
    i = 0
    for frac in fracs:
        if frac in '+-':
            i += 1
            continue
        try:
            sign = fracs[i - 1]
            if sign == '+':
                sign = True
            elif sign == '-':
                sign = False
        except IndexError:
            sign = True
        if '/' in frac:
            numerator = int(frac.split('/')[0])
            denominator = int(frac.split('/')[1])
            numerator = numerator * expr_noz / denominator
        elif frac.replace('-', '').isdigit():
            numerator = int(frac) * expr_noz
        if sign:
            summ += numerator
        else:
            summ -= numerator
        i += 1
    summ = int(summ)
    if summ > expr_noz:
        whole_part = summ // expr_noz
        fract_part = summ % expr_noz
        if fract_part:
            return '{} {}/{}'.format(whole_part, fract_part, expr_noz)
        else:
            return '{}'.format(whole_part)
    return '{}/{}'.format(summ, expr_noz)

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))


if __name__ == '__main__':
    expressions = [
        '5/6 + 4/7',
        '-2/3 - -2',
        '2/3 + 2 - -4/7 - 4/5 + 1/6 + 1/2',
        '8/3 + -2/3',
        '1/3 - 1/3',
        '4/3 + 71/4',
    ]

    for expr in expressions:
        print(frac_calculator(expr))