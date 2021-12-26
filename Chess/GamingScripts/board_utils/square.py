from typing import Any
import pygame


class Square:

    def __init__(self, rank: int, file: str, color: tuple[int, int, int], piece: Any, square_length: int, is_empty: bool = False):
        pygame.init()
        self.rank = rank
        self.file = file
        self.color = color
        self.is_empty = is_empty
        self.piece = piece
        self.square_length = square_length
        self.is_emptiable = True

    def get_window_pos(self):
        y = (self.rank-1)*100
        possible_files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        x = possible_files.index(self.file.lower())*100
        return x, y

    def draw(self, win: pygame.Surface):
        x, y = self.get_window_pos()
        self.rect = pygame.Rect(x, y, self.square_length, self.square_length)
        pygame.gfxdraw.rectangle(win, self.rect, self.color)
        if self.piece:
            win.blit(self.piece.image_surface, (x, y))
