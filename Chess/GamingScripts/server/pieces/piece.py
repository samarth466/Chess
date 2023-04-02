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
        if not PATH.endswith('_none.png'):
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

    def __str__(self) -> str:
        color = 'White' if self.color == WHITE else 'Black'
        return f"{self.file}{self.rank}: {color} {self.name}"

    def __getstate__(self):
        state = self.__dict__.copy()
        image = state.pop("image")
        state["image_string"] = (pygame.image.tobytes(
            image, "RGB"), image.get_size())
        surface = state.pop("surface")
        state["surface_string"] = (pygame.image.tobytes(
            surface, "RGB"), surface.get_size())
        return state

    def __setstate__(self, state):
        image_string, size = state.pop("image_string")
        state["image"] = pygame.image.frombytes(image_string, "RGB")
        surface_string, size = state.pop("surface_string")
        state["surface"] = pygame.image.frombytes(surface_string, "RGB")
        self.__dict__.update(state)
