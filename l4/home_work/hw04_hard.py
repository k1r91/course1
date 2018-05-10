from functools import reduce

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


def matrix_rotate(mtx):
    return list(map(list, zip(*mtx)))


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


def max_mult_five(n):
    n = n.replace('\n', '')
    max_mult = 0
    i = 0
    while i < len(n) - 5:
        mult = reduce(lambda x, y: x * y, map(int, n[i:i + 5]))
        if mult > max_mult:
            max_mult = mult
        i += 1
    return max_mult

# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.


def queens_beat(position):
    for current_queen in position:
        ls = position[:]
        ls.remove(current_queen)
        for queen in ls:
            # check horizontal line
            if current_queen[0] == queen[0]:
                return False
            # check vertical line
            if current_queen[1] == queen[1]:
                return False
            # check diagonal line
            if current_queen[0] - queen[0] == current_queen[1] - queen[1]:
                return False
    return True
if __name__ == '__main__':
    print(matrix_rotate(matrix))
    print(max_mult_five(number))
    positions = [
        [(1, 2), (2, 4), (3, 6), (4, 8), (5, 3), (6, 1), (7, 7), (8, 5)],
        [(1, 4), (2, 6), (3, 8), (4, 2), (5, 7), (6, 1), (7, 3), (8, 5)],
        [(3, 2), (1, 2), (2, 7), (4, 8), (6, 8), (5, 3), (4, 2), (7, 7)],
        [(8, 8), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)],
        [(2, 3), (5, 4), (1, 7), (8, 2), (3, 5), (7, 8), (6, 5), (4, 6)],
        [(5, 8), (1, 1), (1, 8), (8, 5), (3, 3), (6, 1), (6, 7), (3, 6)],
        [(4, 8), (3, 2), (8, 6), (3, 3), (7, 7), (5, 6), (4, 2), (8, 5)]
    ]
    for step, pos in enumerate(positions):
        if queens_beat(pos):
            mod = 'NO'
        else:
            mod = 'YES'
        print('Position № {} is beatable: {}'.format(step, mod))
