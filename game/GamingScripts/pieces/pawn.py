import pygame
from .piece import Piece
from . import Bishop, Knight, Queen, Rook
from ..chess.CONSTANTS import WHITE, BLACK
from ..board_utils.square import Square
from game.GamingScripts.board_utils import square


class Pawn(Piece):

    def __init__(self, image, file, rank, color, min_x, max_x, min_y, max_y, square_width, square_height, win_width, win_height):
        pygame.init()
        self.image = image
        self.image_surface = pygame.image.load(image)
        self.file = file
        self.rank = rank
        self.color = color
        self.name = 'Pawn'
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.square_width = square_width
        self.square_height = square_height
        self.win_width = win_width
        self.win_height = win_height
        self.x, self.y = self.piece_x, self.piece_y
        self.attacked_pieces = []
        self.double_moved_on_first_turn = False
        super().__init__(self.image, self.file, self.rank, self.name, self.color)

    def move(self, squares: dict, win: pygame.Surface, multiplier: int):
        if not isinstance(squares, dict):
            raise TypeError('The squares attribute must be a dict.')
        if self.square_height != self.square_width:
            raise TypeError(
                'The height and width of the square must be the same.')
        if multiplier != 1 or multiplier != -1:
            raise TypeError("The 'multiplier' parameter must be 1 or -1")
        limiting_pos = [[self.min_x, self.max_x], [self.min_y, self.max_y]]
        pieces = []
        max_length = 1
        selected = False
        direction = 0
        max_direction = 3
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
                for event in pygame.event.get():
                    if event.type == pygame.K_SPACE or event.type == pygame.K_KP5:
                        if (self.x, self.y, self.name) in pieces:
                            selected = False
                            pieces.pop()
                        else:
                            selected = True
                            pieces.append((self.x, self.y, self.name))
            keys = pygame.key.get_pressed()
            if ((keys[pygame.K_LSHIFT] and keys[pygame.K_7]) or (keys[pygame.K_RSHIFT] and keys[pygame.K_7]) or (keys[pygame.K_LSHIFT] and keys[pygame.K_KP_7]) or (keys[pygame.K_RSHIFT] and keys[pygame.K_KP_7])) and not ((keys[pygame.K_LSHIFT] and keys[pygame.K_7]) and (keys[pygame.K_RSHIFT] and keys[pygame.K_7]) and (keys[pygame.K_LSHIFT] and keys[pygame.K_KP_7]) and (keys[pygame.K_RSHIFT] and keys[pygame.K_KP_7])):
                self.x -= self.square_width
                self.y += multiplier*self.square_height
                file, rank = self.get_game_pos()
                if squares[file+str(rank)].piece and squares[file+str(rank)].piece.color != self.color:
                    self.attacked_pieces.append(squares[file+str(rank)])
                else:
                    self.x += self.square_width
                    self.y -= multiplier*self.square_height
                self.file, self.rank = file, rank
            if ((keys[pygame.K_LSHIFT] and keys[pygame.K_8]) or (keys[pygame.K_RSHIFT] and keys[pygame.K_8]) or (keys[pygame.K_LSHIFT] and keys[pygame.K_KP_8]) or (keys[pygame.K_RSHIFT] and keys[pygame.K_KP_8])) and not ((keys[pygame.K_LSHIFT] and keys[pygame.K_8]) and (keys[pygame.K_RSHIFT] and keys[pygame.K_8]) and (keys[pygame.K_LSHIFT] and keys[pygame.K_KP_8]) and (keys[pygame.K_RSHIFT] and keys[pygame.K_KP_8])):
                self.y += multiplier*self.square_height
                file, rank = self.get_game_pos()
                if squares[file+str(rank)].piece:
                    self.y -= multiplier*self.square_height
                self.file, self.rank = file, rank
            if ((keys[pygame.K_LSHIFT] and keys[pygame.K_9]) or (keys[pygame.K_RSHIFT] and keys[pygame.K_9]) or (keys[pygame.K_LSHIFT] and keys[pygame.K_KP_9]) or (keys[pygame.K_RSHIFT] and keys[pygame.K_KP_9])) and not ((keys[pygame.K_LSHIFT] and keys[pygame.K_9]) and (keys[pygame.K_RSHIFT] and keys[pygame.K_9]) and (keys[pygame.K_LSHIFT] and keys[pygame.K_KP_9]) and (keys[pygame.K_RSHIFT] and keys[pygame.K_KP_9])):
                self.x += self.square_width
                self.y += multiplier*self.square_height
                file, rank = self.get_game_pos()
                if squares[file+str(rank)].piece and squares[file+str(rank)].piece.color != self.color:
                    self.attacked_pieces.append(squares[file+str(rank)])
                else:
                    self.x -= self.square_width
                    self.y -= multiplier*self.square_height
                self.file, self.rank = file, rank
            if keys[pygame.K_d]:
                rank, file = self.get_game_pos()
                self.move_forward_twice(rank, file, multiplier, squares)
                if self.color == WHITE and self.x/self.square_width+1 == 2:
                    self.y += multiplier * self.square_height * 2
                    file, rank = self.get_game_pos()
                    if squares[file+str(rank)].piece:
                        self.y -= multiplier * self.square_height * 2
                if self.color == BLACK and self.x/self.square_width == 7:
                    self.y += multiplier * self.square_height * 2
                    file, rank = self.get_game_pos()
                    if squares[file+str(rank)].piece:
                        self.y -= multiplier * self.square_height * 2
                self.file, self.rank = file, rank
                self.double_moved_on_first_turn = True
            if keys[pygame.K_e]:
                self.en_passante(squares)
            while direction < max_direction:
                if direction == 0:
                    self.x -= self.square_width
                    self.y += multiplier * self.square_height
                    file, rank = self.get_game_pos()
                    if not squares[file+str(rank)].piece:
                        self.attacked_pieces.append(((self.x, self.y),))
                    else:
                        self.x += self.square_width
                        self.y -= multiplier*self.square_height
                        file, rank = self.get_game_pos()
                        if squares[file+str(rank)].piece.color != self.color:
                            self.attacked_pieces(
                                ((self.x, self.y), squares[file+str(rank)].piece))
                elif direction == 1:
                    self.y += multiplier * self.square_height
                    file, rank = self.get_game_pos()
                    if not squares[file+str(rank)].piece:
                        self.attacked_pieces.append(((self.x, self.y),))
                    else:
                        self.y -= multiplier*self.square_height
                        file, rank = self.get_game_pos()
                        if squares[file+str(rank)].piece.color != self.color:
                            self.attacked_pieces(
                                ((self.x, self.y), squares[file+str(rank)].piece))
                elif direction == 2:
                    self.x += self.square_width
                    self.y += multiplier * self.square_height
                    file, rank = self.get_game_pos()
                    if not squares[file+str(rank)].piece:
                        self.attacked_pieces.append(((self.x, self.y),))
                    else:
                        self.x -= self.square_width
                        self.y -= multiplier*self.square_height
                        file, rank = self.get_game_pos()
                        if squares[file+str(rank)].piece.color != self.color:
                            self.attacked_pieces(
                                ((self.x, self.y), squares[file+str(rank)].piece))
                direction += 1
        self.x, self.y = self.piece_x, self.piece_y
        return self.attacked_pieces, (self.piece_x, self.piece_y), pieces

    def move_forward_twice(rank: int, file: str, squares: dict[str, Square]) -> tuple[in , int]:
        if Self.color == WHITE and rank == 2:
            rank += 2
            if squares[file+str(rank)].piece:
                rank -= 2
        elif self.color == BLACK and rank == 7:
            rank += 2
            if squares[file+str(rank)].piece:
                rank -= 2
        return self.get_window_pos(file, rank)

    def promotion(self, promoted_piece: str, images: dict[tuple[int, int, int], dict[str, str]]) -> self.__class__:
        promoted_pieces = [Rook, Knight, Bishop, Queen]
        if promoted_piece in promoted_pieces:
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