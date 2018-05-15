# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil


from hw05_easy import list_dir
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def change_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    os.chdir(dir_name)
    print("Директория изменена на {}".format(os.getcwd()))


def copy_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    full_path = os.path.join(os.getcwd(), dir_name)
    if os.path.isfile(full_path):
        suffix = input("Введите желаемый суффикс для копии: ")
        shutil.copy2(full_path, full_path + suffix)
    else:
        print("Исходное имя должно быть файлом")
        return

def remove_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    full_path = os.path.join(os.getcwd(), dir_name)
    if os.path.isfile(full_path):
        question = input("Вы уверены что хотите удалить файл {}? y/n ".format(dir_name))
        if question == 'y':
            os.remove(full_path)
            print("Файл {} успешно удалён".format(dir_name))
        else:
            return
    else:
        print("Исходное имя должно быть файлом")
        return


def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cd": change_dir,
    "ls": list_dir,
    "rm": remove_file,
    "cp": copy_file,
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")