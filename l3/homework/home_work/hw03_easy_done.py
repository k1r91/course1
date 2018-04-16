# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    bigtmp = number * 10**ndigits
    frac = bigtmp - bigtmp // 1
    bigtmp = bigtmp // 1
    print(frac)
    if frac >= 0.5:
        frac = 1
    else:
        frac = 0
    bigtmp += frac
    result = bigtmp / 10**ndigits
    return result
print(my_round(2.6, 0))
print(my_round(2.1234567, 5))
print(my_round(2.1234567, 6))
print(my_round(3.14159, 25))
print(my_round(2.1234567, 1))
print(my_round(2.1234567, 0))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_str = str(ticket_number)
    if not ticket_str.isdigit():
        return False
    if len(ticket_str) != 6:
        return False
    i = 0
    suml = 0
    sumr = 0
    for symb in ticket_str:
        if i < 3:
            suml += int(symb)
        else:
            sumr += int(symb)
        i += 1
    if suml == sumr:
        return True
    else:
        return False
print(lucky_ticket(123456))
print(lucky_ticket(123321))
print(lucky_ticket(123015))
print(lucky_ticket(123456))
print(lucky_ticket(952178))


