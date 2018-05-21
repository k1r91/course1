# -*- coding: utf-8 -*-

"""
Это пример небольшой программы для рисования кругов и квадратов.
Вам нужно на основе этой программы сделать небольшую "танцевальную" сценку с
использованием кругов, квардратов и треугольников. Сделать всё это нужно в
объектно ориентированном стиле.

Какие классы нужно реализовать:

-Многоугольник(на его основе сделать квадрат и правильный треугольник)
--класс должен уметь отрисовывать себя
--перемещаться в некоторм направлении, заданом координатами x, y
--увеличивать(необязательно)
--поворачивать(необязательно)

-Квардрат(наследуется от многоугольника)
--метод __init__ принимает координаты середины, ширину и цвет

-Треугольник(наследуется от многоугольника)
--метод __init__ принимает координаты середины, длинну грани и цвет

-Круг
--метод __init__ принимает координаты середины, радиус и цвет
--класс должен уметь отрисовывать себя
--премещаться в некоторм направлении, заданом координатами x, y
--увеличивать(необязательно)

Также рекомендуется создать вспомогательный сласс Vector для представления
точек на плоскости и различных операций с ними - сложение, умножение на число,
вычитание.


Из получившихся классов нужно составить какую-нибудь динамическую сцену.
Смотрите пример example.gif
"""

import turtle
import time
import random
import math


class Figure:
    def __init__(self, coords, ttl, color):
        self.coords = coords
        self.ttl = ttl
        self.left = -350
        self.right = 350
        self.color = color


class Circle(Figure):
    def __init__(self, coords, ttl, color, radius, max_radius=70):
        super().__init__(coords, ttl, color)
        self._start_radius = radius
        self.radius = radius
        self.direction = True
        self.graw_direction = True
        self.max_radius = max_radius

    def draw(self):
        self.ttl.color(self.color)
        self.ttl.penup()
        self.ttl.setpos(self.coords[0], self.coords[1] - self.radius)
        self.ttl.pendown()
        self.ttl.circle(self.radius)

    def move_horizont(self):
        if self.is_at_right_border():
            self.direction = False
        if self.is_at_left_border():
            self.direction = True
        if self.direction:
            self.coords[0] += 5
        else:
            self.coords[0] -= 5

    def is_at_right_border(self):
        if self.coords[0] > self.right:
            return True

    def is_at_left_border(self):
        if self.coords[0] < self.left:
            return True

    @property
    def is_big(self):
        if self.radius > self.max_radius:
            return True

    @property
    def is_small(self):
        if self.radius < self._start_radius:
            return True

    def grow(self):
        if self.is_big:
            self.graw_direction = False
        if self.is_small:
            self.graw_direction = True
        if self.graw_direction:
            self.radius += 1
        else:
            self.radius -= 1

    def rotate(self, point, degree):
        radian = math.radians(degree)
        offset_x = (self.coords[0] - point[0]) * math.cos(radian) - \
                   (self.coords[1] - point[1]) * math.sin(radian)
        offset_y = (self.coords[0] - point[0]) * math.sin(radian) + \
                   (self.coords[1] - point[1]) * math.cos(radian)
        self.coords[0] = point[0] + offset_x
        self.coords[1] = point[1] + offset_y


class Polygon:
    def __init__(self, coords, ttl, color, max_graw_value=300):
        self.coords = coords
        self.ttl = ttl
        self.color = color
        self.direction = True
        self.left = -350
        self.right = 350
        self.max_graw_value = max_graw_value
        self.min_graw_value = 0
        self.current_graw_value = 0
        self.graw_direction = True
        self.offsets = self.get_offsets()

    def draw(self):
        self.ttl.color(self.color)
        self.ttl.penup()
        self.ttl.setpos(self.coords[0][0], self.coords[0][1])
        self.ttl.pendown()
        for coord in self.coords:
            self.ttl.goto(coord[0], coord[1])
        self.ttl.goto(self.coords[0][0], self.coords[0][1])
        self.ttl.penup()

    def move_horizont(self):
        if self.is_at_left_border:
            self.direction = True
        if self.is_at_right_border:
            self.direction = False
        for i, coord in enumerate(self.coords[:]):
            if self.direction:
                self.coords[i][0] += 3
            else:
                self.coords[i][0] -= 3

    @property
    def is_at_right_border(self):
        max_right = max([x[0] for x in self.coords])
        if max_right > self.right:
            return True

    @property
    def is_at_left_border(self):
        max_left = min([x[0] for x in self.coords])
        if max_left < self.left:
            return True

    @property
    def center(self):
        center_x = self.avg([x[0] for x in self.coords])
        center_y = self.avg([x[1] for x in self.coords])
        return [center_x, center_y]

    def rotate(self, degree):
        radian = math.radians(degree)
        for i, coord in enumerate(self.coords[:]):
            offset_x = math.cos(radian) * (coord[0] - self.center[0]) - \
                       math.sin(radian) * (coord[1] - self.center[1])
            offset_y = math.sin(radian) * (coord[0] - self.center[0]) + \
                       math.cos(radian) * (coord[1] - self.center[1])
            self.coords[i][0] = self.center[0] + offset_x
            self.coords[i][1] = self.center[1] + offset_y

    def lift_up(self, offset):
        for i, coord in enumerate(self.coords[:]):
            self.coords[i][1] += offset

    @property
    def is_big(self):
        if self.current_graw_value >= self.max_graw_value:
            return True

    @property
    def is_normal(self):
        if self.current_graw_value <= self.min_graw_value:
            return True

    def grow(self):
        if self.is_big:
            self.graw_direction = False
        if self.is_normal:
            self.graw_direction = True
        for i, coord in enumerate(self.coords[:]):
            if self.graw_direction:
                self.coords[i][0] = coord[0] + self.offsets[i][0]
                self.coords[i][1] = coord[1] + self.offsets[i][1]
                self.current_graw_value += 1
            else:
                self.coords[i][0] = coord[0] - self.offsets[i][0]
                self.coords[i][1] = coord[1] - self.offsets[i][1]
                self.current_graw_value -= 1

    def get_offsets(self):
        offsets = {}
        for i, coord in enumerate(self.coords):
            offset_x = coord[0] - self.center[0]
            offset_y = coord[1] - self.center[1]
            if offset_x > 0:
                if offset_x > offset_y:
                    res_offset_x = 1
                else:
                    res_offset_x = math.fabs(offset_x / offset_y)
            else:
                if offset_x > offset_y:
                    res_offset_x = -1
                else:
                    res_offset_x = -math.fabs(offset_x / offset_y)
            if offset_y > 0:
                if offset_y > offset_x:
                    res_offset_y = 1
                else:
                    res_offset_y = math.fabs(offset_y / offset_x)
            else:
                if offset_y > offset_x:
                    res_offset_y = -1
                else:
                    res_offset_y = -math.fabs(offset_y / offset_x)
            offsets[i] = [res_offset_x, res_offset_y]
        print(offsets)
        return offsets

    @staticmethod
    def avg(ls):
        return sum(ls) / len(ls)


class Square(Polygon):
    def __init__(self, middle_point, side_length, ttl, color, max_graw_value=70):
        mediana = side_length / 2
        coords = [
            [middle_point[0] + mediana, middle_point[1] + mediana],
            [middle_point[0] + mediana, middle_point[1] - mediana],
            [middle_point[0] - mediana, middle_point[1] - mediana],
            [middle_point[0] - mediana, middle_point[1] + mediana],
        ]
        super().__init__(coords, ttl, color, max_graw_value=max_graw_value)


class Triangle(Polygon):
    def __init__(self, coords, ttl, color):
        super().__init__(coords[:3], ttl, color)


def draw_rect(ttl):
    x = random.randint(-200, 200) #получаем случайные координаты
    y = random.randint(-200, 200)

    ttl.color('red')    # устанавливаем цвет линии
    ttl.penup()         # убираем "ручку" от холста, чтобы переместить в нужное место
    ttl.setpos(x, y)    # перемещаем на первую вершину
    ttl.pendown()       # опускаем ручку обратно
    ttl.goto(x + 50, y) # проводим линии для сторон четырёхугольника
    ttl.goto(x + 50, y + 50)
    ttl.goto(x, y + 50)
    ttl.goto(x, y)


def draw_circle(ttl):
    x = random.randint(-200, 200) #получаем случайные координаты
    y = random.randint(-200, 200)

    ttl.color('violet')     # устанавливаем цвет линии
    ttl.penup()             # убираем "ручку" от холста, чтобы переместить в нужное место
    ttl.setpos(x, y)        # перемещаем в "основание" - это будет самая низкая точка
    ttl.pendown()           # опускаем ручку обратно

    ttl.circle(25)          # рисуем круг радиуса 25


def main():

    turtle.tracer(0, 0)  # устанавливаем все задержки в 0, чтобы рисовалось мгновенно
    turtle.hideturtle()  # убираем точку посередине

    ttl = turtle.Turtle()  # создаём объект черепашки для рисования
    ttl.hideturtle()      # делаем её невидимой
    circle_1 = Circle([0, 340], ttl, 'red', 50)
    circle_2 = Circle([0, 0], ttl, 'violet', 20)
    circle_3 = Circle([80, 120], ttl, 'blue', 30)
    circle_4 = Circle([70, 110], ttl, 'blue', 10)
    circle_5 = Circle([170, 170], ttl, 'red', 60)
    five_polygon = Polygon([[-50, -50], [50, -50], [75, 0], [50, 50],
                            [-50, 50]], ttl, 'blue')
    star = Polygon([[-30, -55], [0, 35], [30, -55], [-50, 0], [50, 0]], ttl,
                   'green')
    star.lift_up(-150)
    square = Square([-100, -100], 50, ttl, 'yellow')
    triangle = Triangle([[-150, -150], [50, -200], [25, -70]], ttl, 'grey')
    while True:
        time.sleep(.01) # засыпаем, чтобы увидеть что нарисовали
        ttl.clear()     # очищаем всё нарисованое ранее
        circle_1.draw()
        circle_1.move_horizont()
        circle_2.draw()
        circle_2.grow()
        circle_3.draw()
        circle_3.rotate([0, 0], 2)
        circle_4.draw()
        circle_4.rotate([170, 170], 2)
        circle_5.draw()
        five_polygon.draw()
        five_polygon.move_horizont()
        five_polygon.rotate(3)
        # five_polygon.grow()
        star.draw()
        star.rotate(3)
        star.move_horizont()
        square.draw()
        # square.rotate(1)
        square.grow()
        square.move_horizont()
        square.rotate(2)
        triangle.draw()
        triangle.grow()
        turtle.update()  # т.к. мы сделали turtle.tracer(0, 0), нужно обновить экран, чтобы увидеть нарисованное

if __name__ == '__main__':
    main()
