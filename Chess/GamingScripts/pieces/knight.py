import pygame
#import string

#from pygame_gui.elements.ui_text_entry_line import UITextEntryLine
from typing import Sequence, Literal

from board_utils import Square
from chess.CONSTANTS import (SQUARE_WIDTH, WHITE, BLACK, RED, BLUE_GREEN)
from .piece import Piece
from flatten import flatten
from utils.types import (
    Position, Positions, Squares
)
from utils.functions import get_game_pos, get_string_from_sequence, get_window_pos


class Knight(Piece):

    def __init__(self, image, file, rank, color, min_x, max_x, min_y, max_y, square_width, square_height, win_width, win_height):
        pygame.init()
        self.image = image
        self.image_surface = pygame.image.load(self.image)
        self.rank = rank
        self.file = file
        self.color = color
        self.name = 'Knight'
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.square_width = square_width
        self.square_height = square_height
        self.win_width = win_width
        self.win_height = win_height
        self.piece_x, self.piece_y = pygame.mouse.get_pos()
        self.x, self.y = self.piece_x, self.piece_y
        self.attacked_pieces = []
        self.has_moved = False
        super().__init__(self.image, self.file, self.rank, self.name,
                         self.color, self.square_width, self.square_height)

    def get_attacked_positions(self, x: int, y: int):
        positions = []
        for i in range(1, 3):
            if x-self.square_width*i >= 0 and 0 <= y <= self.win_height-self.square_height:
                positions.append((x-self.square_width*i, y))
            if x+self.square_width*i <= self.win_width and 0 <= y <= self.win_height-self.square_height:
                positions.append((x+self.square_width*i, y))
            if 0 <= x <= self.win_width-self.square_width and y-self.square_height*i >= 0:
                positions.append(x, y-self.square_height*i)
            if 0 <= x <= self.win_width-self.square_width and y+self.square_height*i <= self.win_height-self.square_height:
                positions.append((x, y+self.square_height*i))
        return positions

    def _update_attacked_pieces(self, x: int, y: int, square_width: int, square_height: int, squares: Squares) -> list:
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

    def get_possible_positions(self, current_position: Position, squares: Squares) -> Positions:
        file, rank = current_position
        backLeft1 = get_string_from_sequence((self.possible_files[self.possible_files.index(
            file)-1], rank-2) if file != self.possible_files[0] and rank > 2 else (None, 0))
        backRight1 = get_string_from_sequence((self.possible_files[self.possible_files.index(
            file)+1], rank-2) if file != self.possible_files[-1] and rank > 2 else (None, 0))
        backRight2 = get_string_from_sequence((self.possible_files[self.possible_files.index(
            file)+2], rank-1) if file not in self.possible_files[-2:] and rank > 1 else (None, 0))
        forwardRight2 = get_string_from_sequence((self.possible_files[self.possible_files.index(
            file)+2], rank+1) if file not in self.possible_files[-2:] and rank < 8 else (None, 0))
        forwardRight1 = get_string_from_sequence((self.possible_files[self.possible_files.index(
            file)+1], rank+2) if file != self.possible_files[-1] and rank < 7 else (None, 0))
        forwardLeft1 = get_string_from_sequence((self.possible_files[self.possible_files.index(
            file)-1], rank+2) if file != self.possible_files[0] and rank < 7 else (None, 0))
        forwardLeft2 = get_string_from_sequence((self.possible_files[self.possible_files.index(
            file)-2], rank+1) if file != self.possible_files[:2] and rank < 8 else (None, 0))
        backLeft2 = get_string_from_sequence((self.possible_files[self.possible_files.index(
            file)-2], rank-1) if file != self.possible_files[:2] and rank > 1 else (None, 0))
        return list(filter((lambda i: (squares[i].piece.color != self.color and all(i))), [backLeft1, backLeft2, backRight1, backRight2, forwardRight1, forwardRight2, forwardLeft1, forwardLeft2]))

    def find_piece_from_move_set(self, move_set: Positions, squares: Squares):
        for square in move_set:
            piece_at_current_position = squares[square].piece
            if piece_at_current_position is self:
                return piece_at_current_position

    def move(self, squares: Squares, win: pygame.Surface, board):
        if not isinstance(squares, list):
            raise TypeError(
                "The squares arguement must be a list(), not "+str(type(squares))[8:-1]+"().")
        limiting_pos = [[self.min_x, max_x], [self.min_y, self.max_y]]
        max_length = 1
        selected = False
        direction = 0
        max_direction = 8
        direction_offset = 0
        pygame.font.init()
        while (self.x in limiting_pos[0] and self.y in limiting_pos[1]):
            if len(self.pieces) > max_length:
                font = pygame.font.SysFont("comicsans", 40)
                text = font.render(
                    "You can't select that piece because you have already selected a piece. You must either move the already selected piece or unselect it.", 1, DARK_GREEN)
                win.blit(txt, ((self.max_x-txt.get_width()) /
                               2, (self.max_y-txt.get_height())/2))
            for event in pygame.event.get():
                if event.type == pygame.K_SPACE or event.type == pygame.K_RETURN:
                    if (self.x, self.y, self.name) in pieces:
                        selected = False
                        self.pieces.pop()
                    else:
                        selected = True
                        self.pieces.append((self.x, self.y, self.name))
            keys = pygame.key.get_pressed()
            if ((keys[pygame.K_RALT] and keys[pygame.K_k]) or (keys[pygame.K_LALT] and keys[pygame.K_k])) and not ((keys[pygame.K_RALT] and keys[pygame.K_k]) and (keys[pygame.K_LALT] and keys[pygame.K_k])):
                while True:
                    text = "Choose direction of movement: (d, or u)"
                    font = font.render(text, 1, BLUE_GREEN)
                    win.fill(WHITE)
                    win.blit(txt, ((self.max_x-txt.get_width()) /
                                   2, (self.max_y-txt.get_height())/2))
                    if keys[pygame.K_d]:
                        text = "Choose number of steps: (1 or 2))"
                        font = font.render(text, 1, BLUE_GREEN)
                        win.fill(WHITE)
                        win.blit(txt, ((self.max_x-txt.get_width()) /
                                 2, (self.max_y-txt.get_height())/2))
                        if keys[pygame.K_1]:
                            text = "Choose direction of movement: (l, or r)"
                            font = font.render(text, 1, BLUE_GREEN)
                            win.fill(WHITE)
                            win.blit(txt, ((self.max_x-txt.get_width()) /
                                     2, (self.max_y-txt.get_height())/2))
                            if keys[pygame.K_l]:
                                self.rank -= 1
                                self.file = self.possible_files[self.possible_files.index(
                                    self.file)-2]
                            if keys[pygame.K_r]:
                                self.rank -= 1
                                self.file = self.possible_files[self.possible_files.index(
                                    self.file)+2]
                        if keys[pygame.K_2]:
                            text = "Choose direction of movement: (l, or r)"
                            font = font.render(text, 1, BLUE_GREEN)
                            win.fill(WHITE)
                            win.blit(txt, ((self.max_x-txt.get_width()) /
                                     2, (self.max_y-txt.get_height())/2))
                            if keys[pygame.K_l]:
                                self.rank -= 2
                                self.file = self.possible_files[self.possible_files.index(
                                    self.file)-1]
                            if keys[pygame.K_r]:
                                self.rank -= 2
                                self.file = self.possible_files[self.possible_files.index(
                                    self.file)+1]
                    if keys[pygame.K_u]:
                        text = "Choose number of steps: (1 or 2)"
                        font = font.render(text, 1, BLUE_GREEN)
                        win.fill(WHITE)
                        win.blit(txt, ((self.max_x-txt.get_width()) /
                                 2, (self.max_y-txt.get_height())/2))
                        if keys[pygame.K_1]:
                            text = "Choose direction of movement: (l, or r)"
                            font = font.render(text, 1, BLUE_GREEN)
                            win.fill(WHITE)
                            win.blit(txt, ((self.max_x-txt.get_width()) /
                                     2, (self.max_y-txt.get_height())/2))
                            if keys[pygame.K_l]:
                                self.rank += 1
                                self.file = self.possible_files[self.possible_files.index(
                                    self.file)-2]
                            if keys[pygame.K_r]:
                                self.rank += 1
                                self.file = self.possible_files[self.possible_files.index(
                                    self.file)+2]
                        if keys[pygame.K_2]:
                            text = "Choose direction of movement: (l, or r)"
                            font = font.render(text, 1, BLUE_GREEN)
                            win.fill(WHITE)
                            win.blit(txt, ((self.max_x-txt.get_width()) /
                                     2, (self.max_y-txt.get_height())/2))
                            if keys[pygame.K_l]:
                                self.rank += 2
                                self.file = self.possible_files[self.possible_files.index(
                                    self.file)-1]
                            if keys[pygame.K_r]:
                                self.rank += 2
                                self.file = self.possible_files[self.possible_files.index(
                                    self.file)+1]
            while direction < max_direction:
                self.attacked_pieces = self._update_attacked_pieces(
                    self.x, self.y, self.square_width, self.square_height, squares)
                direction += 1
            direction = 0
        return self.attacked_pieces, (self.piece_x, self.piece_y), (original_x, original_y), self
