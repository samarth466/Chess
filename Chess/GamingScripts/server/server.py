import socket
import threading
import json
import random

from chess import Board, Player
from pygame.display import set_mode
from chess.CONSTANTS import WINDOW_WIDTH, WINDOW_HEIGHT, SQUARE_WIDTH, SQUARE_HEIGHT, BLACK, WHITE

PORT = 5050
MESSAGE_SIZE = 4096
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "Disconnect!"
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_clients(connections: list, addresses: list):
    boolean_choice = bool(random.randint(0, 1))
    players = {
        WHITE: connections[int(boolean_choice)],
        BLACK: connections[int(not boolean_choice)]
    }
    window = set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    name = players[WHITE].recv(MESSAGE_SIZE).decode(FORMAT)
    if name == DISCONNECT_MESSAGE:
        players[WHITE].send("Message Recieved.".encode(FORMAT))
        players[BLACK].send("Opponent left.".encode(FORMAT))
        players[WHITE].close()
        return
    player1 = Player(name, WHITE)
    name = players[BLACK].recv(MESSAGE_SIZE).decode(FORMAT)
    if name == DISCONNECT_MESSAGE:
        players[BLACK].send("Message Recieved.".encode(FORMAT))
        players[WHITE].send("Opponent left.".encode(FORMAT))
        players[BLACK].close()
        return
    player2 = Player(name, BLACK)
    board = Board((WINDOW_WIDTH, WINDOW_HEIGHT), SQUARE_WIDTH,
                  SQUARE_HEIGHT, player1, player2, window)
    data = json.dumps(
        {pos: square.piece.id for pos, square in board.squares.items()}).encode(FORMAT)
    for conn in connections:
        conn.send(data)
    current_turn = board.get_current_player()
    conn = players[current_turn.color]
    while True:
        move = conn.recv(MESSAGE_SIZE).decode()
        message = board.move(move, current_turn)
        if message == "Invalid move!":
            conn.send(f"{message} Please try again.".encode(FORMAT))
        else:
            conn.send(f"Successfully made move:\n{move}".encode(FORMAT))
            break
    try:
        name = board.find_player_by_color(board.end()).username
        for conn in connections:
            conn.send(f"{name} won!".encode(FORMAT))
        return
    except:
        for conn in connections:
            conn.send("".encode(FORMAT))


def start() -> None:
    server.listen()
    addresses = []
    connections = []
    while True:
        conn, addr = server.accept()
        connections.append(conn)
        addresses.append(addr)
        if len(connections) == 2:
            for conn in connections:
                conn.send("Starting game!".encode(FORMAT))
            thread = threading.Thread(
                target=handle_clients, args=(connections, addresses))
            connections = []
            addresses = []
            thread.start()
        else:
            conn.send("Waiting for opponent".encode(FORMAT))


if __name__ == "__main__":
    start()
