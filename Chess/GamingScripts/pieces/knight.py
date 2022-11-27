import pygame
#import string

#from pygame_gui.elements.ui_text_entry_line import UITextEntryLine
from typing import Sequence, Literal

from board_utils import Square
from chess.CONSTANTS import (SQUARE_WIDTH, WHITE, BLACK, BLUE_GREEN)
from .piece import Piece
from .king import King
from flatten import flatten
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
            self.file, self.rank, self.possible_files,self.square_width,self.square_height)
        self.attacked_pieces = []
        self.instances.append(self)

    def update_attacked_pieces(self, x: int, y: int, square_width: int, square_height: int, squares: Squares) -> list:
        attacked_pieces = []
        possible_positions = self.get_possible_positions(
            get_game_pos(x, y, self.possible_files), squares)
        possible_squares = [square for square in squares.values(
        ) if square.get_window_pos() in possible_positions]
        x_values = [square.x for square in possible_squares]
        y_values = [square.y for square in possible_squares]
        colors = [square.color for square in possible_squares]
        coordinates = zip(x_values, y_values, colors)
        for position in possible_positions:
            x, y = position.split('')
            attacked_pieces.append((x, y))
        attacked_pieces.extend(self.get_attacked_positions(x, y))
        return attacked_pieces

    def _get_possible_positions(self, current_position: GamePosition, squares: Squares) -> Positions:
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

    def _find_piece_from_move_set(self, move_set: Positions, squares: Squares):
        for square in move_set:
            piece_at_current_position = squares[square].piece
            if piece_at_current_position in self.instances:
                return piece_at_current_position

    def validate(self, position: GamePosition, squares: Squares, king: King) -> bool:
        file, rank = position
        possible_positions = self._get_possible_positions((file, rank))
        if not self._find_piece_from_move_set(possible_positions, squares) or (self.color == squares[file+str(rank)].piece.color and squares[file+str(rank)].piece.color):
            return False
        else:
            temp = squares[file+str(rank)]
            if isinstance(temp.piece, Empty):
                squares[file+str(rank)].piece = squares[self.file +
                                                        str(self.rank)].piece
            else:
                temp = squares[self.file+str(self.rank)].piece
                squares[self.file+str(self.rank)].piece = temp
            if king.check(squares=squares, position=position):
                return False
            else:
                return True
