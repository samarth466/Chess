import socket
import pygame
import json
from os.path import join
#from thorpy import Inserter
#from voice_recognition import speak

# PyGame Initializations

pygame.init()
pygame.font.init()
pygame.display.init()

# Constants

WINNING_FONT = pygame.font.SysFont('comicsans', 60, True)
WINDOW_WIDTH = WINDOW_HEIGHT = min(
    pygame.display.Info().current_w, pygame.display.Info().current_h)
BLUE_GREEN = (13, 152, 186)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Socket Constants

PORT = 5050
MESSAGE_SIZE = 2240000
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = 'Disconnect!'
HOST = '192.168.1.180'
ADDR = (HOST, PORT)
CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CLIENT.connect(ADDR)


def draw(window: pygame.Surface, data: str) -> None:
    if not data:
        data = {}
    else:
        data = eval(data)
    file = "A"
    rank = 1
    square_size = WINDOW_HEIGHT//8
    for i in range(0, WINDOW_WIDTH, square_size):
        print(file)
        for j in range(0, WINDOW_HEIGHT, square_size):
            color = BLACK
            if ord(file) % 2 == 0 and rank % 2 == 1:
                color = WHITE
            if ord(file) % 2 == 1 and rank % 2 == 0:
                color = WHITE
            pygame.draw.rect(window, color, (i, j, square_size, square_size))
            if f"{file}{rank}" not in data:
                pass
            elif data[f"{file}{rank}"].endswith(str(None)):
                window.blit(pygame.image.load(
                    join("Chessmen", data[f"{file}{rank}"])), (i, j))
            rank += 1
        rank = 1
        file = chr(ord(file)+1)
    pygame.display.update()


def main() -> None:
    SCREEN = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SCALED)
    pygame.display.set_caption("Chess")
    run = True
    clock = pygame.time.Clock()
    FPS = 60
    sound_level = 2
    volume = 0
    accessibility = True
    #move_textbox = Inserter("Move: ")
    #move_textbox.auto_resize = True
    # move_textbox.add_key_event(pygame.K_RETURN)
    # move_textbox.finish()
    # move_textbox.blit()
    while True:
        name = input("Enter your name: ")
        if len(name) < 3:
            print("Invalid input. You must enter your name.")
        else:
            CLIENT.send(name.encode(FORMAT))
            break
    opponent_name = CLIENT.recv(MESSAGE_SIZE).decode(FORMAT)
    print(f"Playing against {opponent_name}")
    while run:
        clock.tick(FPS)
        SCREEN.fill(GREY)
        #SCREEN.fill((0, 72, 0))
        data = CLIENT.recv(MESSAGE_SIZE)
        if "Waiting for opponent".encode(FORMAT) in data:
            print(data.decode(FORMAT))
            CLIENT.recv(MESSAGE_SIZE)
        msg = CLIENT.recv(MESSAGE_SIZE).decode(FORMAT)
        print(msg)
            draw(SCREEN, msg)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run = False
        for i in range(3):
            if keys[ord(str(i))]:
                sound_level = i
        if keys[pygame.K_LCTRL] and keys[pygame.K_DOWN] and volume > 0:
            volume -= 1
        if keys[pygame.K_LCTRL] and keys[pygame.K_UP]:
            volume += 1
        if keys[pygame.K_a]:
            accessibility = not accessibility
        # if (keys[pygame.K_LCTRL] and keys[pygame.K_e]) or (keys[pygame.K_RCTRL] and keys[pygame.K_e]):
            # move_textbox.enter()
        #move = move_textbox.get_value()
        while True:
            move = input("Enter a move: ")
            CLIENT.send(move.encode(FORMAT))
            message = CLIENT.recv(MESSAGE_SIZE).decode(FORMAT)
            if "try" in message:
                print(message)
            else:
                print(message)
                break
        message = CLIENT.recv(MESSAGE_SIZE).decode(FORMAT)
        if 'won' in message:
            print("Game over. {message}")
            break
        elif 'draw' in message:
            print("Game over. {message}")
            break


if __name__ == "__main__":
    while True:
        main()
        again = input("Would you like to play again? (Yes/No): ")
        if again.lower == 'yes':
            CLIENT.connect(ADDR)
        else:
            pygame.quit()
            break
