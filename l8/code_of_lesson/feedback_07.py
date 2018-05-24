
import classes as cl


def main():
    user_answer = True
    while user_answer:
        match = cl.Game()

        input_data = input("\nЕщё партейку?\n(Y/N): ").lower()
        # if input_data.lower() == "y":
        #     
            user_answer = input_data.lower() == "y"


if __name__ == "__main__":
    main()

main()

# ----------------------------------------------------------

class Card():

    temp = [random.randint(1, 90) for i in range(5)]    
    self.is_uniq(temp)

    def is_uniq(self, str):
        self.str = str
        for i in self.card:
            for j in self.str:
                if j in i:
                    self.str.remove(j)
                    self.str.append(random.randint(1, 90))
        return self.str

    @property
    def roll(self):
        self.barrel = random.randint(0, len(bag)-1)
        print('Новый бочонок: {} (осталось {})'
              .format(bag[self.barrel], len(bag)-1))
        return bag.pop(self.barrel)

    @property
    def __str__(self):
        if self.player == 'user':
            print('-' * 6, 'Ваша карточка', '-' * 6, '\n')
        else:
            print('-' * 2, 'Карточка компьютера', '-' * 2, '\n')
        for i in range(len(self.card)):
            for j in self.card[i]:
                print(j, end=' ')
            print('\n')
        print('-' * 25)

    @property
    def win_check(self):
        for i in self.card:
            for j in i:
                try:
                    int(j)
                except TypeError:
                    pass
                except ValueError:
                    pass
                else:
                    return True    


print('1. Начать игру')
print('2. Выход')
key = input('Введите номер пункта в меню ')
if key == '1':
    user = Card('user')
    comp = Card('comp')
    user.display
    comp.display
elif key == '2':
    sys.exit()

while True:
    x = user.roll
    #print('ВЫтащили', x)
    #print(bag)
    user.display
    comp.display
    if user.win_check != True:          # PEP-8
        print('Вы выиграли')
        sys.exit()
    if comp.win_check != True:
        print('Выиграл компьютер')
        sys.exit()


# random.sample(range(1, 91), 15)

# -------------------------------------------------------------

number = random.randint(1, 90)
while not self.is_unique_number(number, list_to_append):
    # если номер не уникальный, продолжаем его получать
    number = random.randint(1, 90)

def strike_out(self, number):
    for i in range(len(self.numbers)):
       # for j in range(len(self.numbers[i])):
            if self.numbers[i][j] == number:
                self.numbers[i][j] = self.strike

def __is_all_numbers_unique(self):
    '''
    Вспомогательный метод для проверки, все ли номера в карте получились уникальными.
    Возвращает True, если так, или первый попавшийся номер, который не уникален
    :return:
    '''
    for line in self.numbers:
        for number in line:
            if number == 0:
                continue
            tmp_line = line[:]
            tmp_line.remove(number)
            if number in tmp_line:
                return str(number)
            rest_lines = self.numbers[:]
            rest_lines.remove(line)
            for rest_line in rest_lines:
                if number in rest_line:
                    return str(number)
    return True                


def is_winner(self):
    '''
    Проверка, победила ли карточка
    :return:
    '''
    for line in self.numbers:
        for number in line:
            if number != 0 and str(number).isdigit():
                return False
    return True    



class Game:
    '''
    Игру можно запустить в режиме симуляции,
    задав параметр mode=1 в объявлении класса
    '''
    def __init__(self, user_card, cpu_card, mode=0):
        self.user_card = user_card
        self.cpu_card = cpu_card
        self.turn = 0
        self.barrels = list(range(1, 91))
        self.winner = None
        self.mode = mode
        if self.mode not in [0, 1]:
            raise ValueError("use mode = 0 for standart game or mode = 1 for simulation game")
    @time_it
    def start(self)



def main():
    if __name__ == '__main__':
        usr_card = Card("--Пользовательская карточка--", "Пользователь")
        cpu_card = Card("-----Карточка компьютера-----", "Компьютер")
        game = Game(usr_card, cpu_card, mode=0)
        game.start()

main()


# ----------------------------------------------------------


def __str__(card):
    '''
    Функция для печати карточки
    :param card: 
    :return: 
    '''
    print(9 * '{:^3} '.format('---'))
    for i, v in enumerate(card[:], 1):
        if v == 0:
            v = '.'
        elif v == -1:
            v = '-'
        if i % 9:
            print('{:^3}'.format(v), sep='', end=' ')
        else:
            print('{:^3}'.format(v), sep='', end='\n')
    print(9 * '{:^3} '.format('---'))


 while len(bag1) > 0 and \
        len([i for i in card_user[:] if i > 0]) > 0 and \
         len([i for i in card_pc[:] if i > 0]) > 0:
    curr_barrel = bag1.pop()
    print('Новый бочонок: {} (осталось {})'.format(curr_barrel, len(bag1)))
    print('\n----------- Ваша карточка ---------')
    print_card(card_user)
    print('\n-------- Карточка компьютера ------')
    print_card(card_pc)
    answer = input('Зачеркнуть цифру? (y/n)')   

# -----------------------------------------------------------------

class Game:

    def game_over(self, num_keg):
        answer = input('Зачеркнуть цифру? (y/n)\n')
        if answer == 'y':
            if not Game.search_number(self, num_keg, self.carta_person, 1):
                print('Вы проиграли')
                sys.exit()
        elif answer == 'n':
            if Game.search_number(self, num_keg, self.carta_person, 1):
                print('Вы проиграли')
                sys.exit()
        elif answer != 'y' and answer != 'n':
            print('Повторите ввод')
            Game.game_over(self, num_keg)


# ----
if my_flag_work and check_element(card_user.card_list, barrel):
    card_user.remove_number(barrel)
    card_user.card_number -= 1

# Пользователь ошибся
elif ((my_flag_work and not check_element(card_user.card_list, barrel)) or 
    not my_flag_work and check_element(card_user.card_list, barrel)):
    flag_game = False
    break

# Компьютер всегда делает правильный выбор: есть число - зачеркивает, нету - продолжает
if check_element(card_computer.card_list, barrel):
    card_computer.remove_number(barrel)
    card_computer.card_number -= 1

# -------


if self.comp_kegs == 15 and self.person_kegs == 15:
    print('Ничья')
elif self.comp_kegs == 15:
    print('Победил компьютер')
elif self.person_kegs == 15:
    print('Вы победили')

# ------------------------------------------------------------

class UserCard:

def __init__(self):
    self.card_list = []


    self.card_list_for_print = list(self.card_list)
    for string in self.card_list_for_print:    
        for i in range(4):
            string.insert(random.randint(0, 8), 'a')    


def __str__(self):
    text = self.print_belong_card() + '\n'
    for string in self.card_list_for_print:
        for i in string:
            if i == 'a':
                text += '   '
            else:
                text += '{:>2} '.format(i)
        text += '\n'                
    return text          


    def remove_number(self, number):  
        for string in self.card_list:
            for i, element in enumerate(string):
                if element == number:
                    string[i] = '-'
        return self.card_list  



class ComputerCard(UserCard):   
    """Класс карточки компьютера

    print_belong_card() - переопределенный метод "родителя"

    """    
    def __init__(self):
        super().__init__()
    
    def print_belong_card(self):
        return "-- Карточка компьютера ---"


while flag_question:
    continue_question = str(input('{} (y/n)\n'.format(text)))   
        
    if continue_question in ['y', 'n']:
            
        if continue_question == 'y':
            flag_question = False
            return True
            
        else:
            flag_question = False
            return False
    else:
        print('Некорректный ввод. Попробуйте еще раз\n')        


elif len(barrels) == 0 and card_user.card_number > 0 and card_computer.card_number > 0:
    return '\nНикто не выиграл и не проиграл'

# --------------------------------------------------------------------------

class Card:
    def __init__(self):
        self.bagnums   = [ x for x in range(1,91) ]     # Мешок с бочками
        self.cardnums  = random.sample(range(1,91), 15) # Номера на карточке

    def step(self) :
        print( '\nВы:' )
        self.print_card()
        n = random.choice( self.bagnums )  # Вытащили бочонок из мешка
        self.bagnums.remove( n )           # Вытащили без возврата
        answer = None
        while answer != 'c' and answer != 'd' : # Дождемся правильного ответа
            answer = input('Номер ' + str(n) + ': Зачеркнуть(d)/продолжить(c):')
        if answer == 'd' :
           if n in self.cardnums :       #
              self.cardnums.remove( n )  # Номер закрываем бочеой
              self.card[ self.card.index(str(n)) ] = 'XX'
              return True
           else : 
              print( 'Вы проиграли!')
              return False
        elif answer == 'c' :
           if n in self.cardnums :
              print( 'Вы проиграли!')
              return False
           else : return True
        else : self.step()
            
    def autostep(self) :
        # Все то же, что и в предыдущем случае, но в надежде, 
        # что компьютер не ошибается          


# --------------------------------------------------------------------------

    def pop_item(self, item):
        try:
            self.__lotto_card.remove(int(item))
        except KeyError:
            print('Такого числа нет в вашей карте')
            print('Вы проиграли')
            sys.exit()

        ind = self.__lotto_list.index(item)
        self.__lotto_list[ind] = '--'

        if not self.__lotto_card:
            print('Все числа закрыты')
            if self.__mode == ' Карточка компьютера ':
                print("Компьютер победил!")
            else:
                print('Вы победили!')
            sys.exit()        

# -------------------------------------------------

MAX_NUMBER = 90

class CardAndBarrel:
    def __init__(self, n=MAX_NUMBER, MIN_NUMBER=1, NUMBER_BARREL=90):
        self._MAX_NUMBER = MAX_NUMBER
        self._MIN_NUMBER = MIN_NUMBER
        self._NUMBER_BARREL = NUMBER_BARREL


class PlayGame:
    def __init__(self, card_user, card_comp, play_barrel, player):
        self.card_user = list(itertools.chain(*card_user))
        self.card_comp = list(itertools.chain(*card_comp))
        self.play_barrel = play_barrel
        self.player = player

    def play(self):
        regulations = True
        count = 1
        while regulations == True:          # PEP-8
            num_barrel = str(play_barrel[count])
            if len(num_barrel) < 2:            


# -----------------------------------------------------

def fight(ck, uk):
    global count_kegs
    global used_kegs
    number = random.randint(1, 90)
    if number in used_kegs:
        fight()
    used_kegs.append(number)
    count_kegs -= 1                


# -----------------------------------------------------
# Вытаскивание произвольного бочонка
ls = [i for i in range(1, 91)]
def barrel(list):
    barrel_list = list
    if len(barrel_list) > 0:
        number = random.randint(0, len(barrel_list) - 1)
        print('Новый бочонок: {} (осталось {})'.format(barrel_list[number],len(barrel_list) - 1))
        ls.pop(number)
        return number    

def card_print(card, name):
    list_num = card
    nm = name
    print("{}".format(nm).center(26, "-"))
    print('{0[0]:>2} {0[1]:>2} {0[2]:>2} {0[3]:>2} {0[4]:>2} {0[5]:>2} {0[6]:>2} {0[7]:>2} {0[8]:>2}'.format(*list_num))
    print('{1[0]:>2} {1[1]:>2} {1[2]:>2} {1[3]:>2} {1[4]:>2} {1[5]:>2} {1[6]:>2} {1[7]:>2} {1[8]:>2}'.format(*list_num))
    print('{2[0]:>2} {2[1]:>2} {2[2]:>2} {2[3]:>2} {2[4]:>2} {2[5]:>2} {2[6]:>2} {2[7]:>2} {2[8]:>2}'.format(*list_num))
    print("".center(26, "-"))



if count_computer == 15:
    print('Выиграл компьютер!')
else:
    print('Выиграл игрок!')

# --------------------------------------------------------

    def isincard(self, nmbr):
        return nmbr in self.card
        #     return True
        # else:
        #     return False

# --------------------------------------
    self.card = sorted(self.card[0:5]) + sorted(self.card[5:10]) \
                    + sorted(self.card[10:]) 

    def __str__(self):
        return self.name + "\n" \
               + " ".join([str(i) for i in self.card[0:5]]) + "\n" \
               + " ".join([str(i) for i in self.card[5:10]]) + "\n" \
               + " ".join([str(i) for i in self.card[10:]]) + "\n"            

# -------------------------------------------------------


def card_list(card):
    print ('     {}       {}    {}      {}           {}'.format(card[0][0], card[0][1], card[0][2], card[0][3], card[0][4]))
    print (' {}       {}     {}         {}     {}      '.format(card[1][0],card[1][1],card[1][2],card[1][3],card[1][4]))
    print ('     {}      {}     {}      {}     {}      '.format(card[2][0],card[2][1],card[2][2],card[2][3],card[2][4]))
    print(' - ' * 18)


def check_card(card1, card2):
   
    if card1[0] == card1[1] == card1[2] == ['--','--','--','--','--'] 
        print(' * '*18)
        print("Вы победили!!!")
        print(' * '*18)
        raise StopIteration
    if card2[0] == ['--','--','--','--','--'] and card2[1] == ['--','--','--','--','--'] and card2[2] == ['--','--','--','--','--']:
        print(' * '*18)
        print("Победил Компьютер!!!")
        print(' * '*18)
        raise StopIteration


functions.numbers(card1, c)
functions.card_list(card1)        
#------------------------------------------------------------

    def __str__(self, own):
        b = ''
        c = ''
        d = ''

        lines = [self.line_1, self.line_2, self.line_3 ]
        for line in lines:
            for i in line:
                if len(str(i)) == 2:
                    b = b + ' ' + str(i)
                else:
                    b = b + '  ' + str(i)
        
        return '\n{}\n {}\n {}\n {}\n'.format(own, b, c, d)

# ----------------------------------------------------------

    self.type = type

    def __str__(self):
        return "{0}\n{1}\n{2}".format(
            self.kegs.get_text_about_keg_curr(),
            self.player_card,
            self.computer_card
        )