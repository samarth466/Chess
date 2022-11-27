from utils.functions import get_window_pos, get_game_pos
import pygame
from .piece import Piece
from .king import King
from utils.types import GamePosition, Squares


class Queen(Piece):

    def __init__(self, file: str, rank: int, color: pygame.Color, min_x: int, max_x: int, min_y: int, max_y: int, square_width: int, square_height: int, win_width: int, win_height: int) -> None:
        pygame.init()       # initialize pygame
        super().__init__(file, rank, 'Queen', color)
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.square_width = square_width       # width of a single square position
        self.square_height = square_height        # height of single square position
        self.win_width = win_width       # width of the window
        self.win_height = win_height      # height of the window
        self.piece_x, self.piece_y = self.x, self.y = get_window_pos(
            self.file, self.rank, self.possible_files, self.square_width, self.square_height)
        self.attacked_pieces = []      # list of pieces being attacked by self

    def validate(self, position: GamePosition, squares: Squares, king: King) -> bool:
        file, rank = position
        try:
            move_ratio = (rank-self.rank)/(ord(file)-ord(self.file))
            if move_ratio in [-1, 0, 1]:
                squares[file+str(rank)], squares[self.file+str(self.rank)
                                                 ] = squares[self.file+str(self.rank)], squares[file+str(rank)]
                if king.check(squares=squares, position=position):
                    return False
                else:
                    if move_ratio == 0:
                        stop = self.rank-rank
                        step = -1 if stop < 0 else 1
                        for i in range(0, stop, step):
                            compare_file = chr(ord(self.file)+i)
                            if not isinstance(squares[compare_file+str(self.rank+i)], Empty) and compare_file != file:
                                return False
                        else:
                            return True
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
            stop = ord(self.file)-ord(file)
            step = -1 if stop < 0 else 1
            for i in range(0, stop, step):
                compare_rank = self.rank+i
                if not isinstance(squares[chr(ord(self.file)+i)+str(compare_rank)]) and compare_rank != rank:
                    return False
            else:
                return True
        return False
