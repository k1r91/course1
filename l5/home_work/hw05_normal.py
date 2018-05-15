import hw05_easy as easy
import os, sys

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

if __name__ == '__main__':
    home = os.getcwd()
    print('Welcome to my small conslole utility! Type "help" to view posiible commands, type "exit" or "q" to exit.')
    while True:
        current_directory = os.getcwd()
        print(current_directory + ">")
        command = input()
        user_input = command.split()
        command = user_input[0]
        args = user_input[1:]
        if command in ['exit', 'q']:
            print("Exiting...")
            sys.exit(1)
        if easy.commands.get(command):
            easy.commands[command](*args)
        else:
            print('Unrecognized command. Type "help" to view posiible commands, type "exit" or "q" to exit.')