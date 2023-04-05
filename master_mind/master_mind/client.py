import socket
from utils import Player
from random import choice


class Person(Player):

    def _make_guess(self) -> list[str]:
        while True:
            guess = input(
                "What do you think the code is?: ").upper().split(' ')
            if len(guess) != self.CODE_LENGTH:
                print(
                    f"Your guess was not the correct length. The guess must have {self.CODE_LENGTH} items.")
                continue
            for color in guess:
                if color not in self.COLORS:
                    print(f"{color} is not a valid color. Please try again.")
                    break
            else:
                return guess

    def play(self, code: list[str] = None, message: str = "") -> tuple[list[str], str]:
        if self.status == 'code maker':
            pass
        elif self.status == 'code breaker':
            if message:
                print(message)
            guess = self._make_guess()
            return guess


# Socket Client
PORT = 5050
MESSAGE_SIZE = 4096
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = 'Disconnect'
HOST = '192.168.1.180'
ADDR = (HOST, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def game() -> None:
    while True:
        print("Welcome to Master Mind")
        mode = "PV" + \
            input("Do you want to play against the computer or another player? (P for another player, C for computer): ").upper()
        client.send(mode.encode(FORMAT))
        player = Person("code breaker")
        print(f"You have {player.TRIES} attempts to guess the code.")
        turns_left = player.TRIES
        if mode == 'PVC':
            guess = ' '.join(player.play())
            while True:
                turns_left -= 1
                print(f"You have {turns_left} turns left to guess the code!")
                client.send(guess.encode(FORMAT))
                message = client.recv(MESSAGE_SIZE).decode(FORMAT)
                if 'won' in message:
                    print(message)
                    break
                msg = client.recv(MESSAGE_SIZE).decode(FORMAT)
                if msg:
                    print(msg)
                    break
                guess = ' '.join(player.play(message=message))
        else:
            pass
        replay = input("Do you want to play again? Y/N: ").upper()
        if replay == 'N':
            client.close()
            break


if __name__ == "__main__":
    game()
