import pygame
from utils.types import GamePosition, Squares
from chess.CONSTANTS import WHITE, BLACK
from os.path import join
from pathlib import Path


class Piece:

    def __init__(self, file: str, rank: int, name: str, color: pygame.Color) -> None:
        COLOR_LETTERING = 'W' if color == WHITE else 'B'
        PATH = join(Path(__file__).parent.parent, 'chessmen',
                    f"{COLOR_LETTERING}_{name}.png")
        pygame.init()
        if PATH.endswith(f'_{None}.png') != True:
            self.image = pygame.image.load(PATH).convert_alpha()
            self.SURFACE = pygame.Surface(
                (self.image.get_width(), self.image.get_height()), pygame.SRCALPHA)
        else:
            self.image = self.SURFACE = None
        self.rank = rank
        self.file = file
        self.color = color
        self.name = name
        self.possible_files = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    def draw(self, win: pygame.Surface) -> None:
        x, y = self.get_window_pos()
        self.SURFACE.blit(self.image, (x, y))

    def update_attacked_pieces(self, squares: Squares) -> list[GamePosition]:
        return self.attacked_pieces.extend(self._get_possible_positions((self.x, self.y), squares))
