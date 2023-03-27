from itertools import cycle
from typing import Union
import string
import pygame

from pieces import Bishop, Empty, King, Knight, Pawn, Queen, Rook
from pieces.piece import Piece
from board_utils.square import Square
from .CONSTANTS import (WHITE, BLACK, GREY)
from .player import Player
from utils.functions import get_string_from_sequence
from .tables import Table
from utils.types import Squares, PositionDict, WindowPosition, GamePosition
from flatten import flatten


def capture_piece(matterial):
    for color, color_pieces in matterial:
        for piece_name, piece_list in color_pieces:
            if piece_list:
                for i, piece in enumerate(piece_list):
                    yield (color, piece_name, i)


class Board:

    def __init__(self, size: tuple[int, int], square_width: int, square_height: int, player1: Player, player2: Player, window: pygame.Surface, upper_offset: int = 0, lower_offset: int = 0) -> None:
        """
        Initialize the Board class.
        """
        pygame.init()
        pygame.display.init()
        self.win_width, self.win_height = size
        self.square_width = square_width
        self.square_height = square_height
        self.players = cycle([player1, player2])
        self.WINDOW = window
        self.upper_offset = upper_offset
        self.lower_offset = lower_offset
        self.captured_pieces = []
        self.possible_files = string.ascii_uppercase[:8]
        self.matterial = {
            BLACK: {
                'Bishop': [
                    Bishop('C', 8, BLACK, 0, self.win_width, 0, self.win_height,
                           self.square_width, self.square_height, self.win_width, self.win_height),
                    Bishop('F', 8, BLACK, 0, self.win_width, 0, self.win_height,
                           self.square_width, self.square_height, self.win_width, self.win_height)
                ],
                'King': [
                    King('E', 8, BLACK, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height)
                ],
                'Knight': [
                    Knight('B', 8, BLACK, 0, self.win_width, 0,
                           self.win_height, self.square_width, self.square_height, self.win_width, self.win_height),
                    Knight('G', 8, BLACK, 0, self.win_width, 0,
                           self.win_height, self.square_width, self.square_height, self.win_width, self.win_height)
                ],
                'Pawn': [
                    Pawn('A', 7, BLACK, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn('B', 7, BLACK, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn('C', 7, BLACK, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn('D', 7, BLACK, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn('E', 7, BLACK, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn('F', 7, BLACK, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn('G', 7, BLACK, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn('H', 7, BLACK, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height)
                ],
                'Queen': [
                    Queen('D', 8, BLACK, 0, self.win_width, 0,
                          self.win_height, self.square_width, self.square_height, self.win_width, self.win_height)
                ],
                'Rook': [
                    Rook('A', 8, BLACK, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Rook('H', 8, BLACK, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height)
                ]
            },
            WHITE: {
                'Bishop': [
                    Bishop('C', 1, BLACK, 0, self.win_width, 0, self.win_height,
                           self.square_width, self.square_height, self.win_width, self.win_height),
                    Bishop('F', 1, WHITE, 0, self.win_width, 0,
                           self.win_height, self.square_width, self.square_height, self.win_width, self.win_height)
                ],
                'King': [
                    King('E', 1, WHITE, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height)
                ],
                'Knight': [
                    Knight('B', 2, WHITE, 0, self.win_width, 0,
                           self.win_height, self.square_width, self.square_height, self.win_width, self.win_height),
                    Knight('G', 2, WHITE, 0, self.win_width, 0,
                           self.win_height, self.square_width, self.square_height, self.win_width, self.win_height)
                ],
                'Pawn': [
                    Pawn('A', 2, WHITE, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn('B', 2, WHITE, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn('C', 2, WHITE, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn('D', 2, WHITE, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn('E', 2, WHITE, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn('F', 2, WHITE, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn('G', 2, WHITE, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn('H', 2, WHITE, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height)
                ],
                'Queen': [
                    Queen('D', 1, WHITE, 0, self.win_width, 0,
                          self.win_height, self.square_width, self.square_height, self.win_width, self.win_height)
                ],
                'Rook': [
                    Rook('A', 1, WHITE, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Rook('H', 1, WHITE, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height)
                ]
            }
        }
        args = tuple(None for _ in range(11))
        self.matterial[WHITE]['Empty'] = self.matterial[BLACK]['Empty'] = [
            Empty(*args) for _ in range(16)]
        self.squares: dict[str, Square] = {
            'A1': Square(1, 'A', WHITE, self.matterial[WHITE]['Rook'][0], self.square_width),
            'A2': Square(2, 'A', BLACK, self.matterial[WHITE]['Pawn'][0], self.square_width),
            'A3': Square(3, 'A', WHITE, self.matterial[WHITE]['Empty'][0], self.square_width),
            'A4': Square(4, 'A', BLACK, self.matterial[WHITE]['Empty'][0], self.square_width),
            'A5': Square(5, 'A', WHITE, self.matterial[BLACK]['Empty'][0], self.square_width),
            'A6': Square(6, 'A', BLACK, self.matterial[BLACK]['Empty'][0], self.square_width),
            'A7': Square(7, 'A', WHITE, self.matterial[BLACK]['Pawn'][0], self.square_width),
            'A8': Square(8, 'A', BLACK, self.matterial[BLACK]['Rook'][0], self.square_width),
            'B1': Square(1, 'B', BLACK, self.matterial[WHITE]['Knight'][0], self.square_width),
            'B2': Square(2, 'B', WHITE, self.matterial[WHITE]['Pawn'][1], self.square_width),
            'B3': Square(3, 'B', BLACK, self.matterial[WHITE]['Empty'][0], self.square_width),
            'B4': Square(4, 'B', WHITE, self.matterial[WHITE]['Empty'][0], self.square_width),
            'B5': Square(5, 'B', BLACK, self.matterial[BLACK]['Empty'][0], self.square_width),
            'B6': Square(6, 'B', WHITE, self.matterial[BLACK]['Empty'][0], self.square_width),
            'B7': Square(7, 'B', BLACK, self.matterial[BLACK]['Pawn'][1], self.square_width),
            'B8': Square(8, 'B', WHITE, self.matterial[BLACK]['Knight'][0], self.square_width),
            'C1': Square(1, 'C', WHITE, self.matterial[WHITE]['Bishop'][0], self.square_width),
            'C2': Square(2, 'C', BLACK, self.matterial[WHITE]['Pawn'][2], self.square_width),
            'C3': Square(3, 'C', WHITE, self.matterial[WHITE]['Empty'][0], self.square_width),
            'C4': Square(4, 'C', BLACK, self.matterial[WHITE]['Empty'][0], self.square_width),
            'C5': Square(5, 'C', WHITE, self.matterial[BLACK]['Empty'][0], self.square_width),
            'C6': Square(6, 'C', BLACK, self.matterial[BLACK]['Empty'][0], self.square_width),
            'C7': Square(7, 'C', WHITE, self.matterial[BLACK]['Pawn'][2], self.square_width),
            'C8': Square(8, 'C', BLACK, self.matterial[BLACK]['Bishop'][0], self.square_width),
            'D1': Square(1, 'D', BLACK, self.matterial[WHITE]['Queen'][0], self.square_width),
            'D2': Square(2, 'D', WHITE, self.matterial[WHITE]['Pawn'][3], self.square_width),
            'D3': Square(3, 'D', BLACK, self.matterial[WHITE]['Empty'][0], self.square_width),
            'D4': Square(4, 'D', WHITE, self.matterial[WHITE]['Empty'][0], self.square_width),
            'D5': Square(5, 'D', BLACK, self.matterial[BLACK]['Empty'][0], self.square_width),
            'D6': Square(6, 'D', WHITE, self.matterial[BLACK]['Empty'][0], self.square_width),
            'D7': Square(7, 'D', BLACK, self.matterial[BLACK]['Pawn'][3], self.square_width),
            'D8': Square(8, 'D', WHITE, self.matterial[BLACK]['Queen'][0], self.square_width),
            'E1': Square(1, 'E', WHITE, self.matterial[WHITE]['King'][0], self.square_width),
            'E2': Square(2, 'E', BLACK, self.matterial[WHITE]['Pawn'][4], self.square_width),
            'E3': Square(3, 'E', WHITE, self.matterial[WHITE]['Empty'][0], self.square_width),
            'E4': Square(4, 'E', BLACK, self.matterial[WHITE]['Empty'][0], self.square_width),
            'E5': Square(5, 'E', WHITE, self.matterial[BLACK]['Empty'][0], self.square_width),
            'E6': Square(6, 'E', BLACK, self.matterial[BLACK]['Empty'][0], self.square_width),
            'E7': Square(7, 'E', WHITE, self.matterial[BLACK]['Pawn'][4], self.square_width),
            'E8': Square(8, 'E', BLACK, self.matterial[BLACK]['King'][0], self.square_width),
            'F1': Square(1, 'F', BLACK, self.matterial[WHITE]['Bishop'][1], self.square_width),
            'F2': Square(2, 'F', WHITE, self.matterial[WHITE]['Pawn'][5], self.square_width),
            'F3': Square(3, 'F', BLACK, self.matterial[WHITE]['Empty'][0], self.square_width),
            'F4': Square(4, 'F', WHITE, self.matterial[WHITE]['Empty'][0], self.square_width),
            'F5': Square(5, 'F', BLACK, self.matterial[BLACK]['Empty'][0], self.square_width),
            'F6': Square(6, 'F', WHITE, self.matterial[BLACK]['Empty'][0], self.square_width),
            'F7': Square(7, 'F', BLACK, self.matterial[BLACK]['Pawn'][5], self.square_width),
            'F8': Square(8, 'F', WHITE, self.matterial[BLACK]['Bishop'][1], self.square_width),
            'G1': Square(1, 'G', WHITE, self.matterial[WHITE]['Knight'][1], self.square_width),
            'G2': Square(2, 'G', BLACK, self.matterial[WHITE]['Pawn'][6], self.square_width),
            'G3': Square(3, 'G', WHITE, self.matterial[WHITE]['Empty'][0], self.square_width),
            'G4': Square(4, 'G', BLACK, self.matterial[WHITE]['Empty'][0], self.square_width),
            'G5': Square(5, 'G', WHITE, self.matterial[BLACK]['Empty'][0], self.square_width),
            'G6': Square(6, 'G', BLACK, self.matterial[BLACK]['Empty'][0], self.square_width),
            'G7': Square(7, 'G', WHITE, self.matterial[BLACK]['Pawn'][6], self.square_width),
            'G8': Square(8, 'G', BLACK, self.matterial[BLACK]['Knight'][1], self.square_width),
            'H1': Square(1, 'H', BLACK, self.matterial[WHITE]['Rook'][1], self.square_width),
            'H2': Square(2, 'H', WHITE, self.matterial[WHITE]['Pawn'][7], self.square_width),
            'H3': Square(3, 'H', BLACK, self.matterial[WHITE]['Empty'][0], self.square_width),
            'H4': Square(4, 'H', WHITE, self.matterial[WHITE]['Empty'][0], self.square_width),
            'H5': Square(5, 'H', BLACK, self.matterial[BLACK]['Empty'][0], self.square_width),
            'H6': Square(6, 'H', WHITE, self.matterial[BLACK]['Empty'][0], self.square_width),
            'H7': Square(7, 'H', BLACK, self.matterial[BLACK]['Pawn'][7], self.square_width),
            'H8': Square(8, 'H', WHITE, self.matterial[BLACK]['Rook'][1], self.square_width)
        }

    def convert_current_position(self, window_to_game: bool = True, window_position: WindowPosition = None, game_position: GamePosition = None):
        if window_to_game and not window_position:
            raise TypeError(
                "'window_to_game' was passed as True, but 'window_pos' was missing a value")
        if not window_to_game and not game_position:
            raise TypeError(
                "'window_to_game' was passed as False, but 'game_pos' was missing a value")
        if window_to_game:
            return get_string_from_sequence(tuple(str(i) for i in self.get_game_pos(*window_position)))
        elif not window_to_game:
            return get_string_from_sequence(tuple(str(i) for i in self.get_window_pos(*game_position)))

    def get_window_pos(self, rank: int, file: str) -> tuple[int, int]:
        x = self.possible_files.index(file)*self.square_width
        y = (rank-1)*self.square_height
        return x, y

    def get_game_pos(self, x: int, y: int) -> tuple[str, int]:
        file = self.possible_files[x//self.square_width]
        rank = y//self.square_height
        return file, rank

    def move(self, move: str, keep_current_turn: bool = False):
        if keep_current_turn:
            next(self.players)
        turn = next(self.players)
        color = turn.color
        first_letter = ''
        if len(move) >= 3:
            first_letter = move[0].lower()
            position = move[1:]
        else:
            position = move
            formatted_move = (move[0], move[1])
        if color == WHITE:
            king = self.squares['E1'].piece
        else:
            king = self.squares['E8'].piece
        if position == move and move[0] in self.possible_files:
            for square in self.squares:
                if square[0] == position[0]:
                    piece = self.squares[square].piece
                    if isinstance(piece, Pawn):
                        if piece.color == color:
                            if not piece.validate(formatted_move, self.squares.copy(), king):
                                print("Invalid move!")
                                move = input("Enter a move: ")
                                self.move(move, True)
                            self.squares[piece.file+str(
                                piece.rank)].piece, self.squares[move].piece = self.squares[move].piece, self.squares[piece.file+str(piece.rank)].piece
                            break
        if first_letter in self.possible_files:
            piece = self.squares[first_letter+str(int(formatted_move[1])-1)
                                 ] if color == WHITE else self.squares[first_letter+str(int(formatted_move[1])+1)]
            if isinstance(Piece, Pawn):
                if not piece.validate(formatted_move, self.squares.copy(), king):
                    print("Invalid move!")
                    move = input("Enter a move: ")
                    self.move(move, True)
                other_piece = self.squares[move].piece
                if other_piece.color != color:
                    self.matterial[other_piece.color][other_piece.name].remove(
                        other_piece)
                    self.squares[move].piece = Empty(
                        tuple(None for _ in range(11)))
                self.squares[Piece.file+str(
                    piece.rank)].piece, self.squares[move].piece = self.squares[move].piece, self.squares[piece.file+str(piece.rank)].piece
        if first_letter == 'k':
            piece = self.matterial[color]['King'][0]
            if not piece.validate(formatted_move, self.squares.copy()):
                print("Invalid move!")
                move = input("Enter a move: ")
                self.move(move, True)
            other_piece = self.squares[move].piece
            if other_piece.color != color:
                self.matterial[other_piece.color][other_piece.name].remove(
                    other_piece)
                self.squares[move].piece = Empty(
                    tuple(None for _ in range(11)))
            self.squares[piece.file+str(
                piece.rank)].piece, self.squares[move].piece = self.squares[move].piece, self.squares[piece.file+str(piece.rank)].piece
        if first_letter == 'n':
            possible_positions = Knight.get_possible_positions(formatted_move)
            for file, rank in possible_positions:
                piece = self.squares[file+str(rank)].piece
                if isinstance(piece, Knight):
                    if piece.validate(formatted_move, squares.copy(), king):
                        other_piece = self.squares[move].piece
                        if other_piece.color != color:
                            self.matterial[other_piece.color][other_piece.name].remove(
                                other_piece)
                            self.squares[move].piece = Empty(
                                tuple(None for _ in range(11)))
                        self.squares[move].piece, self.squares[piece.file+str(
                            piece.rank)].piece = self.squares[piece.file+str(self.rank)].piece, self.squares[move].piece
                        break
            else:
                print("Invalid move!")
                move = input("Enter a move: ")
                self.move(move, True)
        if first_letter == 'b':
            diagonals = self.squares[move[1:].upper()].get_diagonals()
            bishop1, bishop2 = self.matterial[color]['Bishop']
            if (bishop1.file, bishop1.rank) in diagonals[0] or (bishop1.file, bishop1.rank) in diagonals[1]:
                if not bishop1.validate(formatted_move, self.squares.copy(), king):
                    print("Invalid move!")
                    move = input("Enter a move: ")
                    self.move(move, True)
                other_piece = self.squares[move].piece
                if other_piece.color != color:
                    self.matterial[other_piece.color][other_piece.name].remove(
                        other_piece)
                    self.squares[move].piece = Empty(
                        tuple(None for _ in range(11)))
                self.squares[bishop1.file+str(
                    bishop1.rank)].piece, self.squares[position].piece = self.squares[position].piece, self.squares[bishop1.file+str(bishop1.rank)].piece
            elif (bishop2.file, bishop2.rank) in diagonals[0] or (bishop2.file, bishop2.rank) in diagonals[1]:
                if not bishop2.validate(formatted_move, self.squares.copy(), king):
                    print("Invalid move!")
                    move = input("Enter a move: ")
                    self.move(move, True)
                other_piece = self.squares[move].piece
                if other_piece.color != color:
                    self.matterial[other_piece.color][other_piece.name].remove(
                        other_piece)
                    self.squares[move].piece = Empty(
                        tuple(None for _ in range(11)))
                self.squares[bishop2.file+str(
                    bishop2.rank)].piece, self.squares[position].piece = self.squares[position].piece, self.squares[bishop2.file+str(bishop2.rank)].piece
        if first_letter == 'r':
            if isinstance(specifier, int):
                if not specifier in move:
                    print("Invalid move!")
                    move = input("Enter a move: ")
                    self.move(move, True)
                rook1, rook2 = self.matterial[color]['Rook']
                files = self.squares[move].get_files()
                if (rook1.file, rook1.rank) in files:
                    if (rook2.file, rook2.rank) in files:
                        print("Invalid move: ")
                        move = input("Enter a move: ")
                        self.move(move, True)
                    if rook1.validate(formatted_move, self.squares.copy(), king):
                        other_piece = self.squares[move].piece
                        if other_piece.color != color:
                            self.matterial[other_piece.color][other_piece.name].remove(
                                other_piece)
                            self.squares[move].piece = Empty(
                                tuple(None for _ in range(11)))
                        self.squares[rook1.file+str(
                            rook1.rank)].piece, self.squares[move].piece = self.squares[move].piece, self.squares[rook1.file+str(rook1.rank)]
                if (rook2.file, rook2.rank) in files:
                    if (rook1.file, rook1.rank) in files:
                        print("Invalid move: ")
                        move = input("Enter a move: ")
                        self.move(move, True)
                    if rook2.validate(formatted_move, self.squares.copy(), king):
                        other_piece = self.squares[move].piece
                        if other_piece.color != color:
                            self.matterial[other_piece.color][other_piece.name].remove(
                                other_piece)
                            self.squares[move].piece = Empty(
                                tuple(None for _ in range(11)))
                        self.squares[rook2.file+str(
                            rook2.rank)].piece, self.squares[move].piece = self.squares[move].piece, self.squares[rook2.file+str(rook2.rank)]
            elif isinstance(specifier, str):
                if not specifier in move:
                    print("Invalid move!")
                    move = input("Enter a move: ")
                    self.move(move, True)
                rook1, rook2 = self.matterial[color]['Rook']
                ranks = self.squares[move].get_ranks()
                if (rook1.file, rook1.rank) in ranks:
                    if (rook2.file, rook2.rank) in ranks:
                        print("Invalid move: ")
                        move = input("Enter a move: ")
                        self.move(move, True)
                    if rook1.validate(formatted_move, self.squares.copy(), king):
                        other_piece = self.squares[move].piece
                        if other_piece.color != color:
                            self.matterial[other_piece.color][other_piece.name].remove(
                                other_piece)
                            self.squares[move].piece = Empty(
                                tuple(None for _ in range(11)))
                        self.squares[rook1.file+str(
                            rook1.rank)].piece, self.squares[move].piece = self.squares[move].piece, self.squares[rook1.file+str(rook1.rank)]
                if (rook2.file, rook2.rank) in ranks:
                    if (rook1.file, rook1.rank) in ranks:
                        print("Invalid move: ")
                        move = input("Enter a move: ")
                        self.move(move, True)
                    if rook2.validate(formatted_move, self.squares.copy(), king):
                        other_piece = self.squares[move].piece
                        if other_piece.color != color:
                            self.matterial[other_piece.color][other_piece.name].remove(
                                other_piece)
                            self.squares[move].piece = Empty(
                                tuple(None for _ in range(11)))
                        self.squares[rook2.file+str(
                            rook2.rank)].piece, self.squares[move].piece = self.squares[move].piece, self.squares[rook2.file+str(rook2.rank)]
            else:
                ranks = self.squares[move].get_ranks()
                files = self.squares[move].get_files()
                rook1, rook2 = self.matterial[color]['Rook']
                if (rook1.file, rook1.rank) in ranks or (rook1.file, rook1.rank) in files:
                    if rook1.validate(formatted_move, self.squares.copy(), king):
                        self.squares[rook1.file+str(
                            rook1.rank)].piece, self.squares[move].piece = self.squares[move].piece, self.squares[rook1.file+str(rook1.rank)].piece
                elif (rook2.file, rook2.rank) in ranks or (rook2.file, rook2.rank) in files:
                    if rook2.validate(formatted_move, self.squares.copy(), king):
                        self.squares[rook2.file+str(
                            rook2.rank)].piece, self.squares[move].piece = self.squares[move].piece, self.squares[rook2.file+str(rook2.rank)].piece
        elif first_letter == 'q':
            piece = self.matterial[color]['Queen'][0]
            if not piece.validate(position, self.squares, self.matterial[color]['King'][0]):
                print("Invalid move!")
                move = input("Enter a move: ")
                self.move(move, True)
            other_piece = self.squares[move].piece
            if other_piece.color != color:
                self.matterial[other_piece.color][other_piece.name].remove(
                    other_piece)
                self.squares[move].piece = Empty(
                    tuple(None for _ in range(11)))
            self.squares[piece.file+str(
                piece.rank)].piece, self.squares[move].piece = self.squares[move].piece, self.squares[piece.file+str(piece.rank)].piece

    def draw_board(self, positions: PositionDict = {}):
        board = pygame.Surface((self.win_width, self.win_height))
        self.offset_box_1 = pygame.Surface((self.win_width, self.upper_offset))
        self.offset_box_2 = pygame.Surface((self.win_width, self.lower_offset))
        self.offset_box_1.fill(GREY), board.fill(
            GREY), self.offset_box_2.fill(GREY)
        if positions:
            for position, piece in positions:
                self.squares[position[0]+str(position[1])].draw(board, piece)
        else:
            print(self.squares['D2'].piece)
            print(self.squares['D4'].piece)
            for square in self.squares.values():
                square.draw(board)
        self.WINDOW.blit(board, (0, 0))
        pygame.display.update()

    def capture_piece(self):
        while True:
            captured_pieces = capture_piece(self.matterial)
            try:
                color, piece_name, i = next(captured_pieces)
                x, y = self.matterial[color][piece_name][i].x, self.matterial[color][piece_name][i].y
                if piece.x == x and piece.y == y:
                    captured_pieces.close()
                    captured_piece = self.matterial[color][piece_name].pop(i)
                    self.captured_pieces.append(captured_piece)
            except StopIteration:
                break
            except GeneratorExit:
                break

    def _update_square_attackers(self, attackers):
        for square in self.squares.values():
            if self.get_window_pos(square.rank, square.file) in attackers:
                square.attacked = True
            else:
                square.attacked = False

    def update_screen(self, move_info: tuple[list[Piece], WindowPosition, WindowPosition, Piece]):
        attacked_pieces, new_pos, old_pos, piece = move_info
        self._update_square_attackers(attacked_pieces)
        old_pos = get_string_from_sequence(
            tuple(str(i) for i in self.get_game_pos(*old_pos)))
        piece = self.squares[old_pos].piece
        self.squares[old_pos].piece = None
        new_pos = get_string_from_sequence(
            tuple(str(i) for i in self.get_game_pos(*new_pos)))
        old_piece = self.squares[new_pos].piece
        if not old_piece:
            self.squares[new_pos].piece = piece
        else:
            if old_piece.color != piece.color:
                self.capture_piece(old_piece.x, old_piece.y)
                self.squares[old_pos].piece = piece
        self.update()

    def update(self):
        self.draw_board()
        pygame.display.update()

    def end(self):
        if self.matterial[BLACK]['King'][0].checkmate(list(self.matterial[WHITE].values())):
            return WHITE
        elif self.matterial[WHITE]['King'][0].checkmate(list(self.matterial[BLACK].values())):
            return BLACK
        elif len(self.matterial[BLACK].values()) == 1:
            return WHITE
        elif len(self.matterial[WHITE].values()) == 1:
            return BLACK
        else:
            return None

    def promote(self, pawn: Pawn) -> None:
        table = Table(self.window, 2, 2, [
            ['Bishop', 'Knight'], ['Queen', 'Rook']])
        table.draw(bold=True, underline=True, size=80)
        cursor_x, cursor_y = (self.window.get_width()-262, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            if cursor_y == 600:
                cursor_x = self.window.get_width()
                cursor_y = 0
            else:
                cursor_y += 200
        if keys[pygame.K_RETURN]:
            if cursor_x < self.window.get_width()/2:
                selected_piece = self.matterial[pawn.color].keys()[
                    cursor_y/100]
            else:
                selected_piece = self.matterial[pawn.color].keys()[
                    cursor_y/100+texts_length//2]
            piece = pawn.promotion(selected_piece, self.images)
            piece_name = piece.name
            self.matterial[pawn.color][piece_name].append(piece)

    def find_player_by_color(self, color: pygame.Color) -> Player:
        for player in self.players:
            if player.color == color:
                return player
