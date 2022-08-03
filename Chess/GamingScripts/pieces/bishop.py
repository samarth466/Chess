import pygame
from utils.functions import get_game_pos, get_window_pos
from utils.types import WindowPosition
from .piece import Piece


class Bishop(Piece):

    def __init__(self, image: str, file: str, rank: int, color: pygame.Color, min_x: int, max_x: int, min_y: int, max_y: int, square_width: int, square_height: int, win_width: int, win_height: int) -> None:
        pygame.init()
        super().__init__(image, file, rank, 'Bishop', color)
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.square_width = square_width
        self.square_height = square_height
        self.win_width = win_width
        self.win_height = win_height
        self.x, self.y = self.piece_x, self.piece_y = get_window_pos(
            self.file, self.rank, self.possible_files)
        self.attacked_pieces = []

    def move(self, win: pygame.Surface, squares: dict) -> tuple[list[Piece], WindowPosition, WindowPosition, Piece]:
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
        original_x, original_y = self.x, self.y
        pygame.font.init()
        for other in squares.values():
            if (other.file, other.rank) == (self.file, self.rank):
                continue
            other_piece = other.piece
            while (self.x in limiting_pos[0] and self.y in limiting_pos[1]):
                if len(pieces) > max_length:
                    fnt = pygame.font.SysFont("comicsans", 40)
                    txt = fnt.render(
                        "You can't select that piece because you have already selected a piece. You must either move the already selected piece or unselect it.")
                    win.blit(txt, (self.max_x-(txt.get_width/2) /
                                   2, self.max_y-(txt.get_height()/2)/2))
                self.x, self.y = self.get_window_pos()
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
                    if self.y == other_piece.piece_y and self.x == other_piece.piece_x:
                        if other_piece.color == self.color:
                            self.x += self.square_width
                            self.y -= self.square_height
                            self.attacked_pieces.append((other_piece.x,other_piece.y))
                    self.piece_x = self.x
                    self.piece_y = self.y
                if (keys[pygame.K_KP3] or keys[pygame.K_3]) and not (keys[pygame.K_3] and keys[pygame.K_KP3]):
                    self.x -= self.square_width
                    self.y -= self.square_height
                    if self.x == other_piece.piece_x and self.y == other_piece.piece_y:
                        if other_piece.color == self.color:
                            self.x += self.square_width
                            self.y += self.square_width
                            self.attacked_pieces.append((other_piece.x,other_piece.y))
                    self.piece_x = self.x
                    self.piece_y = self.y
                if (keys[pygame.K_KP7] or keys[pygame.K_7]) and not (keys[pygame.K_KP7] and keys[pygame.K_7]):
                    self.x -= self.square_width
                    self.y -= self.square_height
                    if self.x == other_piece.piece_x and self.y == other_piece.piece_y:
                        if other_piece.color == self.color:
                            self.x += self.square_width
                            self.y += self.square_height
                            self.attacked_pieces.append((other_piece.x,other_piece.y))
                    self.piece_x = self.x
                    self.piece_y = self.y
                if (keys[pygame.K_KP9] or keys[pygame.K_9]) and not (keys[pygame.K_KP9] and keys[pygame.K_9]):
                    self.x += self.SQUARE_width
                    self.y -= self.square_height
                    if self.y == other_piece.piece_y and self.x == other_piece.piece_x:
                        if other_piece.color == self.color:
                            self.x -= self.square_width
                            self.y += self.square_height
                            self.attacked_pieces.append((other_piece.x,other_piece.y))
                    self.piece_x = self.x
                    self.piece_y = self.y
                while direction < max_direction:
                    if direction == 0:
                        while self.x >= 0 and self.y <= win_height-self.square_height:
                            self.x -= self.square_width
                            self.y += self.square_height
                            self.attacked_pieces.append((self.x,self.y))
                            if self.y == other_piece.piece_y and self.x == other_piece.piece_x:
                                break
                    if direction == 1:
                        while self.x <= self.win_width-self.square_width and self.y <= self.win_height-square_height:
                            self.x += self.square_width
                            self.y += self.square_height
                            self.attacked_pieces.append((self.x,self.y))
                            if self.x == other_piece.piece_x and self.y == other_piece.piece_y:
                                break
                    if direction == 2:
                        while self.x >= 0 and self.y >= 0:
                            self.x -= self.square_width
                            self.y -= self.square_height
                            self.attacked_pieces.append((self.x,self.y))
                            if self.x == other_piece.piece_x and self.x == other_piece.piece_y:
                                break
                    if direction == 3:
                        while self.x <= self.win_width-self.square_width and self.y >= 0:
                            self.x += self.square_width
                            self.y -= self.square_height
                            self.attacked_pieces.append((self.x,self.y))
                            if self.x == other_piece.piece_x and self.y == other_piece.piece_y:
                                break
                    direction += 1
                direction = 0
        self.x, self.y = self.piece_x, self.piece_y
        self.file, self.rank = get_game_pos(
            self.x, self.y, self.possible_files)
        return self.attacked_pieces, (self.piece_x, self.piece_y), (original_x, original_y), self