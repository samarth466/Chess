import pygame
from .piece import Piece


class Queen(Piece):

    def __init__(self, image, file, rank, color, min_x, max_x, min_y, max_y, square_width, square_height, win_width, win_height):
        pygame.init()       # initialize pygame
        self.image = image      # location of the image representation of piece
        # loads the image for piece into pygame
        self.image_surface = pygame.image.load(image)
        self.rank = rank       # rank of piece as represented in a chess game
        self.file = file      # file of piece as represented in a chess game
        self.color = color      # color of the piece (black or white)
        self.name = 'Queen'      # name of this piece
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.square_width = square_width       # width of a single square position
        self.square_height = square_height        # height of single square position
        self.win_width = win_width       # width of the window
        self.win_height = win_height      # height of the window
        self.x, self.y = self.get_window_pos()
        self.piece_x, self.piece_y = self.x, self.y
        self.attacked_pieces = []      # list of pieces being attacked by self
        self.attackers = []      # list of pieces attacking self
        super().__init__(self.image, self.file, self.rank, self.name, self.color)

    def move(self, squares: dict, win: pygame.Surface) -> list:
        # we need to loop through squares, so we must make sure that square is a list as we need to associate the position with a Square instance
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
        max_direction = 8
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
                self.file, self.rank = self.get_game_pos()
                for event in pygame.event.get():
                    if event.type == pygame.K_SPACE or event.type == pygame.K_KP5:
                        if (self.x, self.y, self.name) in pieces:
                            selected = False
                            pieces.pop()
                        else:
                            selected = True
                            pieces.append((self.x, self.y, self.name))
                keys = pygame.key.get_pressed()
                if ((keys[pygame.K_RCTRL] and keys[pygame.K_1]) or (keys[pygame.K_RCTRL] and keys[pygame.K_KP1])) and not ((keys[pygame.K_RCTRL] and keys[pygame.K_1]) and (keys[pygame.K_RCTRL] and keys[pygame.K_KP1])):
                    self.x -= self.square_width
                    self.y += self.square_height
                    if self.x == other_piece.piece_x and self.y == other_piece.piece_y:
                        if self.color == other_piece.color:
                            self.x += self.square_width
                            self.y -= self.square_height
                        else:
                            self.attacked_pieces.append(other_piece)
                        self.piece_x, self.piece_y = self.x, self.y
                if ((keys[pygame.K_RCTRL] and keys[pygame.K_2]) or (keys[pygame.K_RCTRL] and keys[pygame.K_KP2])) and not ((keys[pygame.K_RCTRL] and keys[pygame.K_2]) and (keys[pygame.K_RCTRL] and keys[pygame.K_RCTRL] and keys[pygame.K_KP2])):
                    self.y += self.square_height
                    if self.y == other.piece_y and self.x == other.piece_x:
                        if self.color == other_piece.color:
                            self.y -= self.square_height
                        else:
                            self.attacked_pieces.append(other_piece)
                    self.piece_y = self.y
                if ((keys[pygame.K_RCTRL] and keys[pygame.K_3]) or (keys[pygame.K_RCTRL] and keys[pygame.K_KP3])) and not ((keys[pygame.K_RCTRL] and keys[pygame.K_3]) and (keys[pygame.K_RCTRL] and keys[pygame.K_KP3])):
                    self.x += self.square_width
                    self.y += self.square_height
                    if self.x == other_piece.piece_x and self.y == other_piece.piece_y:
                        if self.color == other_piece.color:
                            self.x -= self.square_width
                            self.y -= self.square_height
                        else:
                            self.attacked_pieces.append(other_piece)
                        self.piece_x, self.piece_y = self.x, self.y
                if ((keys[pygame.K_RCTRL] and keys[pygame.K_KP4]) or (keys[pygame.K_RCTRL] and keys[pygame.K_4])) and not ((keys[pygame.K_RCTRL] and keys[pygame.K_4]) and (keys[pygame.K_RCTRL] and keys[pygame.K_KP4])):
                    self.x -= self.square_width
                    if self.x == other.piece_x and self.y == other.piece_y:
                        if self.color == other_piece.color:
                            self.x += self.square_width
                        else:
                            self.attacked_pieces.append(other_pieces)
                    self.piece_x = self.x
                if ((keys[pygame.K_RCTRL] and keys[pygame.K_6]) or (keys[pygame.K_KP6] and keys[pygame.K_6])) and not ((keys[pygame.K_RCTRL] and keys[pygame.K_6]) and (keys[pygame.K_RCTRL] and keys[pygame.K_KP6])):
                    self.x += self.square_width
                    if self.x == other.piece_x and self.y == other.piece_y:
                        if self.color == other_piece.color:
                            self.x -= self.square_width
                        else:
                            self.attacked_pieces.append(other_piece)
                    self.piece_x = self.x
                if ((keys[pygame.K_RCTRL] and keys[pygame.K_7]) or (keys[pygame.K_RCTRL] and keys[pygame.K_KP7])) and not ((keys[pygame.K_RCTRL] and keys[pygame.K_7]) and (keys[pygame.K_RCTRL] and keys[pygame.K_KP7])):
                    self.x -= self.square_width
                    self.y -= self.square_height
                    if self.x == other_piece.piece_x and self.y == other_piece.piece_y:
                        if self.color == other_piece.color:
                            self.x += self.square_width
                            self.y += self.square_height
                        else:
                            self.attacked_pieces.append(other_piece)
                        self.piece_x, self.piece_y = self.x, self.y
                if ((keys[pygame.K_RCTRL] and keys[pygame.K_KP8]) or (keys[pygame.K_RCTRL] and keys[pygame.K_8])) and not ((keys[pygame.K_RCTRL] and keys[pygame.K_8]) and (keys[pygame.K_RCTRL] and keys[pygame.K_KP8])):
                    self.y -= self.square_height
                    if self.y == other.piece_y and self.x == other.piece_x:
                        if self.color == other_piece.color:
                            self.x += self.square_height
                        else:
                            self.attacked_pieces.append(other_piece)
                    self.piece_y = self.y
                if ((keys[pygame.K_RCTRL] and keys[pygame.K_1]) or (keys[pygame.K_RCTRL] and keys[pygame.K_KP1])) and not ((keys[pygame.K_RCTRL] and keys[pygame.K_1]) and (keys[pygame.K_RCTRL] and keys[pygame.K_KP1])):
                    self.x += self.square_width
                    self.y -= self.square_height
                    if self.x == other_piece.piece_x and self.y == other_piece.piece_y:
                        if self.color == other_piece.color:
                            self.x -= self.square_width
                            self.y += self.square_height
                        else:
                            self.attacked_pieces.append(other_piece)
                        self.piece_x, self.piece_y = self.x, self.y
                while direction <= max_direction:
                    if direction == 0:
                        while self.y <= win_height-self.square_height and self.x >= 0:
                            self.x -= self.square_width
                            self.y += self.square_height
                            if not (self.y == other_piece.piece_y and self.x == other_piece.piece_x):
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
                    elif direction == 1:
                        while self.y <= self.win_height-self.square_height:
                            self.y -= self.square_height
                            if not (self.x == other_piece.piece_x and self.y == other_piece.piece_y):
                                self.attacked_pieces.append(
                                    ((self.x, self.y),))
                                continue
                        else:
                            self.y += self.square_height
                            if other.color != self.color:
                                self.attacked_pieces.append(other_piece) if not other_piece in self.attacked_pieces
                                break
                    elif direction == 2:
                        while self.x <= win_width-self.square_width and self.y <= self.win_height-self.square_height:
                            self.x += self.square_width
                            self.y += self.square_height
                            if not (self.x == other_piece.piece_x and self.y == other_piece.piece_y):
                                self.attacked_pieces.append(
                                    ((self.x, self.y),))
                                continue
                            else:
                                self.x -= self.square_width
                                self.y -= self.square_height
                                if other.color != self.color:
                                    self.attacked_pieces.append(
                                        (other_piece, (self.x, self.y)))
                                    self.y -= self.square_height
                    elif direction == 3:
                        while self.x >= 0:
                            self.x -= self.square_width
                            if not (self.x == other_piece.piece_x and self.y == other_piece.piece_y):
                                self.attacked_pieces.append(
                                    ((self.x, self.y),))
                                continue
                        else:
                            self.x += self.square_width
                            if other.color != self.color:
                                self.attacked_pieces.append(
                                    (other_piece, (self.x, self.y)))
                                break
                    elif direction == 4:
                        self.x += self.square_width
                        if not (self.x == other_piece.piece_x and self.y == other_piece.piece_y):
                            self.attacked_pieces.append(((self.x, self.y),))
                            continue
                        else:
                            self.x -= self.square_width
                            if self.color != other_piece.color:
                                self.attacked_pieces.append(
                                    (other_piece, (self.x, self.y)))
                                break
                    elif direction == 5:
                        self.x -= self.square_width
                        self.y -= self.square_height
                        if not (self.x == other_piece.piece_x self.y == other_piece.piece_y):
                            self.attacked_pieces.append(((self.x, self.y),))
                            continue
                        else:
                            self.x += self.square_width
                            self.y += self.square_height
                            if self.color != other_piece.color:
                                self.attacked_pieces.append(
                                    (other_piece, (self.x, self.y)))
                                break
                    elif direction == 6:
                        while self.y >= 0:
                            self.y -= self.square_height
                            if not (self.x == other_piece.piece_x and self.y == other_piece.piece_y):
                                self.attacked_pieces.append(((self.x, self.y)))
                                continue
                            else:
                                self.y += self.square_height
                                if self.color != other_piece.color:
                                    self.attacked_pieces.append(
                                        (other_piece, (self.x, self.y)))
                                    self.y += self.square_height
                                    break
                    elif direction == 7:
                        self.x += self.square_width
                        self.y -= self.square_height
                        if not (self.x == other_piece.piece_x and self.y == other_piece.piece_y):
                            self.attacked_pieces.append(((self.x, self.y),))
                            continue
                        else:
                            if self.color != other_piece.color:
                                self.attacked_pieces.append(
                                    (other_pieces, (self.x, self.y)))
                                break
                    direction += 1
        self.x, self.y = self.piece_x, self.piece_y
        return self.attacked_pieces, (self.piece_x, self.piece_y), pieces
