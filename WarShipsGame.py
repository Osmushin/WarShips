import random

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
        self.ship_sizes = [5, 4, 3, 3, 2]
        self.turn = 0

    def start(self):
        for size in self.ship_sizes:
            self.board1.place_ship(size)
            self.board2.place_ship(size)
        print('Поле игрока № 1:')
        self.board1.print_board()
        print('\nПоле игрока № 2:')
        self.board2.print_board()
        self.play()

    def play(self):
        while True:
            if self.turn == 0:
                print('Ход игрока №1:')
                grid_change = InputValidator()
                target = grid_change.validation()
                if ord(target[0]) == 1050:
                    x = ord(target[0])-1041
                else:
                    x = ord(target[0])-1040
                y = int(target[1]) - 1
                if self.board2.grid[x][y] == 'Ó':
                    print('Попал!')
                    self.board2.grid[x][y] = 'X'
                    self.board2.print_board()
                    if not any('O' in row for row in self.board2.grid):
                        print('Игрок 1 побеждает!')
                        break
                else:
                    self.board2.grid[x][y] = '*'
                    print('Мимо!')
                    self.board2.print_board()
                self.turn = 1
            else:
                print('Ход игрока №2:')
                grid_change = InputValidator()
                target = grid_change.validation()
                if ord(target[0]) == 1050:
                    x = ord(target[0])-1041
                else:
                    x = ord(target[0])-1040
                y = int(target[1]) - 1
                if self.board1.grid[x][y] == 'Ó':
                    print('Попал!')
                    self.board1.grid[x][y] = 'X'
                    self.board1.print_board()
                    if not any('O' in row for row in self.board1.grid):
                        print('Игрок 1 побеждает!')
                        break
                else:
                    self.board1.grid[x][y] = '*'
                    print('Мимо!')
                    self.board1.print_board()
                self.turn = 1

game = Game()
game.start()
