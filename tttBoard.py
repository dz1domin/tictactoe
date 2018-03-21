class tttBoard:
    boardState = []
    dim = 3

    def __init__(self):
        self.boardState = [[[' '] for _ in range(self.dim)] for _ in range(self.dim)]

    def draw_board(self):
        for i in range(self.dim):
            if i != 0:
                for k in range(self.dim - 1):
                    print('--+', end='')
                print('--')
            for j in range(self.dim):
                if j < self.dim - 1:
                    print(''.join(self.boardState[i][j]), '|', end='')
                else:
                    print(''.join(self.boardState[i][j]))
        else:
            return True

    def set_point(self, x, y, character):
        self.boardState[x][y] = character
        if self.boardState[x][y] == character:
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

        for i in range(self.dim):
            for j in range(self.dim):

                if self.boardState[i][j] == 'X':
                    horizontal_x += 1
                elif self.boardState[i][j] == 'O':
                    horizontal_o += 1

                if self.boardState[j][i] == 'X':
                    vertical_x += 1
                elif self.boardState[j][i] == 'O':
                    vertical_o += 1

            if self.boardState[i][i] == 'X':
                diagonal1_x += 1
            elif self.boardState[i][i] == 'O':
                diagonal1_o += 1

            if self.boardState[i][-i - 1] == 'X':
                diagonal2_x += 1
            elif self.boardState[i][-i - 1] == 'O':
                diagonal2_o += 1

            if horizontal_x == self.dim or horizontal_o == self.dim:
                check = True
                return check

            if vertical_x == self.dim or vertical_o == self.dim:
                check = True
                return check

            if diagonal1_x == self.dim or diagonal1_o == self.dim:
                check = True
                return check

            if diagonal2_x == self.dim or diagonal2_o == self.dim:
                check = True
                return check

            horizontal_o = 0
            horizontal_x = 0
            vertical_o = 0
            vertical_x = 0
        return check
