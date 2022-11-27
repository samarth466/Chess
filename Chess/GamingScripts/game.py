import pygame
from thorpy import Inserter

from utils.types import GamePosition, PositionDict
from utils.functions import get_string_from_sequence, get_game_pos, get_window_pos
from chess.player import Player
from chess.CONSTANTS import BLACK, SQUARE_HEIGHT, SQUARE_WIDTH, WHITE, WINDOW_HEIGHT, WINDOW_WIDTH, GREY, BLUE_GREEN
from chess.board import Board

# PyGame Initializations

pygame.init()
pygame.font.init()

# Constants

WINNING_FONT = pygame.font.SysFont('comicsans', 60, True)


def main() -> None:
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT+SQUARE_HEIGHT*4),pygame.SCALED)
    SCREEN.scroll(0, SQUARE_WIDTH*2)
    pygame.display.set_caption("Chess")
    board = Board((WINDOW_WIDTH, WINDOW_HEIGHT), SQUARE_WIDTH, SQUARE_HEIGHT, Player('Joe', WHITE), Player('Jane', BLACK), SCREEN, SQUARE_HEIGHT*2, SQUARE_HEIGHT*2)
    run = True
    clock = pygame.time.Clock()
    FPS = 60
    sound_level = 2
    volume = 0
    accessibility = True
    move_textbox = Inserter("Move: ")
    move_textbox.auto_resize = True
    move_textbox.add_key_event(pygame.K_RETURN)
    move_textbox.finish()
    move_textbox.blit()
    while run:
        clock.tick(FPS)
        SCREEN.fill(GREY)
        #SCREEN.fill((0, 72, 0))
        board.draw_board()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run = False
        for i in range(3):
            if keys[ord(str(i))]:
                sound_level = i
        if keys[pygame.K_LCTRL] and keys[pygame.K_DOWN]:
            volume -= 1
        if keys[pygame.K_LCTRL] and keys[pygame.K_UP]:
            volume += 1
        if keys[pygame.K_a]:
            accessibility = not accessibility
        if (keys[pygame.K_LCTRL] and keys[pygame.K_e]) or (keys[pygame.K_RCTRL] and keys[pygame.K_e]):
            move_textbox.enter()
        move = move_textbox.get_value()
        print(move)

if __name__ == "__main__":
    main()