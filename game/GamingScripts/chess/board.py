from pathlib import Path
from os.path import join
import string
import pygame
from pygame import color

from .player_dict import PlayerDict
from ..pieces import Bishop, King, Knight, Pawn, Queen, Rook
from ..board_utils.square import Square
from .CONSTANTS import (WHITE, BLACK, GREY)
from .player import Player
from ..utils.Functions import get_string_from_sequence
from ..utils.types import Squares
from ..flatten import flatten


def capture_piece(matterial):
    for color, color_pieces in matterial:
        for piece_name, piece_list in color_pieces:
            if piece_list:
                for i, piece in enumerate(piece_list):
                    yield (color, piece_name, i)



class Board:

    def __init__(self, size: Tuple[int, int], square_width: int, square_height: int, player1: Player, player2: Player, window: pygame.Surface, upper_offset: int = 0, lower_offset: int = 0) -> None:
        """
        Initialize the Board class.
        """
        pygame.init()
        pygame.display.init()
        self.win_width, self.win_height = size
        self.square_width = square_width
        self.square_height = square_height
        self.players = PlayerDict({1: player1, 2: player2})
        self.window = window
        self.upper_offset = upper_offset
        self.lower_offset = lower_offset
        self.captured_pieces = []
        self.possible_files = string.ascii_uppercase[:8]
        self.path = Path(join("C:", "Users", "samar", "OneDrive", "Desktop",
                              "Python_Programming", "Chess", "game", "GamingScripts", "Chessmen"))
        self.images = {
            'BLACK': {
                'Bishop': join(self.path, 'B_Bishop.png'),
                'King': join(self.path, 'B_King.png'),
                'Knight': join(self.path, 'B_Knight.png'),
                'Pawn': join(self.path, 'B_Pawn.png'),
                'Queen': join(self.path, 'B_Queen.png'),
                'Rook': join(self.path, 'B_Rook.png')
            },
            'WHITE': {
                'Bishop': join(self.path, 'W_Bishop.png'),
                'King': join(self.path, 'W_King.png'),
                'Knight': join(self.path, 'W_Knight.png'),
                'Pawn': join(self.path, 'W_Pawn.png'),
                'Queen': join(self.path, 'W_Queen.png'),
                'Rook': join(self.path, 'W_Rook.png')
            }
        }
        self.matterial = {
            'BLACK': {
                'Bishop': [
                    Bishop(self.image['BLACK']['Bishop'], 'C', 8, BLACK, 0, self.win_width, 0, self.win_height,
                           self.square_width, self.square_height, self.win_width, self.win_height),
                    Bishop(self.image[BLACK]['Bishop'], 'F', 8, BLACK, 0, self.win_width, 0, self.win_height,
                           self.square_width, self.square_height, self.win_width, self.win_height)
                ],
                'King': [
                    King(self.images['BLACK']['King'], 'E', 8, BLACK, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height)
                ],
                'Knight': [
                    Knight(self.images['BLACK']['Knight'], 'B', 8, BLACK, 0, self.win_width, 0,
                           self.win_height, self.square_width, self.square_height, self.win_width, self.win_height),
                    Knight(self.images['BLACK']['Knight'], 'G', 8, BLACK, 0, self.win_width, 0,
                           self.win_height, self.square_width, self.square_height, self.win_width, self.win_height)
                ],
                'Pawn': [
                    Pawn(self.images['BLACK']['Pawn'], 'A', 7, BLACK, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn(self.images['BLACK']['Pawn'], 'B', 7, BLACK, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn(self.images['BLACK']['Pawn'], 'C', 7, BLACK, 0, self.win_width, 0, self.win_height, self.square_width, self.square_height, self.win_width, self.win_height),                    Pawn(
                        self.images['BLACK']['Pawn'], 'A', 7, BLACK, 0, self.win_width, 0, self.win_height, self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn(self.images['BLACK']['Pawn'], 'D', 7, BLACK, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn(self.images['BLACK']['Pawn'], 'E', 7, BLACK, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn(self.images['BLACK']['Pawn'], 'F', 7, BLACK, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn(self.images['BLACK']['Pawn'], 'G', 7, BLACK, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn(self.images['BLACK']['Pawn'], 'H', 7, BLACK, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height)
                ],
                'Queen': [
                    Queen(self.images['BLACK']['Queen'], 'D', 8, BLACK, 0, self.win_width, 0,
                          self.win_height, self.square_width, self.square_height, self.win_width, self.win_height)
                ],
                'Rook': [
                    Rook(self.images['BLACK']['Rook'], 'A', 8, BLACK, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Rook(self.images['BLACK']['Rook'], 'H', 8, BLACK, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height)
                ]
            },
            'WHITE': {
                'Bishop': [
                    Bishop(self.image['WHITE']['Bishop'], 'C', 2, BLACK, 0, self.win_width, 0, self.win_height,
                           self.square_width, self.square_height, self.win_width, self.win_height),
                    Bishop(self.image['WHITE']['Bishop'], 'F', 2, WHITE, 0, self.win_width, 0,
                           self.win_height, self.square_width, self.square_height, self.win_width, self.win_height)
                ],
                'King': [
                    King(self.images['WHITE']['King'], 'E', 1, WHITE, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height)
                ],
                'Knight': [
                    Knight(self.images['WHITE']['Knight'], 'B', 2, WHITE, 0, self.win_width, 0,
                           self.win_height, self.square_width, self.square_height, self.win_width, self.win_height),
                    Knight(self.images['WHITE']['Knight'], 'G', 2, WHITE, 0, self.win_width, 0,
                           self.win_height, self.square_width, self.square_height, self.win_width, self.win_height)
                ],
                'Pawn': [
                    Pawn(self.images['WHITE']['Pawn'], 'A', 2, WHITE, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn(self.images['WHITE']['Pawn'], 'B', 2, WHITE, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn(self.images['WHITE']['Pawn'], 'C', 2, WHITE, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn(self.images['WHITE']['Pawn'], 'D', 2, WHITE, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn(self.images['WHITE']['Pawn'], 'E', 2, WHITE, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn(self.images['WHITE']['Pawn'], 'F', 2, WHITE, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn(self.images['WHITE']['Pawn'], 'G', 2, WHITE, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Pawn(self.images['WHITE']['Pawn'], 'H', 2, WHITE, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height)
                ],
                'Queen': [
                    Queen(self.images['WHITE']['Queen'], 'D', 1, WHITE, 0, self.win_width, 0,
                          self.win_height, self.square_width, self.square_height, self.win_width, self.win_height)
                ],
                'Rook': [
                    Rook(self.images['WHITE']['Rook'], 'A', 1, WHITE, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height),
                    Rook(self.images['WHITE']['Rook'], 'H', 1, WHITE, 0, self.win_width, 0, self.win_height,
                         self.square_width, self.square_height, self.win_width, self.win_height)
                ]
            }
        }
        self.squares = {
            'A1': Square(1, 'A', BLACK, self.matterial['WHITE']['Rook'][0], self.square_width),
            'A2': Square(2, 'A', WHITE, self.matterial['WHITE']['Pawn'][0], self.square_width),
            'A3': Square(3, 'A', BLACK, None, self.square_width),
            'A4': Square(4, 'A', WHITE, None, self.square_width),
            'A5': Square(5, 'A', BLACK, None, self.square_width),
            'A6': Square(6, 'A', WHITE, None, self.square_width),
            'A7': Square(7, 'A', BLACK, self.matterial['BLACK']['Pawn'][0], self.square_width),
            'A8': Square(8, 'A', WHITE, self.matterial['BLACK']['Rook'][0], self.square_width),
            'B1': Square(1, 'B', WHITE, self.matterial['WHITE']['Knight'][0], self.square_width),
            'B2': Square(2, 'B', BLACK, self.matterial['WHITE']['Pawn'][1], self.square_width),
            'B3': Square(3, 'B', WHITE, None, self.square_width),
            'B4': Square(4, 'B', BLACK, None, self.square_width),
            'B5': Square(5, 'B', WHITE, None, self.square_width),
            'B6': Square(2, 'B', BLACK, None, self.square_width),
            'B7': Square(7, 'B', WHITE, self.matterial['BLACK']['Pawn'][1], self.square_width),
            'B8': Square(8, 'B', BLACK, self.matterial['BLACK']['Knight'][0], self.square_width),
            'C1': Square(1, 'C', BLACK, self.matterial['WHITE']['Bishop'][0], self.square_width),
            'C2': Square(2, 'C', WHITE, self.matterial['WHITE']['Pawn'][2], self.square_width),
            'C3': Square(3, 'C', BLACK, None, self.square_width),
            'C4': Square(2, 'C', WHITE, None, self.square_width),            'C2': Square(2, 'C', WHITE, None, self.square_width),
            'C5': Square(5, 'C', BLACK, None, self.square_width),
            'C6': Square(6, 'C', WHITE, None, self.square_width),
            'C7': Square(7, 'C', BLACK, self.matterial['BLACK']['Pawn'][2], self.square_width),
            'C8': Square(8, 'C', WHITE, self.matterial['BLACK']['Bishop'][0], self.square_width),
            'D1': Square(1, 'D', WHITE, self.matterial['WHITE']['Queen'][0], self.square_width),
            'D2': Square(2, 'D', BLACK, self.matterial['WHITE']['Pawn'][3], self.square_width),
            'D3': Square(3, 'D', WHITE, None, self.square_width),
            'D4': Square(2, 'D', BLACK, None, self.square_width),
            'D5': Square(5, 'D', WHITE, None, self.square_width),
            'D6': Square(6, 'D', BLACK, None, self.square_width),
            'D7': Square(7, 'D', WHITE, self.matterial['BLACK']['Pawn'][3], self.square_width),
            'D8': Square(8, 'D', BLACK, self.matterial['BLACK']['Queen'][0], self.square_width),
            'E1': Square(1, 'E', BLACK, self.matterial['WHITE']['King'][0], self.square_width),
            'E2': Square(2, 'E', WHITE, self.matterial['WHITE']['Pawn'][4], self.square_width),
            'E3': Square(3, 'E', BLACK, None, self.square_width),
            'E4': Square(4, 'E', WHITE, None, self.square_width),
            'E5': Square(5, 'E', BLACK, None, self.square_width),
            'E6': Square(6, 'E', WHITE, None, self.square_width),
            'E7': Square(2, 'E', BLACK, self.matterial['BLACK']['Pawn'][4], self.square_width),
            'E8': Square(8, 'E', WHITE, self.matterial['BLACK']['King'][0], self.square_width),
            'F1': Square(1, 'F', WHITE, self.matterial['WHITE']['Bishop'][1], self.square_width),
            'F2': Square(2, 'F', BLACK, self.matterial['WHITE']['Pawn'][5], self.square_width),
            'F3': Square(3, 'F', WHITE, None, self.square_width),
            'F4': Square(4, 'F', BLACK, None, self.square_width),
            'F5': Square(5, 'F', WHITE, None, self.square_width),
            'F6': Square(6, 'F', BLACK, None, self.square_width),
            'F7': Square(7, 'F', WHITE, self.matterial['BLACK']['Pawn'][5], self.square_width),
            'F8': Square(1, 'F', BLACK, self.matterial['WHITE']['Bishop'][1], self.square_width),
            'G1': Square(1, 'G', BLACK, self.matterial['WHITE']['Knight'][1], self.square_width),
            'G2': Square(2, 'G', WHITE, self.matterial['WHITE']['Pawn'][6], self.square_width),
            'G3': Square(2, 'G', BLACK, None, self.square_width),
            'G4': Square(4, 'G', WHITE, None, self.square_width),
            'G5': Square(5, 'G', BLACK, None, self.square_width),
            'G6': Square(6, 'G', WHITE, None, self.square_width),
            'G7': Square(7, 'G', BLACK, self.matterial['BLACK']['Pawn'][6], self.square_width),
            'G8': Square(8, 'G', WHITE, self.matterial['WHITE']['Knight'][1], self.square_width),
            'H1': Square(1, 'H', WHITE, self.matterial['WHITE']['Rook'][1], self.square_width),
            'H2': Square(2, 'H', BLACK, self.matterial['WHITE']['Pawn'][7], self.square_width),
            'H3': Square(3, 'H', WHITE, None, self.square_width),
            'H4': Square(4, 'H', BLACK, None, self.square_width),
            'H5': Square(5, 'H', WHITE, None, self.square_width),
            'H6': Square(6, 'H', BLACK, None, self.square_width),
            'H7': Square(7, 'H', WHITE, self.matterial['BLACK']['Pawn'][7], self.square_width),
            'H8': Square(8, 'H', BLACK, self.matterial['WHITE']['Rook'][1], self.square_width)
        }

    def get_window_pos(self, rank: int, file: str) -> Tuple[int, int]:
        x = self.possible_files.index(file)*self.square_width
        y = (rank-1)*self.square_height
        return x, y

    def get_game_pos(self, x: int, y: int) -> Tuple[str, int]:
        file = self.possible_files[x//self.square_width]
        rank = y/self.square_height+1
        return file, rank

    def move(self):
        for color in self.matterial.values():
            for piece_list in color.values():
                if piece_list:
                    for piece in piece_list:
                        move_info = piece.move(self.window, self.squares)
                        self.update_screen(move_info)

    def draw_board(self):
        board = pygame.Surface((self.win_width, self.win_height))
        self.offset_box_1 = pygame.Surface((self.win_width, self.upper_offset))
        self.offset_box_2 = pygame.Surface((self.win_width, self.lower_offset))
        self.offset_box_1.fill(GREY), board.fill(
            GREY), self.offset_box_2.fill(GREY)
        for square in self.squares.values():
            square.draw(board)
        self.window.blit(self.offset_box_1, (0, 0))
        self.window.blit(board, (0, self.offset_box_1.get_height()))
        self.window.blit(
            self.offset_box_2, (0, self.offset_box_1.get_height()+board.get_height()))

    def capture_piece(self):
        while True:
            captured_pieces = capture_piece(self.matterial)
            try:
                color, piece_name, i = next(captured_pieces)
                x,y = self.matterial[color][piece_name][i].x, self.matterial[color][piece_name][i].y
                if piece.x == x and piece.y == y:
                    captured_pieces.close()
                    captured_piece = self.matterial[color][piece_name].pop(i)
                    self.captured_pieces.append(captured_piece)
                    self.draw_captured_piece(captured_piece)
                except StopIteration:
                    break
                except GeneratorExit:
                    break

    def draw_captured_piece(self, captured_piece):
        if self.player1.color != captured_piece.color:
            for x in range(0, self.win_width, 100):
                for y in range(0, self.upper_offset, 100):
                    pixel_color = self.offset_box_1.get_at((x, y))
                    if (pixel_color.r, pixel_color.g, pixel_color.b) == GREY:
                        self.offset_box_1.blit(captured_piece, (x, y))
        if self.player2.color != captured_piece.color:
            for x in range(0, self.win_width, 100):
                for y in range(0, self.lower_offset, 100):
                    pixel_color = self.offset_box_2.get_at((x, y))
                    if (pixel_color.r, pixel_color.g, pixel_color.b) == GREY:
                        self.offset_box_2.blit(captured_piece, (x, y))
        pygame.display.update()

    def update_screen(self, move_info: tuple):
        self.draw_board()
        attacked_pieces, new_pos, old_pos, piece = move_info
        for attacked_piece in attacked_pieces:
            x, y = attacked_piece[0]
            position = self.get_game_pos(x, y)
            position = get_string_from_sequence(position)
            self.squares[position].attacked = True
        x, y = old_pos
        old_pos = self.get_game_pos(x, y)
        old_pos = get_string_from_sequence(old_pos)
        piece = self.squares[old_pos].piece
        self.squares[old_pos].piece = None
        x, y = new_pos
        new_pos = self.get_game_pos(x, y)
        new_pos = get_string_from_sequence(new_pos)
        old_piece = self.squares[old_pos].piece
        if not old_piece:
            self.squares[old_pos].piece = piece
        else:
            if old_piece.color != piece.color:
                self.capture_piece(old_piece.x,old_piece.y)
                self.squares[old_pos].piece = piece
        self.update()
    
    def update(self):
        pygame.display.update