import pygame
from pygame_gui.elements import ui_text_entry_line
from ..chess.CONSTANTS import (WHITE, BLACK, RED, MANAGER)
from .piece import Piece


class Knight(Piece):

    instances = []

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

    def _update_attacked_pieces(self, direction, x, y, square_width, square_height, squares):
        attacked_pieces = []
        xValues = [x for x in filter(function=lambda i: True if i.x == x or i.x == x+delta_x or i.x == x-delta_x else False, squares)]
        yValues = [y for y in filter(function=lambda i: False if i.y == y or i.y == y+delta_y else False, squares)]
        colors = []
        for square in squares:
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

    def move(self, squares, win, board):
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
                fnt = pygame.font.SysFont("comicsans", 40)
                txt = fnt.render(
                    "You can't select that piece because you have already selected a piece. You must either move the already selected piece or unselect it.")
                win.blit(txt, (self.max_x-(txt.get_width/2)/2, (self.x, self.y))
            self.file, self.rank=self.get_game_pos()
            for event in pygame.event.get():
                if event.type == pygame.K_SPACE or event.type == pygame.K_RETURN:
                    if (self.x, self.y, self.name) in pieces:
                        selected=False
                        self.pieces.pop()
                    else:
                        selected=True
                        self.pieces.append((self.x, self.y, self.name))
            keys=pygame.key.get_pressed()
            if ((keys[pygame.K_RALT] and keys[pygame.K_k]) or (keys[pygame.K_LALT] and keys[pygame.K_k])) and not ((keys[pygame.K_RALT] and keys[pygame.K_k]) and (keys[pygame.K_LALT] and keys[pygame.K_k])):
                active=False
                text_input_line=ui_text_entry_line(relative_rect=pygame.Rect(
                    self.x, self.y, self.square_width, self.square_height), manager=MANAGER)
                text_input_line.disable()
                text_input_line.set_allowed_characters(
                    [1, 2, 3, 4, 5, 6, 7, 8, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
                text_input_line.set_text_length_limit(2)
                if active:
                    text_input_line.enable()
                    text_input_line.focus()
                    if keys[pygame.K_RETURN]:
                        text=text_input_line.get_text()
                        file, rank=str(text[0]), int(text[1])
                        for instance in self.instances:
                            x, y=self.get_window_pos(rank, file)
                            if x, y in instance.attacked_pieces:
                                instance.x=x
                                instance.y=y
                                instance.has_moved=True
                                break
                else:
                    text_input_line.disable()
                    text_input_line.unfocus()
            while direction < max_direction:
                self.attacked_pieces=self._update_attacked_pieces(
                    direction, self.x, self.y, self.square_width, self.square_height, squares)
                direction += 1
            direction=0
        return self.attacked_pieces
