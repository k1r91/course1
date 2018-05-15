import os, sys, shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def print_help(*args):
    help_func = {
    'help': 'help: view this help',
    'make_dir': 'mkdir <dirname>: make directory in current directory',
    'remove_dir': 'rm <dirname>: remove directory in current directory',
    'ls': 'ls: list files and directories in current directoy',
    'dir': 'dir: alias for ls',
    'cd': 'cd <directory>: change working directory',
    'home': 'home: change working directory to this script folder',
    }
    def print_full_help():
        print()
        for text in help_func.values():
            print(text)
        print()
    try:
        arg = args[0]
        if help_func.get(arg):
            print(help_func[arg])
        else:
            print('Implementation of "{}" function doesn\'t exists.'.format(arg))
            print("See the full list of commands:")
            print_full_help()
    except IndexError:
        print_full_help()


def make_dir(*args):
    try:
        dir_name = args[0]
        try:
            os.mkdir(dir_name)
            print('Directory {} created.'.format(dir_name))
        except FileExistsError:
            print('Directory {} already exist.'.format(dir_name))
    except IndexError:
        print_help('make_dir')


def remove_dir(*args):
    try:
        dir_name = args[0]
        try:
            os.rmdir(dir_name)
            print('Directory {} removed'.format(dir_name))
        except FileNotFoundError:
            print('Directory {} not found'.format(dir_name))
    except IndexError:
        print_help('remove_dir')

def list_dir(*args):
    files = []
    dirs = []
    for entry in os.scandir(os.getcwd()):
        if entry.is_file():
            files.append(entry)
        else:
            dirs.append(entry)
    for entry in dirs:
        print('<DIR>{:>30}'.format( entry.name))
    for entry in files:
        print('<FILE>{:>30}'.format(entry.name))


def change_dir(*args):
    try:
        dir_to_change = args[0]
        try:
            os.chdir(dir_to_change)
        except FileNotFoundError:
            print("Directory does not exist.")
        except NotADirectoryError:
            print("{} is not a directory.".format(dir_to_change))
    except IndexError:
        print_help('cd')


def home():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))


commands = {
    "help": print_help,
    "mkdir": make_dir,
    "rm": remove_dir,
    "ls": list_dir,
    "dir": list_dir,
    "cd": change_dir,
    'home': home,
}


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