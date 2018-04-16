# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    if not isinstance(number, (float, int)):
        raise ValueError('number must be float or int')
    if not isinstance(ndigits, (float,int)):
        raise ValueError('ndigits must be int')
    big_number = number * 10**ndigits
    frac = big_number - big_number // 1
    big_number //= 1
    if frac >= .5:
        frac = 1
    else:
        frac = 0
    big_number += frac
    big_number /= 10**ndigits
    return big_number


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    '''
    Defines lucky ticket or not. Solution with strings.
    :param ticket_number:
    :return:
    '''
    if not isinstance(ticket_number, int):
        raise ValueError('Ticket number must be integer.')
    ticket_number = str(ticket_number)
    if len(ticket_number) != 6:
        raise ValueError('Invalid length of ticket number.')
    if sum(map(int,ticket_number[:3])) == sum(map(int, ticket_number[3:])):
        return True
    return False


def lucky_ticket_2(ticket_number):
    '''
    Defines lucky ticket or not. Solution with ariphmetical operations.
    :param ticket_number:
    :return:
    '''
    if not isinstance(ticket_number, int):
        raise ValueError('Ticket number must be integer.')
    if len(str(ticket_number)) != 6:
        raise ValueError('Invalid length of ticket number.')
    digits = []
    for i in range(1, 7):
        if i != 1:
            num = (ticket_number % 10**i - ticket_number % 10**(i - 1)) // 10**(i - 1)
        else:
            num = ticket_number % 10**i
        digits.append(num)
    if sum(digits[:3]) == sum(digits[3:]):
        return True
    return False


if __name__ == '__main__':
    print(my_round(4.6, 0))
    print(my_round(4.54, 1))
    print(my_round(4.546, 2))
    print(my_round(-4.54, 2))
    tickets = [123456, 568910, 524119]
    for ticket in tickets:
        print('{} is lucky: {} - string way function'
              .format(ticket, lucky_ticket(ticket)))
        print('{} is lucky: {} - digits way function'
              .format(ticket, lucky_ticket_2(ticket)))