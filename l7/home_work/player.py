from card import Card


class WinnerException(Exception):
    def __init__(self, player):
        self.player = player

    def __str__(self):
        return "{} выиграл!".format(self.player.name)


class LoserException(Exception):
    def __init__(self, player, feedback=None):
        self.player = player
        self.feedback = feedback

    def __str__(self):
        s = "{} проиграл!".format(self.player.name)
        if self.feedback:
            s += self.feedback
        return s


class Player:

    def __init__(self, name):
        self.name = name
        self.card = Card("Карточка игрока")

    def __str__(self):
        return "Ходит {}:".format(self.name)

    def strike(self, num):
        answer = input("Ходит {}! Зачеркнуть? (y/n)".format(self.name))
        if answer == 'y':
            if self.card.strike(num):
                if self.card.is_all_striked:
                    raise WinnerException(self)
            else:
                raise LoserException(self, 'Вы попытались зачеркнуть не существующую в карточке цифру!')
        elif answer != 'n':
            raise LoserException(self, 'Неверный ответ!')
        else:
            if self.card.strike(num):
                raise LoserException(self, 'Такая цифра есть в вашей карточке!')


class AiPlayer(Player):
    def __init__(self, name):
        self.name = name
        self.card = Card("Карточка компьютера")
        self.card.name = "Карточка игрока {}".format(self.name)

    def strike(self, num):
        print("Ходит {}".format(self.name))
        if self.card.strike(num):
            print("Зачеркнуто: {}".format(num))
            if self.card.is_all_striked:
                raise WinnerException(self)
        else:
            print("Нечего зачеркивать!")