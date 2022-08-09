import pygame

from utils.types import GamePosition, PositionDict
from utils.functions import get_string_from_sequence, get_game_pos, get_window_pos
from chess.player import Player
from chess.CONSTANTS import BLACK, SQUARE_HEIGHT, SQUARE_WIDTH, WHITE, WINDOW_HEIGHT, WINDOW_WIDTH, RED
from chess.board import Board

# PyGame Initializations

pygame.init()
pygame.display.init()
pygame.font.init()

# Constants

WINNING_FONT = pygame.font.SysFont('comicsans', 60, True)


def show_cursor(window: pygame.Surface):
    x, y = pygame.mouse.get_pos()
    x, y = x//SQUARE_WIDTH+SQUARE_WIDTH//2, y//SQUARE_HEIGHT+SQUARE_HEIGHT//2
    pygame.draw.circle(window, RED, (x, y), SQUARE_HEIGHT/2, 1)


def main() -> None:
    pygame.mouse.set_pos((0, SQUARE_HEIGHT*2))
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT+SQUARE_HEIGHT*4))
    SCREEN.scroll(0, SQUARE_WIDTH*2)
    pygame.display.set_caption("Chess")
    board = Board((WINDOW_WIDTH, WINDOW_HEIGHT), SQUARE_WIDTH, SQUARE_HEIGHT, Player('Joe', WHITE, 1), Player('Jane', BLACK, -1), SCREEN, SQUARE_HEIGHT*2, SQUARE_HEIGHT*2)
    run = True
    clock = pygame.time.Clock()
    FPS = 60
    sound_level = 2
    volume = 0
    accessibility = True
    while run:
        clock.tick(FPS)
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
        if keys[pygame.K_KP1] or keys[pygame.K_1]:
            x, y = pygame.mouse.pos()
            pygame.mouse.set_pos(x-SQUARE_WIDTH, y+SQUARE_HEIGHT)
        if keys[pygame.K_KP2] or keys[pygame.K_2]:
            x, y = pygame.mouse.pos()
            pygame.mouse.set_pos(x, y+SQUARE_HEIGHT)
        if keys[pygame.K_KP3] or keys[pygame.K_3]:
            x, y = pygame.mouse.pos()
            pygame.mouse.set_pos(x+SQUARE_WIDTH, y+SQUARE_HEIGHT)
        if keys[pygame.K_KP4] or keys[pygame.K_4]:
            x, y = pygame.mouse.pos()
            pygame.mouse.set_pos(x-SQUARE_WIDTH, y)
        if keys[pygame.K_KP6] or keys[pygame.K_6]:
            x, y = pygame.mouse.pos()
            pygame.mouse.set_pos(x+SQUARE_WIDTH, y)
        if keys[pygame.K_KP7] or keys[pygame.K_7]:
            x, y = pygame.mouse.pos()
            pygame.mouse.set_pos(x-SQUARE_WIDTH, y-SQUARE_HE    IGHT)
        if keys[pygame.K_KP8] or keys[pygame.K_8]:
            x, y = pygame.mouse.pos()
            pygame.mouse.set_pos(x, y-SQUARE_HEIGHT)
        if keys[pygame.K_KP9] or keys[pygame.K_9]:
            x, y = pygame.mouse.pos()
            pygame.mouse.set_pos(x+SQUARE_WIDTH, y-SQUARE_HEIGHT)
        show_cursor(SCREEN)
        if keys[pygame.K_RETURN] or keys[pygame.K_KP5] or keys[pygame.K_KP_ENTER]:
            if board.squares[get_string_from_sequence(tuple(str(i) for i in get_game_pos(*pygame.mouse.get_pos())))].piece:
                board.move()
        winning_color = board.end()
        if winning_color:
            player = board.find_player_by_color(winning_color).name
            txt = f"{player} is the winner!"
            txt_render = WINNING_FONT.render(txt, 1, (0, 72, 0))
            SCREEN.blit(txt_render, (SCREEN.get_width()/2-(txt_render.get_width()/2), SCREEN.get_height()/2-(txt.get_height()/2)))
            pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()