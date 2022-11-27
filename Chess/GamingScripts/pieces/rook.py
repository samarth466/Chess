from typing import Any
from utils.functions import get_window_pos, get_game_pos
import pygame
from .piece import Piece
from .king import King
from .empty import Empty
from utils.types import GamePosition, Squares


class Rook(Piece):

    def __init__(self, file: str, rank: int, color: pygame.Color, min_x: int, max_x: int, min_y: int, max_y: int, square_width: int, square_height: int, win_width: int, win_height: int) -> None:
        pygame.init()
        super().__init__(file, rank, 'Rook', color)
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
        self.has_moved = False

    def validate(self, position: GamePosition, squares: Squares, king: King) -> bool:
        file, rank = position
        try:
            move_ratio = (rank-self.rank)/(ord(file)-ord(self.file))
            if move_ratio == 0:
                squares[file+str(rank)], squares[self.file+str(self.rank)
                                                 ] = squares[self.file+str(self.rank)], squares[file+str(rank)]
                if king.check(squares=squares, position=position):
                    return False
                else:
                    stop = self.rank-rank
                    step = -1 if stop < 0 else 1
                    for i in range(0, stop, step):
                        compare_file = chr(ord(self.file)+i)
                        if not isinstance(squares[compare_file+str(self.rank+i)], Empty) and compare_file != file:
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

    # every val in matterial.values() must be an instance of Rook, Queen, Bishop, Pawn, King, or Knight
    def castle(self, king: King, matterial: dict[str, Any], squares: Squares) -> None:
        step = -1 if self.file < king.file else 1
        start = self.possible_files.index(king.file)
        files_to_check = self.possible_files[start::step][1::-1].sort()
        if len(files_to_check) == 3:
            third_check = files_to_check[2]
            third_square_empty_check = squares[f'{third_check}{self.rank}'].is_empty
        else:
            third_check = third_square_empty_check = True
        if squares[f'{files_to_check[0]}{self.file}'].is_empty and self.squares[f'{files_to_check[1]}{self.rank}'].is_empty and third_square_empty_check:
            if not (king.check(position=(files_to_check[0], self.rank), squares=squares) or king.check(position=(files_to_check[1], self.rank), squares=squares) or king.check(position=(third_check, self.rank), squares=squares) or king.check(position=(self.file, self.rank), squares=squares)):
                if not (self.has_moved or king.has_moved):
                    king.file = files_to_check[1] if len(
                        files_to_check) == 2 else files_to_check[1]
                    self.file = files_to_check[0] if len(
                        files_to_check) == 2 else files_to_check[2]
