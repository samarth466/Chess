from importlib import import_module
from pathlib import Path
from os.path import join
import pygame
from .piece import Piece
from .bishop import Bishop
from .king import King
from .knight import Knight
from .queen import Queen
from .rook import Rook
from chess.CONSTANTS import WHITE, BLACK
from board_utils import Square
from utils.types import Squares, WindowPosition, GamePosition
from utils.functions import get_game_pos, get_window_pos


class Pawn(Piece):

    def __init__(self, file: str, rank: int, color: pygame.Color, min_x: int, max_x: int, min_y: int, max_y: int, square_width: int, square_height: int, win_width: int, win_height: int) -> None:
        pygame.init()
        super().__init__(file, rank, 'Pawn', color)
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
        self.double_moved_on_first_turn = False

    def validate(self, position: GamePosition, squares: Squares, king: King) -> bool:
        file, rank = position
        if file != self.file:
            if rank == self.rank:
                return False
            elif isinstance(squares[file+str(rank)].piece, Empty):
                squares[file+str(rank)], squares[self.file+str(self.rank)
                                                 ] = squares[self.file+str(self.rank)], squares[file+str(rank)]
                return not king.check(squares=squares, position=position)
            return False
        else:
            if 0 < abs(int(rank)-self.rank) <= 2:
                squares[file+str(rank)], squares[self.file+str(self.rank)
                                                 ] = squares[self.file+str(self.rank)], squares[file+str(rank)]
                print(squares[file+str(rank)])
                print(squares[self.file+str(self.rank)])
                return not king.check(squares=squares, position=position)
            return False

    def move_forward_twice(self, rank: int, file: str, squares: Squares) -> tuple[int, int]:
        if Self.color == WHITE and rank == 2:
            rank += 2
            if squares[file+str(rank)].piece:
                rank -= 2
        elif self.color == BLACK and rank == 7:
            rank -= 2
            if squares[file+str(rank)].piece:
                rank += 2
        return self.get_window_pos(file, rank)

    def promotion(self, promoted_piece: str, images: dict[pygame.Color, dict[str, list]], position: GamePosition):
        promoted_pieces = [Rook, Knight, Bishop, Queen]
        if promoted_piece in promoted_pieces:
            promoted_piece_lower = promoted_piece.lower()
            promoted_piece_module = import_module(
                promoted_piece_lower, Path(__file__).resolve().parent)
            promoted_piece = getattr(promoted_piece_module, promoted_piece)
            return promoted_piece(images[self.color][promoted_piece], self.file, self.rank, self.color, self.min_x, self.max_x, self.min_y, self.max_y, self.square_width, self.square_height, self.win_width, self.win_height)

    def en_passante(self, squares: dict[str, Square]) -> tuple[Piece]:
        previous_square = squares[self.possible_files[self.possible_files.index(
            self.file)-1]+str(self.rank)]
        next_square = squares[self.possible_files[self.possible_files.index(
            self.file)+1]+str(self.rank)]
        if self.color == WHITE:
            if self.rank == 5:
                if previous_square.piece:
                    if isinstance(previous_square.piece, self.__class__):
                        if previous_square.piece.double_moved_on_first_turn:
                            self.rank = 6
                            self.file = previous_square.piece.file
                            self.attacked_pieces.append(previous_square.piece)
                elif next_square.piece:
                    if isinstance(next_square.piece, self.__class__):
                        if next_square.piece.double_moved_on_first_turn:
                            self.rank = 6
                            self.file = next_square.piece.file
                            self.attacked_pieces.append(next_square.piece)
        if self.color == BLACK:
            if self.rank == 4:
                if previous_square.piece:
                    if isinstance(previous_square.piece, self.__class__):
                        if previous_square.piece.double_moved_on_first_turn:
                            self.rank = 3
                            self.file = previous_square.piece.file
                            self.attacked_pieces.append(previous_square.piece)
                elif next_square.piece:
                    if isinstance(next_square.piece, self.__class__):
                        if next_square.piece.double_moved_on_first_turn:
                            self.rank = 3
                            self.file = next_square.piece.file
                            self.attacked_pieces.append(next_square.piece)
        return self.attacked_pieces
