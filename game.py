from TicTacToeBoard import TicTacToeBoard
from ConsoleOutput import ConsoleOutput
from ConsoleInput import ConsoleInput
from random import choice


class Game:
    players = ['O', 'X']

    def __init__(self):
        self._dim = 3
        self._board = TicTacToeBoard(self._dim)
        self._input = ConsoleInput()
        self._output = ConsoleOutput()
        self._actual_player = choice(self.players)

    def start_game(self):
        self._output.welcome()
        self._output.draw_board(self._board.get_board_state(), self._dim)

        is_end = False
        while not is_end:
            is_end = self.player_make_move()


    def player_get_move(self):

        self._output.player_move(self._actual_player)
        self._output.get_coord('x')

        x = False
        while not x:
            x = self._input.player_move(self._dim)
            if x == False:
                self._output.wrong_coord(self._dim)

        self._output.get_coord('y')
        y = False
        while not y:
            y = self._input.player_move(self._dim)
            if y == False:
                self._output.wrong_coord(self._dim)
        return x-1, y-1

    def player_make_move(self):

        good_move = False
        while not good_move:
            move = self.player_get_move()
            good_move = self._board.set_point(move[0], move[1], self._actual_player)
            if not good_move:
                self._output.wrong_move()

        self._output.draw_board(self._board.get_board_state(), self._dim)

        if self._board.is_over():
            self._output.congratulate_winner(self._actual_player)
            is_end = True

        elif self._board.is_move_available():   # change player
            if self._actual_player == 'X':
                self._actual_player = 'O'
            else:
                self._actual_player = 'X'
            is_end = False

        else:
            self._output.announce_draw()
            is_end = True

        return is_end
