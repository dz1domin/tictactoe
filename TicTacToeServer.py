from TicTacToeBoard import TicTacToeBoard
from ConsoleOutput import ConsoleOutput
from ConsoleInput import ConsoleInput
from random import choice
from TicTacToePlayers import TicTacToePlayers
import socket


def main():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5005
    BUFFER_SIZE = 512
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    player_list = []

    while len(player_list) < 2:
        conn, addr = s.accept()
        player_list.append(TicTacToePlayers(addr, TCP_PORT, 'Player' + str(len(player_list)), conn))
        data = conn.recv(BUFFER_SIZE)
        print(addr, conn, data)


if __name__ == '__main__':
    main()
