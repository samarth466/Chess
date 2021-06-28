import pygame
from pygame_gui.elements import ui_text_entry_line
from game.GamingScripts.pieces.piece import Piece
from game.GamingScripts.chess.CONSTANTS import (WHITE, BLACK, RED, MANAGER)


class Pawn(Piece):

    def __init__(self, image, file, rank, color, min_x, max_x, min_y, max_y, square_width, square_height, win_width, win_height):
        pygame.init()
        self.image = image
        self.image_surface = pygame.image.load(image)
        self.rank = rank
        self.file = file
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
        self.piece_x, self.piece_y = pygame.mouse.get_cursor()
        self.x, self.y = self.piece_x, self.piece_y
        self.attacked_pieces = []
        self.has_moved = False
        super().__init__(self.image, self.file, self.rank, self.name, self.color)

    def _move(self, x, y, delta_x, delta_y, squares, self_color, board, skip_step):
        if delta_y == 0:
            raise ValueError('The delta_y cannot be 0.')
        xValues = [x for x in filter(function=lambda i: False if i.piece_x == x else True, squares)]:
        yValues = [y for y in filter(function=lambda i: False if i.piece_y == y else True, squares)]
        colors = []
        for square in squares:
            colors.append(square.color)
        if x+delta_x in xValues and y+delta_y in yValues and delta_x != 0:
            if {k: v for (k, v) in zip(zip(xValues, yValues), colors)}[(x, y)] != self_color:
                board.remove_piece(x, y)
                x += delta_x
                y += delta_y
        elif not x+delta_x in xValues and not y+delta_y in yValues and delta_x == 0 and self.has_moved:
                y += delta_y
            elif not x+delta_x in xValues and not y+yValues in yValues and delta_x == 0 and not self.has_moved and skip_step:
                for _ in range(2):
                    y += delta_x
        return (x,y)
    
    def _update_attacked_pieces(self,x,y,delta_x,delta_y,square_width,square_height,squares,self_color):
        temp_x = x
        temp_y = y
        attacked_pieces = []
        xValues = [x for x in filter(function=lambda i: True if i.x == x or i.x == x+delta_x or i.x == x-delta_x else False, squares)]
        yValues = [y for y in filter(function=lambda i: False if i.y == y or i.y == y+delta_y else False, squares)]
        colors = []
        for square in squares:
            colors.append(square.color)
        coordinates = zip(xValues, yValues, colors)
        for other_x,other_y,color in coordinates:
            if x == other_x and y == other_y:
                if self_color != color:
                    attacked_pieces.append((x,y))
                    x = temp_x
                    y = temp_y
        return attacked_pieces
    
    def move(self,win,squares,board):
        if not isinstance(squares,list):
            raise TypeError('The squares arguement must be of type list(), not '+str(type(squares))[8:-1].capitalize()+'().')
        limiting_pos = [[self.min_x,self.max_x],[self.min_y,self.max_y]]
        pieces = []
        max_length = 1
        selected = False
        direction = 0
        max_direction = 2
        direction_offset = 0
        pygame.font.init()
        while (self.x in limiting_pos[0] and self.y in limiting_pos[1]):
            if len(pieces) > max_length:
                fnt = pygame.font.SysFont("comicsans",40)
                txt = fnt.render("You cannot move that piece, because you have already selected a piece. You must move the already selected piece or move it.",1,RED)
                win.blit(txt,(self.get_window_pos()[0],self.get_window_pos()[1]))
            self.file,self.rank = self.get_game_pos()
            for event in pygame.event.get():
                if event.type == pygame.K_SPACE or event.type == pygame.K_RETURN:
                    if (self.x,self.y,self.name) in pieces:
                        selected = False
                        pieces.pop()
                    else:
                        selected = True
                        pieces.append((self.x,self.y,self.name))
            keys = pygame.key.get_pressed()
            if ((keys[pygame.K_RALT] and keys[K_KP7]) or (keys[pygame.K_LALT] and keys[pygame.K_KP7]) or (keys[pygame.K_RALT] and keys[pygame.K_7]) or (keys[pygame.K_LALT] and keys[pygame.K_7])) and not ((keys[pygame.K_RALT] and keys[K_KP7]) and (keys[pygame.K_LALT] and keys[pygame.K_KP7]) and (keys[pygame.K_RALT] and keys[pygame.K_7]) and (keys[pygame.K_LALT] and keys[pygame.K_7])):
                self.x,self.y = self._move(self.x,self.y,-self.square_width,-self.square_height,squares,self.color,board,False)
                self.piece_x = self.x
                self.piece_y = self.y
                self.has_moved = True
            if ((keys[pygame.K_RALT] and keys[K_KP8]) or (keys[pygame.K_LALT] and keys[pygame.K_KP8]) or (keys[pygame.K_RALT] and keys[pygame.K_8]) or (keys[pygame.K_LALT] and keys[pygame.K_8])) and not ((keys[pygame.K_RALT] and keys[K_KP8]) and (keys[pygame.K_LALT] and keys[pygame.K_KP8]) and (keys[pygame.K_RALT] and keys[pygame.K_8]) and (keys[pygame.K_LALT] and keys[pygame.K_8])):
                text_input_line = ui_text_entry_line(relative_rect=pygame.Rect(self.x,self.x,self.square_width,self.square_height),manager=MANAGER)
                text_input_line.enable()
                text_input_line.set_allowed_characters([1,2])
                text_input_line.set_text_length_limit(1)
                text = text_input_line.get_text()
                if text == '1':
                    self.x,self.y = self._move(self.x,self.y,0,-self.square_height,squares,self.color,board,False)
                elif text == '2':
                    self.x,self.y = self._move(self.x,self.y,0,-self.square_height,squares,self.color,board,True)
                self.piece_x = self.x
                self.piece_y = self.y
                self.has_moved = True
            if ((keys[pygame.K_RALT] and keys[K_KP9]) or (keys[pygame.K_LALT] and keys[pygame.K_KP9]) or (keys[pygame.K_RALT] and keys[pygame.K_9]) or (keys[pygame.K_LALT] and keys[pygame.K_9])) and not ((keys[pygame.K_RALT] and keys[K_KP9]) and (keys[pygame.K_LALT] and keys[pygame.K_KP9]) and (keys[pygame.K_RALT] and keys[pygame.K_9]) and (keys[pygame.K_LALT] and keys[pygame.K_9])):
                self.x,self.y = self._move(self.x,self.y,self.square_width,-self.square_height,squares,self.color,board,False)
                self.piece_x = self.x
                self.piece_y = self.y
                self.has_moved = True
            while direction < max_direction:
                if direction == 0:
                        self.attacked_pieces = self._update_attacked_pieces(self.x,self.y,-self.square_width,-self.square_height,self.square_width,self.square_height,squares,self.color)
                    if direction == 1:
                        self.attacked_pieces = self._update_attacked_pieces(self.x,self.y,self.square_width,-self.square_height,self.square_width,self.square_height,squares,self.color)
