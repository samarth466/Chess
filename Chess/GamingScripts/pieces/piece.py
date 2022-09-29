import pygame
from utils.types import GamePosition, Squares


class Piece:

    def __init__(self, image, file, rank, name, color):
        pygame.init()
        self.image = pygame.image.load(image) if image else None
        self.rank = rank
        self.file = file
        self.color = color
        self.name = name
        self.possible_files = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    def draw(self, win):
        x, y = self.get_window_pos()
        win.blit(self.image, (x, y))

    def update_attacked_pieces(self,squares: Squares) -> list[GamePosition]:
        return self.attacked_pieces.extend(self._get_possible_positions((self.x, self.y),squares))
