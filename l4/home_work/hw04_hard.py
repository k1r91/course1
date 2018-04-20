# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример. Дано:
matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]
          
# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку


def transpose(matrix=matrix):
    return list(zip(*matrix))

print(transpose())
print(transpose([[5, 6, 2, 1], [-2, 3, 8, 10]]))
print('*' * 120)
# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.
# Пример 1000-значного числа:
number = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""


def get_multiplication(s):
    '''
    вычисляет произведение чисел в строке s
    :param s:
    :return:
    '''
    multi = 1
    for i in range(len(s)):
        multi *= int(s[i])
    return multi


def get_max_multiplication(n=number):
    multi_list = []
    for i in range(len(n) - 4):
        num = n[i : i + 5]
        try:
            multi_list.append([get_multiplication(num), i])
        except ValueError:
            pass
    maximum = max(multi_list)
    return {"Максимум: ": maximum[0], "Индекс: ": maximum[1]}
print(get_max_multiplication(number))
print(get_max_multiplication('123456790999'))
print('*' * 120)

# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.


def is_beats(queens):
    '''
    простая проверка по диагоналям и прямым каждого ферзя
    :param queens:
    :return:
    '''
    for queen in queens:
        i, j = queen[0] + 1, queen[1] + 1
        while i <= 8 and j <=8:
            if [i, j] in queens:
                return True
            i += 1
            j += 1
        i, j = queen[0] - 1, queen[1] - 1
        while i >= 1 and j >= 1:
            if [i, j] in queens:
                return True
            i -= 1
            j -= 1
        i, j = queen[0] + 1, queen[1] - 1
        while i <= 8 and j >= 1:
            if [i, j] in queens:
                return True
            i += 1
            j -= 1
        i, j = queen[0] - 1, queen[1] + 1
        while i >= 1 and j <= 8:
            if [i, j] in queens:
                return True
            i -= 1
            j += 1
        i = queen[0]
        for j in range(8, queen[1], -1):
            if [i, j] in queens:
                return True
        for j in range(queen[1] - 1, 0, -1):
            if [i, j] in queens:
                return True
        j = queen[1]
        for i in range(1, queen[0]):
            if [i, j] in queens:
                return True
        for i in range(queen[0] + 1, 9):
            if [i, j] in queens:
                return True
    return False

# наборы, где ферзи не бьют друг друга

queens1 = [[2, 1], [4, 2], [6, 3], [8, 4], [3, 5], [1, 6], [7, 7], [5, 8]]
queens5 = [[6, 1], [4, 8], [7, 7], [2, 4], [8, 5], [3, 6], [5, 3], [1, 2]]

print(is_beats(queens1), queens1)
print(is_beats(queens5), queens5)

# наборы, где ферзи бьют друг друга

queens2 = [[1, 1], [4, 2], [6, 3], [8, 4], [3, 5], [1, 6], [7, 7], [5, 8]]
print(is_beats(queens2), queens2)
queens3 = [[3, 1], [4, 2], [6, 3], [8, 4], [3, 5], [1, 6], [7, 7], [5, 8]]
print(is_beats(queens3), queens3)
queens4 = [[1, 1], [2, 2], [3, 7], [6, 2], [8, 8], [3, 2], [1, 4], [2, 7]]
print(is_beats(queens4), queens4)
