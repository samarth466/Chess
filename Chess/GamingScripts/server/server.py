import socket
import threading
import pickle

from chess import Board, Player
from pygame.display import set_mode
from chess.CONSTANTS import WINDOW_WIDTH, WINDOW_HEIGHT, SQUARE_WIDTH, SQUARE_HEIGHT

PORT = 5050
MESSAGE_SIZE = 4096
FORMAT = 'UTF-8'
SERVER = socket.gethostbyname(socket.gethostname)
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_clients(connections: list, addresses: list):
    players = {
        WHITE: connections[0],
        BLACK: connections[1]
    }
    window = set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    name = connections[0].recv(MESSAGE_SIZE).decode(FORMAT)
    if name == DISCONNECT_MESSAGE:
        connections[0].send("Message Recieved.".encode(FORMAT))
        connections[1].send("Opponent left.".encode(FORMAT))
        connections[0].close()
        return
    player1 = Player(name, WHITE)
    name = connections[1].recv(MESSAGE_SIZE).decode(FORMAT)
    if name == DISCONNECT_MESSAGE:
        connections[1].send("Message Recieved.".encode(FORMAT))
        connections[0].send("Opponent left.".encode(FORMAT))
        connections[1].close()
        return
    player2 = Player(name, BLACK)
    board = Board((WINDOW_WIDTH, WINDOW_HEIGHT), SQUARE_WIDTH,
                  SQUARE_HEIGHT, player1, player2, window)
    data = pickle.dumps(board.squares, -1)
    for conn in connections:
        conn.send(data)
    conn = players[board.get_current_player().color]
    while True:
        move = conn.recv(MESSAGE_SIZE).decode()
        message = board.move(move)
        if message == "Invalid move!":
            conn.send(message)
        else:
            break
    try:
        name = board.find_player_by_color(board.end()).username
        for conn in connections:
            conn.send(f"{name} won!".encode(FORMAT))
        return
    except:
        pass


def start() -> None:
    server.listen()
    addresses = connections = []
    while True:
        conn, addr = server.accept()
        connections.append(conn)
        addresses.append(addr)
        if len(connections) == 2:
            thread = threading.Thread(
                target=handle_clients, args=(connections, addresses))
            connections = addresses = []
            thread.start()
        else:
            conn.send("Waiting for opponent".encode(FORMAT))
