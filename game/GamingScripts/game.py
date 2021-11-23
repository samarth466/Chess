from .chess.player import Player
import pygame

from .chess.CONSTANTS import BLACK, SQUARE_HEIGHT, SQUARE_WIDTH, WHITE, WINDOW_HEIGHT, WINDOW_WIDTH
from .chess.board import Board

pygame.init()
pygame.display.init()
pygame.font.init()

WINNING_FONT = pygame.font.SysFont('comicsans', 60, True)


def main():
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    board = Board((WINDOW_WIDTH, WINDOW_HEIGHT), SQUARE_WIDTH, SQUARE_HEIGHT, Player(
        WHITE, 'Joe'), Player(BLACK, 'Jane'), SCREEN, SQUARE_HEIGHT*2, SQUARE_HEIGHT*2)
    run = True
    clock = pygame.time.Clock()
    FPS = 60
    sound_level = 2
    while run:
        clock.tick(FPS)
        SCREEN.fill((0, 72, 0))
        for event in pygame.event.get():
            if event.type == pygame.K_ESCAPE:
                run = False
        keys = pygame.key.get_pressed()
        for i in range(3):
            if keys[ord(str(i))]:
                sound_level = i
        board.move()
        game_has_ended, winning_color = board.end()
        if winning_color:
            player = board.players.find_player_by_color(winning_color).name
            txt = f"{player} is the winner!"
            txt_render = WINNING_FONT.render(txt, 1, (0, 72, 0))
            SCREEN.blit(txt_render, (SCREEN.get_width(
            )/2-(txt_render.get_width()/2), SCREEN.get_height()/2-(txt.get_height()/2)))
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
