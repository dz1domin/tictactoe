from tttBoard import tttBoard

board = tttBoard()
board.draw_board()

board.set_point(0, 0, 'X')
board.set_point(0, 1, 'X')
board.set_point(0, 2, 'X')
board.set_point(1, 0, 'X')
board.set_point(1, 1, 'X')
board.set_point(1, 2, 'X')
board.set_point(2, 0, 'X')
board.set_point(2, 1, 'X')
board.set_point(2, 2, 'X')

print()

board.draw_board()
