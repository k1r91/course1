#!/usr/bin/python3

"""Упражнение "Количество слов"

Функция main() ниже уже определена и заполнена. Она вызывает функции 
print_words() и print_top(), которые вам нужно заполнить.

1. Если при вызове файла задан флаг --count, вызывается функция 
print_words(filename), которая подсчитывает, как часто каждое слово встречается 
в тексте и выводит:
слово1 количество1
слово2 количество2
...

Выводимый список отсортируйте в алфавитном порядке. Храните все слова 
в нижнем регистре, т.о. слова "Слон" и "слон" будут обрабатываться как одно 
слово.

2. Если задан флаг --topcount, вызывается функция print_top(filename),
которая аналогична функции print_words(), но выводит только топ-20 наиболее 
часто встречающихся слов, таким образом первым будет самое часто встречающееся 
слово, за ним следующее по частоте и т.д.

Используйте str.split() (без аргументов), чтобы разбить текст на слова.

Отсекайте знаки припинания при помощи str.strip() с знаками припинания 
в качестве аргумента.

Совет: не пишите всю программу сразу. Доведите ее до какого-то промежуточного 
состояния и выведите вашу текущую структуру данных. Когда все будет работать 
как надо, перейдите к следующему этапу.

Дополнительно: определите вспомогательную функцию, чтобы избежать дублирования 
кода внутри print_words() и print_top().

"""

import sys

# +++ваш код+++
# Определите и заполните функции print_words(filename) и print_top(filename).
# Вы также можете написать вспомогательную функцию, которая читает файл,
# строит по нему словарь слово/количество и возвращает этот словарь.
# Затем print_words() и print_top() смогут просто вызывать эту вспомогательную функцию.

###

# Это базовый код для разбора аргументов коммандной строки.
# Он вызывает print_words() и print_top(), которые необходимо определить.


def sanitize_words(words):
    san_list = '.,:?!"()'
    result = []
    for word in words:
        if len(word) > 2:
            result.append(''.join(char for char in word if char not in san_list))
    return result


def count_words(filename):
    result = {}
    with open(filename, 'r', encoding='utf-8') as f:
        words = f.read().split()
        words = sanitize_words(words)
    for word in words:
        if word not in result.keys():
            result[word] = words.count(word)
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    return result


def print_top(filename):
    for word, count in count_words(filename)[:20]:
        print(word, count)


def print_words(filename):
    for word, count in count_words(filename):
        print(word, count)


def main():
    if len(sys.argv) != 3:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
    main()
