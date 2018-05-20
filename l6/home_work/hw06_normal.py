import re
# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

# Подсказка: обратите внимание на примеры в директории examples.


class Human:
    def __init__(self, name, surname, birthday):
        self.name = name
        self.surname = surname
        self.birthday = birthday

    def __str__(self):
        s = '{} {} {}'.format(self.name, self.surname, self.age)
        return s


class Father(Human):

    def __init__(self, name, surname, birthday):
        super().__init__(name, surname, birthday)
        self.sex = 'male'


class Mother(Human):

    def __init__(self, name, surname, birthday):
        super().__init__(name, surname, birthday)
        self.sex = 'female'


class Student(Human):
    def __init__(self, name, surname, age, classroom, school):
        super().__init__(name, surname, age)
        self.class_room = classroom
        self.school = school
        self.mother = None
        self.father = None

    def set_parents(self, mother, father):
        self.mother = mother
        self.father = father

    def up_class_room(self):
        self.classroom.up()


class ClassRoom:

    def __init__(self, numeral, letter, school, cabinet=None):
        self.numeral = numeral
        self.letter = letter
        self.cabinet = cabinet

    def up(self):
        self.numeral += 1

    def __str__(self):
        return '{}{} - кабинет № {}'.format(self.numeral, self.letter, self.cabinet)

    def __repr___(self):
        return str(self)


class Teacher(Human):
    def __init__(self, name, surname, birthday, subject):
        super().__init__(name, surname, birthday)
        self.subject = subject


def get_classrooms(data, school):
    classrooms = {}
    cabinet = 100
    for room in data:
        number = int(re.findall(r'\d+', room)[0])
        letter = re.findall(r'[А-Я]+', room)[0]
        classrooms[room] = ClassRoom(number, letter, school, cabinet)
        cabinet += 1
    return classrooms


def main():
    school = 'Начальная школа № 170'
    subjects_data = ['Математика', 'Литература', 'Русский язык', 'Физкультура', 'ИЗО', 'Труд']
    teachers = [Teacher('Алексей', 'Петров', '25.01.1987', subjects_data[0]),
                Teacher('Светлана', 'Морозова', '26.02.1973', subjects_data[1]),
                Teacher('Владимир', 'Путин', '01.08.1963', subjects_data[2]),
                Teacher('Ангела', 'Меркель', '12.12.1992', subjects_data[3]),
                Teacher('Сергей', 'Навальный', '15.01.1982', subjects_data[4]),
                Teacher('Алексей', 'Навальный', '17.02.1979', subjects_data[5]),
                ]
    classrooms_data = ['1А', '1Б', '1В', '1Г', '2А', '2Б', '2В', '2Г', '3А', '3Б', '3В', '3Г']
    # get all classrooms
    classrooms = get_classrooms(classrooms_data, school)

if __name__ == '__main__':
    main()
