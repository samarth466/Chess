import pygame
from pygame import key
from .piece import Piece, Rook
from ..board_utils.square import Square
from ..chess.CONSTANTS import WHITE, BLACK


class King(Piece):

    def __init__(self, image, file, rank, color, min_x, max_x, min_y, max_y, square_width, square_height, win_width, win_height):
        pygame.init()       # initialize pygame
        self.image = image      # location of the image representation of piece
        # loads the image for piece into pygame
        self.image_surface = pygame.image.load(image)
        self.rank = rank       # rank of piece as represented in a chess game
        self.file = file      # file of piece as represented in a chess game
        self.color = color      # color of the piece (black or white)
        self.name = 'King'      # name of this piece
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
        self.has_moved = False
        super().__init__(self.image, self.file, self.rank, self.name, self.color)

    def move(self, squares: dict, win: pygame.Surface, matterial: dict) -> tuple:
        # we need to loop through squares and keep track of the position of the piece, so we must make sure that squares is a dict as we need to associate the position with a Square instance
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
            if ((keys[pygame.K_LCTRL] and keys[pygame.K_1]) or (keys[pygame.K_LCTRL] and keys[pygame.K_KP_1])) and not ((keys[pygame.K_LCTRL] and keys[pygame.K_1]) and (keys[pygame.K_LCTRL] and keys[pygame.K_KP_1])):
                self.x -= self.square_width
                self.y += self.square_height
                if self.x == other_piece.piece_x and self.y == other_piece.piece_y:
                    if self.color == other_piece.color:
                        self.x += self.square_width
                        self.y -= self.square_height
                    else:
                        self.attacked_pieces.append(other_piece)
                    if self.check(matterial):
                        if self.attacked_pieces[other_piece]:
                            self.attacked_pieces.pop(
                                self.attacked_pieces.index(other_piece))
                        self.x += self.square_width
                        self.y -= self.square_height
                self.piece_x, self.piece_y = self.x, self.y
                self.has_moved = True
            if ((keys[pygame.K_LCTRL] and keys[pygame.K_2]) or (keys[pygame.K_LCTRL] and keys[pygame.K_KP_2])) and not ((keys[pygame.K_LCTRL] and keys[pygame.K_2]) and (keys[pygame.K_LCTRL] and keys[pygame.K_LCTRL] and keys[pygame.K_KP_2])):
                self.y += self.square_height
                if self.y == other.piece_y and self.x == other.piece_x:
                    if self.color == other_piece.color:
                        self.y -= self.square_height
                    else:
                        self.attacked_pieces.append(other_piece)
                    if self.check(matterial):
                        if self.attacked_pieces[other_piece]:
                            self.attacked_pieces.pop(
                                self.attacked_pieces.index(other_piece))
                        self.y -= self.square_height
                self.piece_y = self.y
                self.has_moved = True
            if ((keys[pygame.K_LCTRL] and keys[pygame.K_3]) or (keys[pygame.K_LCTRL] and keys[pygame.K_KP_3])) and not ((keys[pygame.K_LCTRL] and keys[pygame.K_3]) and (keys[pygame.K_LCTRL] and keys[pygame.K_KP_3])):
                self.x += self.square_width
                self.y += self.square_height
                if self.x == other_piece.piece_x and self.y == other_piece.piece_y:
                    if self.color == other_piece.color:
                        self.x -= self.square_width
                        self.y -= self.square_height
                    else:
                        self.attacked_pieces.append(other_piece)
                    if self.check(matterial):
                        if self.attacked_pieces[other_piece]:
                            self.attacked_pieces.pop(
                                self.attacked_pieces.index(other_piece))
                        self.x -= self.square_width
                        self.y -= self.square_height
                self.piece_x, self.piece_y = self.x, self.y
                self.has_moved = True
            if ((keys[pygame.K_LCTRL] and keys[pygame.K_KP_4]) or (keys[pygame.K_LCTRL] and keys[pygame.K_4])) and not ((keys[pygame.K_LCTRL] and keys[pygame.K_4]) and (keys[pygame.K_LCTRL] and keys[pygame.K_KP_4])):
                self.x -= self.square_width
                if self.x == other.piece_x and self.y == other.piece_y:
                    if self.color == other_piece.color:
                        self.x += self.square_width
                    else:
                        self.attacked_pieces.append(other_pieces)
                    if self.check(matterial):
                        if self.attacked_pieces[other_piece]:
                            self.attacked_pieces.pop(
                                self.attacked_pieces.index(other_piece))
                        self.x += self.square_width
                self.piece_x = self.x
                self.has_moved = True
            if ((keys[pygame.K_LCTRL] and keys[pygame.K_6]) or (keys[pygame.K_LCTRL] and keys[pygame.K_KP_6])) and not ((keys[pygame.K_LCTRL] and keys[pygame.K_6]) and (keys[pygame.K_LCTRL] and keys[pygame.K_KP_6])):
                self.x += self.square_width
                if self.x == other.piece_x and self.y == other.piece_y:
                    if self.color == other_piece.color:
                        self.x -= self.square_width
                    else:
                        self.attacked_pieces.append(other_piece)
                    if self.check(matterial):
                        if self.attacked_pieces[other_piece]:
                            self.attacked_pieces.pop(
                                self.attacked_pieces.index(other_piece))
                        self.x -= self.square_width
                self.piece_x = self.x
                self.has_moved = True
            if ((keys[pygame.K_LCTRL] and keys[pygame.K_7]) or (keys[pygame.K_LCTRL] and keys[pygame.K_KP_7])) and not ((keys[pygame.K_LCTRL] and keys[pygame.K_7]) and (keys[pygame.K_LCTRL] and keys[pygame.K_KP_7])):
                self.x -= self.square_width
                self.y -= self.square_height
                if self.x == other_piece.piece_x and self.y == other_piece.piece_y:
                    if self.color == other_piece.color:
                        self.x += self.square_width
                        self.y += self.square_height
                    else:
                        self.attacked_pieces.append(other_piece)
                    if self.check(matterial):
                        if self.attacked_pieces[other_piece]:
                            self.attacked_pieces.pop(
                                self.attacked_pieces.index(other_piece))
                        self.x += self.square_width
                        self.y += self.square_height
                self.piece_x, self.piece_y = self.x, self.y
                self.has_moved = True
            if ((keys[pygame.K_LCTRL] and keys[pygame.K_KP_8]) or (keys[pygame.K_LCTRL] and keys[pygame.K_8])) and not ((keys[pygame.K_LCTRL] and keys[pygame.K_8]) and (keys[pygame.K_LCTRL] and keys[pygame.K_KP_8])):
                self.y -= self.square_height
                if self.y == other.piece_y and self.x == other.piece_x:
                    if self.color == other_piece.color:
                        self.x += self.square_height
                    else:
                        self.attacked_pieces.append(other_piece)
                    if self.check(matterial):
                        if self.attacked_pieces[other_piece]:
                            self.attacked_pieces.pop(
                                self.attacked_pieces.index(other_piece))
                        self.y += self.square_height
                self.piece_y = self.y
                self.has_moved = True
            if ((keys[pygame.K_LCTRL] and keys[pygame.K_9]) or (keys[pygame.K_LCTRL] and keys[pygame.K_KP_9])) and not ((keys[pygame.K_LCTRL] and keys[pygame.K_9]) and (keys[pygame.K_LCTRL] and keys[pygame.K_KP_9])):
                self.x += self.square_width
                self.y -= self.square_height
                if self.x == other_piece.piece_x and self.y == other_piece.piece_y:
                    if self.color == other_piece.color:
                        self.x -= self.square_width
                        self.y += self.square_height
                    else:
                        self.attacked_pieces.append(other_piece)
                    if self.check(matterial):
                        if self.attacked_pieces[other_piece]:
                            self.attacked_pieces.pop(
                                self.attacked_pieces.index(other_piece))
                        self.x -= self.square_width
                        self.y -= self.square_height
                self.piece_x, self.piece_y = self.x, self.y
                self.has_moved = True
            if keys[pygame.K_c]:
                if self.color == WHITE:
                    self.castle(squares, matterial, True,
                                matterial['WHITE']['Rook'][1])
                elif self.color == BLACK:
                    self.castle(squares, matterial, True,
                                matterial['BLACK']['Rook'][1])
            if ((keys[pygame.K_LSHIFT] and keys[pygame.K_c]) or (keys[pygame.K_RSHIFT] and keys[pygame.K_c])) and not ((keys[pygame.K_LSHIFT] and keys[pygame.K_c]) and (keys[pygame.K_RSHIFT] and keys[pygame.K_c])):
                if self.color == WHITE:
                    self.castle(squares, matterial, False,
                                matterial['WHITE']['Rook'][0])
                elif self.color == BLACK:
                    self.castle(squares, matterial, False,
                                matterial['BLACK'][0])
            while direction <= max_direction:
                if direction == 0:
                    self.x -= self.square_width
                    self.y += self.square_height
                    if not (self.y == other_piece.piece_y and self.x == other_piece.piece_x):
                        self.attacked_pieces.append(((self.x, self.y),))
                    else:
                        self.x += self.square_width
                        self.y -= self.square_height
                        if other.color != self.color:
                            self.attacked_pieces.append(
                                ((self.x, self.y), other_piece))
                elif direction == 1:
                    self.y -= self.square_height
                    if not (self.x == other_piece.piece_x and self.y == other_piece.piece_y):
                        self.attacked_pieces.append(((self.x, self.y),))
                    else:
                        self.y += self.square_height
                        if other.color != self.color:
                            self.attacked_pieces.append(
                                ((self.x, self.y), other_piece))
                elif direction == 2:
                    self.x += self.square_width
                    self.y += self.square_height
                    if not (self.x == other_piece.piece_x and self.y == other_piece.piece_y):
                        self.attacked_pieces.append(((self.x, self.y),))
                    else:
                        self.x -= self.square_width
                        self.y -= self.square_height
                        if other.color != self.color:
                            self.attacked_pieces.append(
                                ((self.x, self.y), other_piece))
                elif direction == 3:
                    self.x -= self.square_width
                    if not (self.x == other_piece.piece_x and self.y == other_piece.piece_y):
                        self.attacked_pieces.append(((self.x, self.y),))
                    else:
                        self.x += self.square_width
                        if other.color != self.color:
                            self.attacked_pieces.append(
                                ((self.x, self.y), other_piece))
                elif direction == 4:
                    self.x += self.square_width
                    if not (self.x == other_piece.piece_x and self.y == other_piece.piece_y):
                        self.attacked_pieces.append(((self.x, self.y),))
                    else:
                        self.x -= self.square_width
                        if self.color != other_piece.color:
                            self.attacked_pieces.append(
                                ((self.x, self.y), other_piece))
                elif direction == 5:
                    self.x -= self.square_width
                    self.y -= self.square_height
                    if not (self.x == other_piece.piece_x and self.y == other_piece.piece_y):
                        self.attacked_pieces.append(((self.x, self.y),))
                    else:
                        self.x += self.square_width
                        self.y += self.square_height
                        if self.color != other_piece.color:
                            self.attacked_pieces.append(
                                ((self.x, self.y), other_piece))
                elif direction == 6:
                    self.y -= self.square_height
                    if not (self.x == other_piece.piece_x and self.y == other_piece.piece_y):
                        self.attacked_pieces.append(((self.x, self.y),))
                    else:
                        self.y += self.square_height
                        if self.color != other_piece.color:
                            self.attacked_pieces.append(
                                ((self.x, self.y), other_piece))
                elif direction == 7:
                    self.x += self.square_width
                    self.y -= self.square_height
                    if not (self.x == other_piece.piece_x and self.y == other_piece.piece_y):
                        self.attacked_pieces.append(((self.x, self.y),))
                    else:
                        if self.color != other_piece.color:
                            self.attacked_pieces.append(
                                ((self.x, self.y), other_pieces))
                direction += 1
        self.x, self.y = self.piece_x, self.piece_y
        return (self.attacked_pieces, (self.piece_x, self.piece_y), pieces)

    def check(self, pieces: list[Piece], position: tuple[str, int] = tuple(), squares: dict[str, Square] = dict()) -> bool:
        if position and squares:
            if squares[position[0]+str(position[1])].attacked:
                return True
            return False
        else:
            for piece in pieces:
                if Self.attackers or ((Self.x, self.y), Self) in piece.attacked_pieces():
                    return True
            return False

    def get_possible_positions_from_current_position(self, position: tuple[int, int], squares: [str, Square]) -> list:
        file, rank = position
        prev_rank = rank-1 if rank > 1 else None
        next_rank = rank+1 if rank < 8 else None
        prev_file = self.possible_files[self.possible_files.index(
            file)-1] if file != self.possible_files[0] else None
        next_file = self.possible_files[self.possible_files.index(
            file)+1] if self.possible_files[-1] else None
        return list(filter(lambda i: squares[i[0]+str(i[1])].piece.color != self.color and all(i), [(prev_file, prev_rank), (file, prev_rank), (prev_file, rank), (file, rank), (next_file, rank), (prev_file, next_rank), (file, next_rank), (next_file, next_rank)]
    
    def     checkmate(self):
        if self.check(pieces):
            possible_positions=self.get_possible_positions_from_current_position(
                (self.file, self.rank))
            filtered_possible_positions=list(
                filter(lambda i: self.check(pieces, i, squares), possible_positions))
            if possible_positions.length() == filtered_possible_positions:
                return True
            return False
        return False

    def castle(self, rook: Rook, squares: dict[str, Square], normal: bool, matterial: dict[str, Any]) -> bool:
        if self.color == WHITE:
            if normal:
                if squares['F1'].empty() and squares['G1'].empty():
                    if not (self.check(matterial, ('F', 1), squares) and self.check(matterial, ('G', 1), squares)):
                        if not (self.has_moved and rook.has_moved):
                            self.file='G'
                            rook.file='F'
            else:
                if squares['B1'].empty() and squares['C1'].empty() and squares['D1'].empty():
                    if not (self.check(matterial, ('B', 1), squares) and self.check(matterial, ('C', 1), squares) and self.check(matterial, ('D', 1), squares)):
                        if not (self.has_moved and rook.has_moved):
                            self.file='B'
                            rook.file='C'
        if self.color == BLACK:
            if normal:
                if squares['F8'].empty() and squares['G8'].empty():
                    if not (self.check(matterial, ('F', 8), squares) and self.check(matterial, ('G', 8), squares)):
                        if not (self.has_moved and rook.has_moved):
                            self.file='G'
                            rook.file='F'
            else:
                if squares['B8'].empty() and squares['C8'].empty() and squares['D8'].empty():
                    if not (self.check(matterial, ('B', 8), squares) and self.check(matterial, ('C', 8), squares) and self.check(matterial, ('D', 8), squares)):
                        if not (self.has_moved and rook.has_moved):
                            self.file='B'
                            rook.file='C'
