import re
import os
import random

# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.


def ex_with_re_1(line):
    pattern = r'[a-z]+(?=[A-Z])|(?<=[A-Z])[a-z]+'
    return re.findall(pattern, line)


def ex_without_re_1(line):
    result = []
    i = 0
    while i < len(line):
        if line[i].istitle():
            i += 1
            continue
        small_str = ''
        while i < len(line) and not line[i].istitle():
            small_str = ''.join([small_str, line[i]])
            i += 1
        result.append(small_str)
    return result
# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.


def ex2_with_re(line):
    pattern = r'(?<=[a-z][a-z])[A-Z]+(?=[A-Z][A-Z])'
    return re.findall(pattern, line)


def ex2_without_re(line):
    result = []
    i = 2
    while i < len(line) - 2:
        if line[i].istitle():
            if not line[i-1].istitle() and not line[i-2].istitle():
                small_str = ''
                while i < len(line) - 2 \
                        and line[i+1].istitle() \
                        and line[i+2].istitle():
                    small_str = ''.join([small_str, line[i]])
                    i += 1
                if small_str:
                    result.append(small_str)
        i += 1
    return result

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.


def ex3_write_file(filename, nmax=2500):
    with open(filename, 'w', encoding='utf-8') as f:
        string_to_write = ''
        for i in range(nmax):
            num = random.randint(0, 9)
            string_to_write = ''.join([string_to_write, str(num)])
        f.write(string_to_write)


def ex3_wre(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        i = 1
        raw_file = f.read()
        concurrences = []
        while True:
            pattern = r'(\d+)\1{' + str(i) + '}'
            result = re.findall(pattern, raw_file)
            if not result:
                break
            concurrences.append(result)
            i += 1
    for index, item in enumerate(concurrences[i - 2]):
        concurrences[i - 2][index] = item * i
    return concurrences[i - 2]


def ex3_wore(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        max_len = 0
        result = []
        i = 0
        file = f.read()
        while i < len(file):
            repeat_digits = file[i]
            while i < len(file) - 1 and file[i] == file[i + 1]:
                repeat_digits = ''.join([repeat_digits, file[i + 1]])
                i += 1
            if len(repeat_digits) == max_len:
                result.append(repeat_digits)
            if len(repeat_digits) > max_len:
                max_len = len(repeat_digits)
                result = list()
                result.append(repeat_digits)
            i += 1
    return result

if __name__ == '__main__':
    line_1 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO' \
           'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK' \
           'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn' \
           'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa' \
           'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete' \
           'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ' \
           'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb' \
           'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC' \
           'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB' \
           'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT' \
           'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu' \
           'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB' \
           'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa' \
           'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ' \
           'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

    line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm' \
             'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV' \
             'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA' \
             'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV' \
             'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW' \
             'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC' \
             'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR' \
             'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm' \
             'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn' \
             'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS' \
             'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf' \
             'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH' \
             'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN' \
             'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ' \
             'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

    print(ex_with_re_1(line_1))
    print('*' * 40)
    print(ex_without_re_1(line_1))
    print('*' * 40)
    print(ex2_with_re(line_2))
    print(ex2_without_re(line_2))
    fname = os.path.join('data', 'numbers.txt')
    ex3_write_file(fname)
    print(ex3_wore(fname))
    # works much slower than my realization
    print(ex3_wre(fname))