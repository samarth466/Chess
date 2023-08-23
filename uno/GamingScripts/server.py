import socket
import threading
from itertools import cycle
from queue import LifoQueue
from .utils import gen_deck, Player, shuffle_deck


# Socket Server
PORT = 5050
MESSAGE_SIZE = 4096
FORMAT = 'UTF-8'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
clients_in_games = 0


def handle_clients(connections,addresses):
    players = []
    deck = shuffle_deck(gen_deck())
    discard_pile = LifoQueue(112)
    while True:
        card = deck.get()
        if "Draw 2" not in card.role:
            discard_pile.put(card)
            break
        else:
            deck = bottom_card(card,deck)
    for i,connection in enumerate(connections):
        name = connection.recv(MESSAGE_SIZE).decode(FORMAT)
        players.append(Player(i,name,deck))
        cards = [(card.role,card.color) for card in players[i].hand]
        connection.send('; '.join(cards).encode(FORMAT))
    players = cycle(players)
    while True:
        player = next(players)
        try:
            msg = eval(connections[player.id].recv(MESSAGE_SIZE).decode(FORMAT))
            card = [card for card in player.hand if card.role == msg[0] and card.color == msg[1]][0]
            player.hand.remove(card)
            discard_pile.put(card)
            if "Draw 4" in card.role:
                pass