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

    def set_point(self, x, y, character):
        self.boardState[x][y] = character
