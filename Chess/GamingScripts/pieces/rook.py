from utils.functions import get_window_pos, get_game_pos
import pygame
from .piece import Piece
from utils.types import GamePosition


class Rook(Piece):

    def __init__(self, image: str, file: str, rank: int, color: pygame.Color, min_x: int, max_x: int, min_y: int, max_y: int, square_width: int, square_height: int, win_width: int, win_height: int) -> None:
        pygame.init()
        super().__init__(image, file, rank, 'Rook', color)
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.square_width = square_width
        self.square_height = square_height
        self.win_width = win_width
        self.win_height = win_height
        self.x, self.y = self.piece_x, self.piece_y = get_window_pos(
            self.file, self.rank, self.possible_files)
        self.attacked_pieces = []
        self.has_moved = False
    
    def validate(self,position: GamePosition) -> bool:
        file,rank = position
        try:
            move_ratio = (rank-self.rank)/(ord(file)-ord(self.file))
            if move_ratio == 0:
                return True
        except ZeroDivisionError:
            return True
        return False