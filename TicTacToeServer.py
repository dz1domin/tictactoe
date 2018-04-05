from TicTacToeBoard import TicTacToeBoard
from ConsoleOutput import ConsoleOutput
from ConsoleInput import ConsoleInput
from random import choice
from TicTacToePlayers import TicTacToePlayers
import socket


def main():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5005
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    player_list = [TicTacToePlayers() for _ in range(2)]


if __name__ == '__main__':
    main()
