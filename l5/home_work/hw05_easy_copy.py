import os, sys, shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def make_dirs():
    for i in range(1, 10):
        try:
            os.mkdir(os.path.join(os.getcwd(), 'dir_{}'.format(i)))
        except FileExistsError:
            pass
def rm_dirs():
    for i in range(1, 10):
        try:
            os.rmdir(os.path.join(os.getcwd(), 'dir_{}'.format(i)))
        except FileNotFoundError:
            pass

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def scan_dir(path=os.getcwd()):
    for file in os.scandir(path):
        if file.is_dir():
            print(file.path)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_file(path=__file__):
    with open(path, 'r', encoding='utf-8') as file:
        f_name_lst = path.split('.')
        f_ext = '.' + f_name_lst[1]
        f_name = f_name_lst[0]
        f_name_tw = ''.join([f_name, '_copy', f_ext])
        full_path_tw = os.path.join(os.getcwd(), f_name_tw)
        with open(full_path_tw, 'w', encoding='utf-8') as file_tw:
            file_tw.write(file.read())
def copy_file_with_shutil(path=__file__):
    f_name_lst = path.split('.')
    f_ext = '.' + f_name_lst[1]
    f_name = f_name_lst[0]
    f_name_tw = ''.join([f_name, '_copy-shutil', f_ext])
    shutil.copy2(path, f_name_tw)

if __name__ == '__main__':
    # rm_dirs()
    make_dirs()
    scan_dir()
    copy_file()
    copy_file_with_shutil()