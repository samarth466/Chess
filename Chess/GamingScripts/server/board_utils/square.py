from typing import Any
import pygame


class Square:

    def __init__(self, rank: int, file: str, color: tuple[int, int, int], piece: Any, square_length: int, is_empty: bool = False):
        self.rank = rank
        self.file = file
        self.color = color
        self.is_empty = is_empty
        self.piece = piece
        self.square_length = square_length
        self.attacked = False

    def get_window_pos(self):
        y = (self.rank-1)*self.square_length
        possible_files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        x = possible_files.index(self.file.lower())*self.square_length
        return x, y

    def draw(self, win: pygame.Surface, piece=None):
        x, y = self.get_window_pos()
        rect = pygame.Rect(x, y, self.square_length, self.square_length)
        pygame.draw.rect(win, self.color, rect)
        if self.piece.image:
            piece_x, piece_y = x+self.square_length//2-self.piece.image.get_width()//2, y + \
                self.square_length//2-self.piece.image.get_height()//2
            win.blit(self.piece.SURFACE, (piece_x, piece_y))

    def __str__(self) -> str:
        return f"{self.piece.name} @ {self.file}{self.rank}"

    def get_diagonals(self):
        diagonals = [[], []]
        for _ in range(max(self.rank, 8-self.rank)):
            if ord(self.file)-1 >= ord('A') and self.rank-1 >= 0:
                diagonals[0].append((chr(ord(self.file)-1), self.rank-1))
            if ord(self.file)+1 <= ord('H') and self.rank+1 <= 8:
                diagonals[0].append((chr(ord(self.file)+1), self.rank+1))
            if ord(self.file)-1 >= ord('A') and self.rank+1 <= 8:
                diagonals[1].append((chr(ord(self.file)-1), self.rank+1))
            if ord(self.file)+1 <= ord('H') and self.rank-1 >= 0:
                diagonals[1].append((chr(ord(self.file)+1), self.rank-1))
        return [sorted(diagonals[0]), sorted(diagonals[1])]

    def get_ranks(self):
        ranks = []
        for _ in range(max(self.rank, 8-self.rank)):
            if self.rank-1 >= 0:
                ranks.append((self.file, self.rank-1))
            elif self.rank+1 <= 8:
                ranks.append((self.file, self.rank+1))
        return sorted(ranks)

    def get_files(self):
        files = []
        for _ in range(max(ord(self.file)-ord('A'), ord('H')-ord(self.file))):
            if ord(self.file)-1 >= ord('A'):
                files.append((chr(ord(self.file)-1), self.rank))
            elif ord(self.file)+1 <= ord('H'):
                files.append((chr(ord(self.file)+1), self.rank))
