from ast import If
from turtle import st
from typing import Any
from utils.functions import get_window_pos, get_game_pos
import pygame
from .piece import Piece
from .rook import Rook
from board_utils.square import Square
from chess.CONSTANTS import WHITE, BLACK
from utils.types import WindowPosition, GamePosition, Positions, Squares


class King(Piece):

    def __init__(self, image: str, file: str, rank: int, color: pygame.Color, min_x: int, max_x: int, min_y: int, max_y: int, square_width: int, square_height: int, win_width: int, win_height: int) -> None:
        pygame.init()       # initialize pygame
        super().__init__(image, file, rank, 'King', color)
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.square_width = square_width       # width of a single square position
        self.square_height = square_height        # height of single square position
        self.win_width = win_width       # width of the window
        self.win_height = win_height      # height of the window
        self.x, self.y = self.piece_x, self.piece_y = get_window_pos(
            self.file, self.rank, self.possible_files)
        self.attacked_pieces = []      # list of pieces being attacked by self
        self.attackers = []      # list of pieces attacking self
        self.has_moved = False

    def validate(self, position: GamePosition, squares: Squares) -> bool:
        file,rank = position
        possible_distances = [0,1]
        if abs(rank-self.rank) in possible_distances and abs(ord(file)-ord(self.file)) in possible_distances:
            piece_color = squares[(file+str(rank))].piece.color
            if piece_color == self.color or not piece_color:
                return False
            else:
                return self.check(position=position,squares=squares)
        return False

    def check(self, pieces: list[Piece] = [], position: GamePosition = tuple(), squares: dict[str, Square] = dict()) -> bool:
        if position and squares:
            if squares[position[0]+str(position[1])].attacked:
                return True
            return False
        else:
            for piece_list in pieces:
                for piece in piece_list:
                    if self.attackers or (self.x, self.y) in piece.attacked_pieces:
                        return True
            return False

    def get_possible_positions_from_current_position(self, position: GamePosition, squares: Squares) -> Positions:
        file, rank = position
        prev_rank = rank-1 if rank > 1 else None
        next_rank = rank+1 if rank < 8 else None
        prev_file = self.possible_files[self.possible_files.index(
            file)-1] if file != self.possible_files[0] else None
        next_file = self.possible_files[self.possible_files.index(
            file)+1] if self.possible_files[-1] else None
        return list(filter((lambda i: (squares[i[0]+str(i[1])].piece.color != self.color and all(i))), [(prev_file, prev_rank), (file, prev_rank), (prev_file, rank), (file, rank), (next_file, rank), (prev_file, next_rank), (file, next_rank), (next_file, next_rank)]))

    def checkmate(self, pieces: list[Piece]) -> bool:
        if self.check(pieces):
            possible_positions = self.get_possible_positions_from_current_position(
                (self.file, self.rank), self.squares)
            filtered_possible_positions = list(
                filter(lambda i: self.check(pieces, i, self.squares), possible_positions))
            if possible_positions.length() == filtered_possible_positions:
                return True
            return False
        return False

    def convert_color_to_rank(self, rank: int) -> bool:
        if self.color == WHITE:
            return MIN_ROWS + rank
        elif self.color == BLACK:
            return MAX_ROWS - rank

    # every val in matterial.values() must be an instance of Rook, Queen, Bishop, Pawn, King, or Knight
    def castle(self, rook: Rook, normal: bool, matterial: dict[str, Any]) -> None:
        if normal:
            if self.squares[f'F{str(self.convert_color_to_rank(0))}'].empty() and self.squares[f'G{str(self.convert_color_to_rank(0))}'].empty():
                if not (self.check(matterial, ('F', self.convert_color_to_rank(0)), self.squares) or self.check(matterial, ('G', self.convert_color_to_rank(0)), self.squares) or self.check(matterial, (self.file, self.rank), self.squares)):
                    if not (self.has_moved or rook.has_moved):
                        self.file = 'G'
                        rook.file = 'F'
        else:
            if self.squares[f'B{str(self.convert_color_to_rank(0))}'].empty() and self.squares[f'C{str(self.convert_color_to_rank(0))}'].empty() and self.squares[f'D{str(self.convert_color_to_rank(0))}'].empty():
                if not (self.check(matterial, ('B', self.convert_color_to_rank(0)), self.squares) or self.check(matterial, ('C', self.convert_color_to_rank(0)), self.squares) or self.check(matterial, ('D', self.convert_color_to_rank(0)), self.squares) or self.check(matterial, (self.file, self.rank), self.squares)):
                    if not (self.has_moved or rook.has_moved):
                        self.file = 'B'
                        rook.file = 'C'
