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


def summ_fractions(expression):
    def nod(a, b):
        while a != 0 and b !=0:
            if a > b:
                a %= b
            else:
                b %= a
        return a + b
    def nok(a, b):
        '''
        вычисляем наименьшее общее кратное
        :param a:
        :param b:
        :return:
        '''
        m = a * b
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        return m // (a + b)
    def common_denominator(oplist):
        '''
        вычисляем общий знаменатель
        :param oplist:
        :return:
        '''
        cdenominator = 1
        for item in oplist:
            try:
                denominator = item[item.index("/") + 1:]
                denominator = int(denominator)
                if cdenominator % denominator:
                    cdenominator = nok(denominator, cdenominator)
            except ValueError:
                pass
        return cdenominator


    def get_numerator(item ,cdenomimanor):
        try:
            denominator = int(item[item.index('/') + 1:])
            numerator = int(item[:item.index('/')]) * (cdenominator / denominator)
        except ValueError:
            numerator = int(item) * cdenominator
        return numerator
    result = ""
    i = 0;
    operation_list = []
    while i < len(expression):
        start = i
        try:
            i = expression.index(" ", i)
            operation_list.append(expression[start:i])
        except ValueError:
            operation_list.append(expression[start:])
            break
        i += 1
    cdenominator = common_denominator(operation_list)
    numerator = 0
    cnumerator = 0
    i = 0
    fraction = True
    while i < len(operation_list):
        if i == 0:
            cnumerator += get_numerator(operation_list[i], cdenominator)
        elif operation_list[i] == "+":
            i += 1
            cnumerator += get_numerator(operation_list[i], cdenominator)
        else:
            i += 1
            cnumerator -= get_numerator(operation_list[i], cdenominator)
        i += 1
    fraction_nod = nod(cnumerator, cdenominator)
    fraction_numerator = cnumerator / fraction_nod
    fraction_denominator = cdenominator / fraction_nod
    fraction_n = fraction_numerator // fraction_denominator
    fraction_f = fraction_numerator % fraction_denominator
    if fraction_f:
        denomstirng = str(int(fraction_f)) + "/" + str(int(fraction_denominator))
    else:
        denomstirng = ""
    if fraction_n:
        numeratstring = str(int(fraction_n))
    elif fraction_f == 0:
        numeratstring = "0"
    else:
        numeratstring = ""
    result = numeratstring + " " + denomstirng
    return result
print(summ_fractions("5/6 + 4/7"))
print(summ_fractions("-2/3 - -2"))
print(summ_fractions("-2/3 + 2 - -4/7 - 4/5 + 1/6 + 1/2"))
print(summ_fractions("8/3 + -2/3"))
print(summ_fractions("1/3 - 1/3"))
print(summ_fractions("4/3 + 71/4"))
# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


def print_salary(workers="data/workers", hours="data/hours_of"):
    with open(workers, "r", encoding='utf-8') as workers:
        workers = list(workers)
        workers_list = []
        i = 0
        for item in workers[1:]:
            workers_list.append(item.split())
        with open(hours, "r", encoding='utf-8') as hours:
            hours = list(hours)
            hours_list = []
            for item in hours[1:]:
                hours_list.append(item.split())

    # сортировка по фамилии
    workers_list.sort(key=lambda x: x[1])
    hours_list.sort(key=lambda x: x[1])
    sep = 10
    i = 0
    sep = " " * 8
    print("Имя  Фамилия  Оклад  Должность  Норма_часов  Отработано часов  Зарплата")
    while i < len(workers_list):
        name = workers_list[i][0]
        surname = workers_list[i][1]
        hours = workers_list[i][-1]
        worked_hours = hours_list[i][2]
        salary = workers_list[i][2]
        position = workers_list[i][3]
        payment = float(salary) * (float(worked_hours) / float(hours))
        print("{0}  {1}  {2}  {3}  {4}  {5}  {6}".
              format(name, surname, salary, position, hours, worked_hours, str(payment)))
        i += 1
print_salary()
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
