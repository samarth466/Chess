from utils.functions import get_window_pos, get_game_pos
import pygame
from .piece import Piece
from utils.types import GamePosition


class Queen(Piece):

    def __init__(self, image: str, file: str, rank: int, color: pygame.Color, min_x: int, max_x: int, min_y: int, max_y: int, square_width: int, square_height: int, win_width: int, win_height: int) -> None:
        pygame.init()       # initialize pygame
        super().__init__(image, file, rank, 'Queen', color)
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.square_width = square_width       # width of a single square position
        self.square_height = square_height        # height of single square position
        self.win_width = win_width       # width of the window
        self.win_height = win_height      # height of the window
        self.piece_x, self.piece_y = self.x, self.y = get_window_pos(
            self.file, self.rank, self.possible_files)
        self.attacked_pieces = []      # list of pieces being attacked by self
    
    def validate(self,position: GamePosition) -> bool:
        file,rank = position
        try:
            move_ratio = (rank-self.rank)/(ord(file)-ord(self.file))
            if move_ratio in [-1,0,1]:
                return True
        except ZeroDivisionError:
            return True
        return False