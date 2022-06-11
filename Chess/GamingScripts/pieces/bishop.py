import pygame
from utils.functions import get_game_pos, get_window_pos
from .piece import Piece


class Bishop(Piece):

    def __init__(self, image, file, rank, color, min_x, max_x, min_y, max_y, square_width, square_height, win_width, win_height):
        pygame.init()
        self.image = image
        self.image_surface = pygame.image.load(image)
        self.file = file
        self.rank = rank
        self.color = color
        self.name = 'Bishop'
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.square_width = square_width
        self.square_height = square_height
        self.win_width = win_width
        self.win_height = win_height
        self.x, self.y = self.piece_x, self.piece_y = get_window_pos(
            self.file, self.rank, super().possible_files)
        self.attacked_pieces = []
        super().__init__(self.image, self.file, self.rank, self.name, self.color)

    def move(self, squares: dict, win: pygame.Surface):
        if not isinstance(squares, dict):
            raise TypeError('The squares attribute must be a dict.')
        if self.square_height != self.square_width:
            raise TypeError(
                'The height and width of the square must be the same.')
        limiting_pos = [[self.min_x, self.max_x], [self.min_y, self.max_y]]
        pieces = []
        max_length = 1
        selected = False
        direction = 0
        max_direction = 4
        pygame.font.init()
        for other in squares.values():
            other_piece = other.piece
            while (self.x in limiting_pos[0] and self.y in limiting_pos[1]):
                if len(pieces) > max_length:
                    fnt = pygame.font.SysFont("comicsans", 40)
                    txt = fnt.render(
                        "You can't select that piece because you have already selected a piece. You must either move the already selected piece or unselect it.")
                    win.blit(txt, (self.max_x-(txt.get_width/2) /
                                   2, self.max_y-(txt.get_height()/2)/2))
                self.x, self.y = self.get_window_pos()
                original_x, original_y = self.x, self.y
                for event in pygame.event.get():
                    if event.type == pygame.K_SPACE or event.type == pygame.K_KP5:
                        if (self.x, self.y, self.name) in pieces:
                            selected = False
                            pieces.pop()
                        else:
                            selected = True
                            pieces.append((self.x, self.y, self.name))
                keys = pygame.key.get_pressed()
                if (keys[pygame.K_KP1] or keys[pygame.K_1]) and not (keys[pygame.K_1] and keys[pygame.K_KP1]):
                    self.x -= self.square_width
                    self.y += self.square_height
                    if self.y == other.piece_y and self.x == other.piece_x:
                        if other_piece.color == self.color:
                            self.x += self.square_width
                            self.y -= self.square_height
                        else:
                            self.attacked_pieces.append(other_piece)
                    self.piece_x = self.x
                    self.piece_y = self.y
                if (keys[pygame.K_KP3] or keys[pygame.K_3]) and not (keys[pygame.K_3] and keys[pygame.K_KP3]):
                    self.x -= self.square_width
                    self.y -= self.square_height
                    if self.x == other.piece_x and self.y == other.piece_y:
                        if other_piece.color == self.color:
                            self.x += self.square_width
                            self.y += self.square_width
                        else:
                            self.attacked_pieces.append(other_piece)
                    self.piece_x = self.x
                    self.piece_y = self.y
                if (keys[pygame.K_KP7] or keys[pygame.K_7]) and not (keys[pygame.K_KP7] and keys[pygame.K_7]):
                    self.x -= self.square_width
                    self.y -= self.square_height
                    if self.x == other.piece_x and self.y == other.piece_y:
                        if other_piece.color == self.color:
                            self.x += self.square_width
                            self.y += self.square_height
                        else:
                            self.attacked_pieces.append(other_piece)
                    self.piece_x = self.x
                    self.piece_y = self.y
                if (keys[pygame.K_KP9] or keys[pygame.K_9]) and not (keys[pygame.K_KP9] and keys[pygame.K_9]):
                    self.x += self.SQUARE_width
                    self.y -= self.square_height
                    if self.y == other.piece_y and self.x == other.piece_x:
                        if other_piece.color == self.color:
                            self.x -= self.square_width
                            self.y += self.square_height
                        else:
                            self.attacked_pieces.append(other_piece)
                    self.piece_y = self.y
                while direction < max_direction:
                    if direction == 0:
                        while self.x >= 0 and self.y <= win_height-self.square_height:
                            self.x -= self.square_width
                            self.y += self.square_height
                            if not (self.y == other.piece_y and self.x == other.piece_x):
                                self.attacked_pieces.append(
                                    ((self.x, self.y),))
                                continue
                            else:
                                if other.color != self.color:
                                    self.attacked_pieces.append(
                                        (self.x, self.y))
                                    break
                    if direction == 1:
                        while self.x <= self.win_width-self.square_width and self.y <= self.win_height-square_height:
                            self.x += self.square_width
                            self.y += self.square_height
                            if not (self.x == other.piece_x and self.y == other.piece_y):
                                self.attacked_pieces.append(
                                    ((self.x, sllf.y),))
                                continue
                            else:
                                self.x -= self.square_width
                                self.y -= self.square_height
                                if other.color != self.color:
                                    self.attacked_pieces.append(
                                        ((self.x, self.y), other_piece))
                                    break
                    if direction == 2:
                        while self.x >= 0 and self.y >= 0:
                            self.x -= self.square_width
                            self.y -= self.square_height
                            if not (self.x == other.piece_x and self.x == other.piece_y):
                                self.attacked_pieces.append(
                                    ((self.x, self.y),))
                                continue
                            else:
                                self.x += self.square_width
                                self.y += self.square_height
                                if other.color != self.color:
                                    self.attacked_pieces.append(
                                        (self.x, self.y))
                                    break
                    if direction == 3:
                        while self.x <= self.win_width-self.square_width and self.y >= 0:
                            self.x += self.square_width
                            self.y -= self.square_height
                            if not (self.x == other.piece_x and self.y == other.piece_y):
                                self.attacked_pieces.append(
                                    ((self.x, self.y),))
                                continue
                            else:
                                self.x += self.square_width
                                self.y -= self.square_height
                                if other.color != self.color:
                                    self.attacked_pieces.append(
                                        ((self.x, self.y), other_piece))
                                    break
                    direction += 1
        self.x, self.y = self.piece_x, self.piece_y
        return self.attacked_pieces, (self.piece_x, self.piece_y), (original_x, original_y), self
