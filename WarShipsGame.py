import random
import time

class InputValidator:

    def validation(self):
        flag = False
        while flag == False:
            target = input('Выберите клетку нанесения удара(например Б4):\n')
            if target[0] in 'АБВГДЕЖЗИК' and target[1:] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                flag == True
                return target
            else:
                print('Неверно введены координаты клетки')
class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [['-' for _ in range(size)] for _ in range(size)]

    def print_board(self):
        letter_scale = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']
        print('  ', end='')
        for i in range(1, self.size+1):
            print(i, end=' ')
        print()
        for i in range(self.size):
            print(letter_scale[i], end=' ')
            for j in range(self.size):
                print(self.grid[i][j], end=' ')
            print()

    def place_ship(self, ship_size):
        while True:
            x = random.randint(0, self.size-1)
            y = random.randint(0, self.size-1)
            is_horyzontal = random.choice([True, False])
            if is_horyzontal:
                if y+ship_size <= self.size:
                    if all(self.grid[x][y+i] == '-' for i in range(ship_size)):
                        for i in range(ship_size):
                            self.grid[x][y+i] = 'O'
                        return
            else:
                if x + ship_size <= self.size:
                    if all(self.grid[x+i][y] == '-' for i in range(ship_size)):
                        for i in range(ship_size):
                            self.grid[x+i][y] = 'O'
                        return

class Game:
    def __init__(self, size=10):
        self.size = size
        self.board1 = Board(size)
        self.board2 = Board(size)
        self.ship_sizes = [1, 2]
        self.turn = 'first'
        self.gamer1 = input('Введите имя игрока №1\n')
        self.gamer2 = input('Введите имя игрока №2\n')
        self.game_over = False

    def start(self):
        for size in self.ship_sizes:
            self.board1.place_ship(size)
            self.board2.place_ship(size)
        print(f'Поле {self.gamer1}:')
        self.board1.print_board()
        print(f'\nПоле {self.gamer2}:')
        self.board2.print_board()
        self.play()

    def player_turn(self, board, player_name1, player_name2, turn1, turn2):
        print(f'Ход {player_name1}!')
        cell_change = InputValidator()
        target = cell_change.validation()
        if ord(target[0]) == 1050:
            x = ord(target[0]) - 1041
        else:
            x = ord(target[0]) - 1040
        y = int(target[1:]) - 1
        if board.grid[x][y] == 'O':
            print('Попал!')
            board.grid[x][y] = 'X'
            print(f'Поле игрока {player_name2}')
            board.print_board()
            if not any('O' in row for row in board.grid):
                print(f'{player_name1} побеждает!')
                print('Подравляем!')
                self.game_over = True
            return turn1

        else:
            board.grid[x][y] = '*'
            print('Мимо!')
            print(f'Поле игрока {player_name2}')
            board.print_board()
            return turn2



    def play(self):
        while self.game_over!= True:
            if self.turn == 'first':
                self.turn = game.player_turn(self.board2, self.gamer1, self.gamer2, 'first', 'second')
            elif self.turn == 'second':
                self.turn = game.player_turn(self.board1, self.gamer2, self.gamer1, 'second', 'first')

game = Game()
game.start()
