class ConsoleInput:

    def player_move(self, dim):
        coord = input()

        try:
            coord = int(coord)
        except ValueError:
            return False

        if 1 <= coord and coord <= dim:
            return coord

        return False

    def board_size(self):
        size = input()

        try:
            size = int(size)
        except ValueError:
            return False

        if size >= 3:
            return size

        return False