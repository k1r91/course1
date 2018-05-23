import random
import os


class Card:
    def __init__(self, name):
        self.name = name
        self.card = self.create_card()

    def create_card(self):
        numbers = random.sample(range(1, 91), 15)
        positions = self.rnd_positions(0, 9, 5) + self.rnd_positions(9, 18, 5) + self.rnd_positions(18, 27, 5)
        numbers = sorted(numbers[:5]) + sorted(numbers[5:10]) + sorted(numbers[10:15])
        return dict(zip(positions, numbers))

    @staticmethod
    def rnd_positions(start, end, count):
        return sorted(random.sample(range(start, end), count))

    def __str__(self):
        result = "-------{:^22}-------{}".format(self.name, os.linesep)
        for i in range(27):
            number = self.card.get(i)
            if number:
                result = ''.join([result, '|{:<2}|'.format(number)])
            else:
                result = ''.join([result, '|  |'])
            if (i + 1) % 9 == 0:
                result = ''.join([result, os.linesep])
        return result

    def strike(self, num):
        if num in self.card.values():
            for item, value in self.card.items():
                if value == num:
                    self.card[item] = '--'
            return True
        return False

    @property
    def is_all_striked(self):
        for value in self.card.values():
            if value != '--':
                return False
        return True

    def strike_all(self):
        for item, value in self.card.items():
            self.card[item] = '--'


def main():
    user_card = Card('Карточка пользователя')
    cpu_card = Card('Карточка компьютера')
    print(user_card)
    print(cpu_card)

if __name__ == '__main__':
    main()