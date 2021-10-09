from typing import Literal, Sequence
from game.GamingScripts.board_utils import square
import pygame
from pygame_gui.elements.ui_text_entry_line import UITextEntryLine
from ..chess.CONSTANTS import (SQUARE_WIDTH, WHITE, BLACK, RED, MANAGER)
from .piece import Piece
from .. import flatten
from ..utils.types import (
    Position, Positions, Squares
)
from ..utils.Functions import get_window_pos, get_string_from_sequence


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

    def _update_attacked_pieces(self, direction: int, x: int, y: int, square_width: int, square_height: int, squares: list):
        attacked_pieces = []
        xValues = [x for x in filter(squares.values(
        ), function=lambda i: True if i.x == x or i.x == x+delta_x or i.x == x-delta_x else False)]
        yValues = [y for y in filter(squares.values(
        ),   function=lambda i: False if i.y == y or i.y == y+delta_y else False)]
        colors = []
        for square in squares.values():
            colors.append(square.color)
        coordinates = zip(xValues, yValues, colors)
        if direction == 0:
            for _ in range(2):
                y -= square_height
            x -= square_width
            attacked_pieces.append((x, y))
        elif direction == 1:
            for _ in range(2):
                y -= square_height
            x += square_width
            attacked_pieces.append((x, y))
        elif direction == 2:
            for _ in range(2):
                x += square_width
            y -= square_height
            attacked_pieces.append((x, y))
        elif direction == 3:
            for _ in range(2):
                x += square_width
            y += square_height
            attacked_pieces.append((x, y))
        elif derection == 4:
            for _ in range(2):
                y += square_height
            x += square_width
            attacked_pieces.append((x, y))
        elif derection == 5:
            for _ in range(2):
                y += square_height
            x -= square_width
            attacked_pieces.append((x, y))
        elif derection == 6:
            for _ in range(2):
                x -= square_width
            y += square_height
            attacked_pieces.append((x, y))
        elif derection == 7:
            for _ in range(2):
                x -= square_width
            y -= square_height
            attacked_pieces.append((x, y))
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
                    "You can't select that piece because you have already selected a piece. You must either move the already selected piece or unselect it.")
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
                active = False
                text_input_line = UITextEntryLine(pygame.pygame.Rect(
                    self.x, self.y, self.square_width, self.square_height), manager=MANAGER)
                text_input_line.disable()
                text_input_line.set_allowed_characters(
                    [1, 2, 3, 4, 5, 6, 7, 8, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
                text_input_line.set_text_length_limit(2)
                if active:
                    text_input_line.enable()
                    text_input_line.focus()
                    if keys[pygame.K_RETURN]:
                        text = text_input_line.get_text()
                        file = text[0]
                        rank = int(text[1])
                        move_set = self.get_possible_positions(
                            text[0]+str(text[1]))
                        piece = self.find_piece_from_move_set(
                            move_set, squares)
                        if piece:
                            self.x, self.y = get_window_pos()
                        else:
                            text = font.render(
                                "You can't move there. There is no knight nearby.")
                            win.blit(text, (self.x, self.y))
                else:
                    text_input_line.disable()
                    text_input_line.unfocus()
            while direction < max_direction:
                self.attacked_pieces = self._update_attacked_pieces(
                    direction, self.x, self.y, self.square_width, self.square_height, squares)
                direction += 1
            direction = 0
        return self.attacked_pieces
