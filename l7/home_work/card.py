import random, os

class Card:

    def __init__(self, name):
        self.name = name
        self.card = self.create_card()

    @staticmethod
    def create_card():
        positions = random.sample(range(9), 5) + random.sample(range(9, 18), 5) + random.sample(range(18, 27), 5)
        numbers = random.sample(range(1, 91), 15)
        result = dict(zip(positions, numbers))
        return result

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

    