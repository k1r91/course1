import os

# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


class Worker:

    def __init__(self, raw_data):
        data = raw_data.split()
        self.name = data[0]
        self.surname = data[1]
        self.salary = int(data[2])
        self.duty = data[3]
        self.clock_rate = int(data[4])
        self.hours_worked = 0

    def set_hours_worked(self, hours):
        self.hours_worked = int(hours)

    def __str__(self):
        return '{:<10} {:<10} {:<10} {:<15} {:<12} {:<17} {:<15.2f}'.format(
            self.name, self.surname,self.salary, self.duty, self.clock_rate,
            self.hours_worked, self.paid_salary)

    @property
    def paid_salary(self):
        if self.hours_worked == self.clock_rate:
            return self.salary
        elif self.hours_worked < self.clock_rate:
            return self.salary * self.hours_worked / self.clock_rate
        else:
            return (2 * self.hours_worked / self.clock_rate - 1) * self.salary


def print_salary(workers):
    print('{:<10} {:<10} {:<10} {:<15} {:<12} {:<17} {:<15}'.format(
        'Имя',
        'Фамилия',
        'Зарплата',
        'Должность',
        'Норма-часов',
        'Отработано часов',
        'Итоговая зарплата'
    ))
    for worker in workers:
        print(worker)


def main():
    workers = []
    with open(os.path.join('data','workers'), 'r', encoding='utf-8') as f:
        for line in f.readlines()[1:]:
            workers.append(Worker(line))
    with open(os.path.join('data', 'hours_of'), 'r', encoding='utf-8') as f:
        for line in f.readlines()[1:]:
            data = line.split()
            for worker in workers:
                if worker.name == data[0] and worker.surname == data[1]:
                    worker.set_hours_worked(data[2])
    print_salary(workers)
if __name__ == '__main__':
    main()