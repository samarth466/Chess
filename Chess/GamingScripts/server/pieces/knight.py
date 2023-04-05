import pygame
from typing import Sequence, Literal

from board_utils import Square
from chess.CONSTANTS import (SQUARE_WIDTH, WHITE, BLACK)
from .piece import Piece
from .king import King
from .empty import Empty
from utils.flatten import flatten
from utils.types import (
    GamePosition, Positions, Squares
)
from utils.functions import get_game_pos, get_window_pos


class Knight(Piece):

    instances = []

    def __init__(self, file: str, rank: int, color: pygame.Color, min_x: int, max_x: int, min_y: int, max_y: int, square_width: int, square_height: int, win_width: int, win_height: int) -> None:
        pygame.init()
        super().__init__(file, rank, 'Knight', color)
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

    @classmethod
    def get_possible_positions(self, current_position: GamePosition, squares: Squares) -> Positions:
        file, rank = current_position
        backLeft1 = (self.possible_files[self.possible_files.index(
            file)-1], rank-2) if file != self.possible_files[0] and rank > 2 else (None, 0)
        backRight1 = (self.possible_files[self.possible_files.index(
            file)+1], rank-2) if file != self.possible_files[-1] and rank > 2 else (None, 0)
        backRight2 = (self.possible_files[self.possible_files.index(
            file)+2], rank-1) if file not in self.possible_files[-2:] and rank > 1 else (None, 0)
        forwardRight2 = (self.possible_files[self.possible_files.index(
            file)+2], rank+1) if file not in self.possible_files[-2:] and rank < 8 else (None, 0)
        forwardRight1 = (self.possible_files[self.possible_files.index(
            file)+1], rank+2) if file != self.possible_files[-1] and rank < 7 else (None, 0)
        forwardLeft1 = (self.possible_files[self.possible_files.index(
            file)-1], rank+2) if file != self.possible_files[0] and rank < 7 else (None, 0)
        forwardLeft2 = (self.possible_files[self.possible_files.index(
            file)-2], rank+1) if file != self.possible_files[:2] and rank < 8 else (None, 0)
        backLeft2 = (self.possible_files[self.possible_files.index(
            file)-2], rank-1) if file != self.possible_files[:2] and rank > 1 else (None, 0)
        return list(filter((lambda i: (squares[i[0]+str(i[1])].piece.color != self.color and all(i))), [backLeft1, backLeft2, backRight1, backRight2, forwardRight1, forwardRight2, forwardLeft1, forwardLeft2]))

    def validate(self, position: GamePosition, squares: Squares, king: King) -> bool:
        file, rank = position
        if isinstance(squares[file+str(rank)], Empty):
            squares[file+str(rank)].piece, squares[self.file+str(self.rank)
                                                   ].piece = squares[self.file+str(self.rank)].piece, squares[file+str(rank)].piece
            return not king.check(position=position, squares=squares)
        else:
            if squares[file+str(rank)].piece.color != self.color:
                squares[file+str(rank)
                        ].piece = Empty(tuple(None for _ in range(11)))
            squares[file+str(rank)].piece, squares[self.file+str(self.rank)
                                                   ].piece = squares[self.file+str(self.rank)].piece, squares[file+str(rank)].piece
            return not king.check(position=position, squares=squares)
