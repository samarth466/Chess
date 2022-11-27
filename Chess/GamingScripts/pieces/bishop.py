import pygame
from utils.functions import get_game_pos, get_window_pos
from utils.types import GamePosition, Squares
from .piece import Piece
from .king import King
from .empty import Empty


class Bishop(Piece):

    def __init__(self, file: str, rank: int, color: pygame.Color, min_x: int, max_x: int, min_y: int, max_y: int, square_width: int, square_height: int, win_width: int, win_height: int) -> None:
        pygame.init()
        super().__init__(file, rank, 'Bishop', color)
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.square_width = square_width
        self.square_height = square_height
        self.win_width = win_width
        self.win_height = win_height
        self.x, self.y = self.piece_x, self.piece_y = get_window_pos(
            self.file, self.rank, self.possible_files, self.square_width, self.square_height)
        self.attacked_pieces = []

    def validate(self, position: GamePosition, squares: Squares, king: King) -> bool:
        file, rank = position
        try:
            move_ratio = (rank-self.rank)/(ord(file)-ord(self.file))
            if move_ratio in [1, -1]:
                squares[file+str(rank)] = squares[self.file+str(self.rank)]
                if king.check(squares=squares, position=position):
                    return False
                else:
                    stop = self.rank-rank
                    step = -1 if stop < 0 else 1
                    for i in range(0, stop, step):
                        compare_file = chr(ord(self.file)+i)
                        if not isinstance(squares[compare_file+str(self.rank+i)].piece, Empty) and compare_file != file:
                            return False
                    else:
                        return True
        except ZeroDivisionError:
            return False
        return False
