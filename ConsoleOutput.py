

class ConsoleOutput:

    def welcome(self):
        print("Welcome in TicTacToe!")

    def draw_board(self, board, dim):
        for i in range(dim):
            if i != 0:
                for k in range(dim - 1):
                    print('--+', end='')
                print('--')
            for j in range(dim):
                if j < dim - 1:
                    print(''.join(board[i][j]), '|', end='')
                else:
                    print(''.join(board[i][j]))
        else:
            return True

    def player_move(self, player):
        print("Player", player, "move")

    def get_coord(self, coord):
        print("Coordinate {}:".format(coord))

    def wrong_coord(self, dim):
        print("Wrong value! Coordinates have to be integer from 1 to {}".format(dim))

    def wrong_move(self):
        print("Wrong move!")

    def congratulate_winner(self, winner):
        print("Congratulate", winner, "player, you win!")

    def announce_draw(self):
        print("It's a draw!")
