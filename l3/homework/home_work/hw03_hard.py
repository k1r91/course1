import math
import os

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

    def nod(a, b):
        '''
        greatest common divisor
        :param a:
        :param b:
        :return:
        '''
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        return a + b

    def simplify_fraction(num, denom):
        while nod(num, denom) != 1:
            frac_nod = nod(num, denom)
            num /= frac_nod
            denom /= frac_nod
        return int(num), int(denom)

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
    if math.fabs(summ) > expr_noz:
        whole_part = summ // expr_noz
        fract_part = summ % expr_noz
        if fract_part:
            fract_part, expr_noz = simplify_fraction(fract_part, expr_noz)
            return '{} {}/{}'.format(whole_part, fract_part, expr_noz)
        else:
            return '{}'.format(whole_part)
    if summ:
        if math.fabs(summ) == expr_noz:
            return str(int(summ/expr_noz))
        summ, expr_noz = simplify_fraction(summ, expr_noz)
        return '{}/{}'.format(summ, expr_noz)
    else:
        return '0'

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


def calculate_salary(fname_workers, fname_hours):

    def _calc_salary(st_salary, st_hours, w_hours):
        '''
        calculate salary according to the condition
        :param st_salary: standart worker salary
        :param st_hours: standart worker hours
        :param w_hours: worked hours
        :return:
        '''
        st_salary, st_hours, w_hours = tuple(map(int, [st_salary,
                                                       st_hours,
                                                       w_hours]))
        if st_hours == w_hours:
            result_salary = st_salary
        elif w_hours < st_hours:
            result_salary = st_salary * w_hours / st_hours
        else:
            result_salary = st_salary * (1 + 2 * (w_hours-st_hours) / st_hours)
        return result_salary

    def print_salary(wlist):
        '''
        print all salaries
        :param wlist:
        :return:
        '''
        h_template = '{:<17}' * 7
        w_template = '{:<17}' * 6
        w_template = ''.join([w_template, '{:<17.2f}'])
        print(h_template.format('Имя', 'Фамилия', 'Зарплата', 'Должность',
                              'Норма часов', 'Отработано часов',
                              'Итоговая зарплата'))
        for worker in wlist:
            print(w_template.format(worker[0], worker[1], worker[2], worker[3],
                                  worker[4], worker[5], worker[6]))
    def fill_list(fname):
        result = []
        with open(os.path.join(fname), encoding='utf-8') as file:
            file_list = list(file)
            for line in file_list[1:]:
                result.append(line.split())
        return sorted(result, key=lambda x: x[1])

    workers_list, hours_list = fill_list(fname_workers), fill_list(fname_hours)
    i = 0
    for worker in workers_list:
        worker.append(hours_list[i][2])
        worker.append(_calc_salary(worker[2], worker[4], worker[5]))
        i += 1

    print_salary(workers_list)


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


def fun_with_fruits(fruit_fname):
    # clear all files
    for file in os.listdir(os.path.join('data/fruit_files')):
        fname = os.path.join('data/fruit_files/{}'.format(file))
        if os.path.isfile(fname):
            os.remove(fname)
    rus_letters = list(map(chr, range(ord('А'), ord('Я') + 1)))
    with open(os.path.join(fruit_fname), 'r', encoding='utf-8') as f:
        for line in f:
            if line[0] in rus_letters:
                fname = os.path.join('data/fruit_files/{}'.format(line[0]))
                if os.path.isfile(fname):
                    with open(fname, 'a', encoding='utf-8') as file:
                        file.write(line)
                else:
                    with open(fname, 'w', encoding='utf-8') as file:
                        file.write(line)

if __name__ == '__main__':
    expressions = [
        '5/6 + 4/7',
        '-2/3 - -2',
        '2/3 + 2 - -4/7 - 4/5 + 1/6 + 1/2',
        '8/3 + -2/3',
        '1/3 - 1/3',
        '4/3 + 71/4',
        '2/3 - 2 - -4/7 - 4/5 - 1/6 - 1/2',
        '1/3 + 1/12 + 5/12',
        '-4/5 + 4/5',
        '5/3 - 1/6 - 1/2',
    ]

    for expr in expressions:
        print(frac_calculator(expr))

    calculate_salary('data/workers', 'data/hours_of')
    fun_with_fruits('data/fruits.txt')