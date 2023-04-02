import socket
import threading
from utils import Player
from random import choice


class Computer(Player):

    def _guess_code(self, guess: list[str]) -> str:
        for color in guess:
            if color not in self.COLORS:
                return f"{color} is not a valid color."
        return ""

    def play(self, code: list[str] = None, message: str = "") -> tuple[list[str], str]:
        if self.status == 'code maker':
            if not code:
                code = self._generate_code()
            elif message:
                guess = message.split(' ')
                correct_pos, incorrect_pos = self._check_code(guess, code)
                if correct_pos == self.CODE_LENGTH:
                    return code, "You won."
                message = f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}"
                return code, message
            return code, message
        elif self.status == 'code breaker':
            pass


# Socket Server
PORT = 5050
MESSAGE_SIZE = 4096
FORMAT = 'UTF-8'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
clients_in_games = 0


def handle_client(connection: socket.socket, address: tuple[str, str]):
    print(f"{address} connected")
    message = connection.recv(MESSAGE_SIZE).decode(FORMAT)
    if message == 'Disconnect':
        connection.send("Message received.".encode(FORMAT))
        connection.close()
    if message.upper() == 'PVC':
        computer = Computer('code maker')
        code, msg = computer.play()
        for attempt in range(1, computer.TRIES+1):
            print(attempt)
            message = connection.recv(MESSAGE_SIZE).decode(FORMAT)
            if message == 'Disconnect':
                connection.send("Message Received.".encode(FORMAT))
                break
            guess = message.upper()
            code, msg = computer.play(code, guess)
            if msg == 'You won.':
                msg += f' You guessed the code in {attempt} tries.'
                connection.send(msg.encode(FORMAT))
                break
            connection.send(msg.encode(FORMAT))
        else:
            message = f'You lost. The code was {code}'
            print(message)
            connection.send(message.encode(FORMAT))
    elif message.upper == 'PVP':
        pass
    connection.close()


def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Number of threads: {threading.active_count()-1}")


print("Starting Server...")
start()
