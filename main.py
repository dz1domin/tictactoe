from game import Game

# todo: handle inputs
# todo: base game loop and player prompts
# todo: randomizing who goes first and attributing win accordingly


def main():
    game = Game()
    game.start_game()

# board = tttBoard()
#
# board.set_point(0, 0, ' ')
# board.set_point(0, 1, ' ')
# board.set_point(0, 2, 'X')
# board.set_point(1, 0, ' ')
# board.set_point(1, 1, 'X')
# board.set_point(1, 2, ' ')
# board.set_point(2, 0, 'X')
# board.set_point(2, 1, ' ')
# board.set_point(2, 2, ' ')
#
# print(board.get_boardstate())
#
# print()
#
# print(board.is_over())


if __name__ == '__main__':
    main()
