from copy import deepcopy


class TicTacToeBoard:

    def __init__(self, dim):
        self._dim = dim
        self._board_state = [[' ' for _ in range(self._dim)] for _ in range(self._dim)]

    def get_board_state(self):
        return deepcopy(self._board_state)

    # to bym wrzucił do klasy output, w ten sposób board nie jest zależny od outputu
    # który może być w konsoli, a równie dobrze w jakimś gui czy tym tcp
    # def draw_board(self):
    #     for i in range(self._dim):
    #         if i != 0:
    #             for k in range(self._dim - 1):
    #                 print('--+', end='')
    #             print('--')
    #         for j in range(self._dim):
    #             if j < self._dim - 1:
    #                 print(''.join(self._board_state[i][j]), '|', end='')
    #             else:
    #                 print(''.join(self._board_state[i][j]))
    #     else:
    #         return True

    def set_point(self, x, y, character):

        if self._board_state[x][y] == ' ':
            self._board_state[x][y] = character
            return True
        else:
            return False

    def is_over(self):
        check = False
        horizontal_x = 0
        vertical_x = 0
        horizontal_o = 0
        vertical_o = 0
        diagonal1_x = 0
        diagonal1_o = 0
        diagonal2_x = 0
        diagonal2_o = 0

        for i in range(self._dim):
            for j in range(self._dim):

                if self._board_state[i][j] == 'X':
                    horizontal_x += 1
                elif self._board_state[i][j] == 'O':
                    horizontal_o += 1

                if self._board_state[j][i] == 'X':
                    vertical_x += 1
                elif self._board_state[j][i] == 'O':
                    vertical_o += 1

            if self._board_state[i][i] == 'X':
                diagonal1_x += 1
            elif self._board_state[i][i] == 'O':
                diagonal1_o += 1

            if self._board_state[i][-i - 1] == 'X':
                diagonal2_x += 1
            elif self._board_state[i][-i - 1] == 'O':
                diagonal2_o += 1

            if horizontal_x == self._dim or horizontal_o == self._dim:
                check = True
                return check

            if vertical_x == self._dim or vertical_o == self._dim:
                check = True
                return check

            if diagonal1_x == self._dim or diagonal1_o == self._dim:
                check = True
                return check

            if diagonal2_x == self._dim or diagonal2_o == self._dim:
                check = True
                return check

            horizontal_o = 0
            horizontal_x = 0
            vertical_o = 0
            vertical_x = 0
        return check

    def is_move_available(self):
        for i in range(self._dim):
            for j in range(self._dim):
                if self._board_state[i][j] == ' ':
                    return True
        return False
