from game import Game
from player import AiPlayer


def main():
    if __name__ == '__main__':
        game1 = Game([AiPlayer('Оптимус Прайм'), AiPlayer('Мегатрон'), AiPlayer('Бендер')])
        game1.go()
if __name__ == '__main__':
    main()
