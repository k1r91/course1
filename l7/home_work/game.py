import random
from player import WinnerException, LoserException, Player, AiPlayer
from card import Card


class Game:
    def __init__(self, players):
        self.players = players
        self.barrels = list(range(1, 91))
        random.shuffle(self.barrels)

    def __str__(self):
        return "{}".format(self.barrels)

    def go(self):
        i = 1
        while self.barrels:
            barrel = self.barrels.pop()
            print('*' * 40)
            print("Ход № {}. Выпал бочонок № {}. Карточки:".format(i, barrel))
            try:
                for player in self.players:
                    print(player.card)
                    player.strike(barrel)
            except (WinnerException, LoserException) as e:
                print(e)
                break
            i += 1


if __name__ == '__main__':
    game1 = Game([Player('Кирилл'), AiPlayer('Мегатрон')])
    game1.go()
