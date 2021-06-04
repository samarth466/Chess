import pygame
from game.gaming_scripts.pieces.piece import Piece

class Rook(Piece):

    def __init__(self,image,file,rank,color,min_x,max_x,min_y,max_y,square_width,square_height,win_width,win_height):
        pygame.init()
        self.image = image
        self.image_surface = pygame.image.load(image)
        self.rank = rank
        self.file = file
        self.color = color
        self.name = 'Rook'
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.square_width = square_width
        self.square_height = square_height
        self.win_width = win_width
        self.win_height = win_height
        self.x,self.y = self.piece_x,self.piece_y
        self.attacked_pieces = []
        super().__init__(self.image,self.file,self.rank,self.name,self.color)
    
    def move(self,squares,win):
        if not isinstance(squares,list):
            raise TypeError('The squares attribute must be a list.')
        if self.square_height != self.square_width:
            raise TypeError('The height and width of the square must be the same.')
        limiting_pos = [[self.min_x,self.max_x],[self.min_y,self.max_y]]
        pieces = []
        max_length = 1
        selected = False
        direction = 0
        max_direction = 4
        pygame.font.init()
        for other in squares:
            while (self.x in limiting_pos[0] and self.y in limiting_pos[1]):
                if len(pieces) > max_length:
                    fnt = pygame.font.SysFont("comicsans",40)
                    txt = fnt.render("You can't select that piece because you have already selected a piece. You must either move the already selected piece or unselect it.")
                    win.blit(txt,(self.max_x-(txt.get_width/2)/2,self.max_y-(txt.get_height()/2)/2))
                self.file,self.rank = self.get_game_pos()
                for event in pygame.event.get():
                    if event.type == pygame.K_SPACE or event.type == pygame.K_KP5:
                        if (self.x,self.y,self.name) in pieces:
                            selected = False
                            pieces.pop()
                        else:
                            selected = True
                            pieces.append((self.x,self.y,self.name))
                keys = pygame.key.get_pressed()
                if keys[pygame.K_KP2] or keys[pygame.K_2]:
                    self.y += self.square_height
                    if self.y == other.piece_y and self.x == other.piece_x:
                        self.y -= self.square_height
                    self.piece_y = self.y
                if keys[pygame.K_KP4] or keys[pygame.K_4]:
                    self.x -= self.square_width
                    if self.x == other.piece_x and self.y == other.piece_y:
                        self.x += self.square_width
                    self.piece_x = self.x
                    self.has_moved = True
                if keys[pygame.K_KP6] or keys[pygame.K_6]:
                    self.x += self.square_width
                    if self.x == other.piece_x and self.y == other.piece_y:
                        self.x -= self.square_width
                    self.piece_x = self.x
                    self.has_moved = True
                if keys[pygame.K_KP8] or keys[pygame.K_8]:
                    self.y -= self.square_height
                    if self.y == other.piece_y and self.x == other.piece_x:
                        self.x += self.square_height
                    self.piece_y = self.y
                    self.has_moved = True
                while (self.x in limiting_pos[0] and self.y in limiting_pos[1]):
                    if direction == max_direction:
                        break
                    if direction == 0:
                        while self.y <= win_height-self.square_height:
                            self.y += self.square_height
                            if self.y == other.piece_y and self.x == other.piece_x:
                                if other.color != self.color:
                                    self.attacked_pieces.append((self.x,self.y))
                                    self.y -= self.square_height
                                else:
                                    self.y -= self.square_height
                                    break
                            else:
                                self.attacked_pieces.append((self.x,self.y))
                    if direction == 1:
                        while self.x >= 0:
                            self.x -= self.square_width
                            if self.x == self.other.piece_x and self.y == other.piece_y:
                                if other.color != self.color:
                                    self.attacked_pieces.append((self.x,self.y))
                                    self.x += self.square_width
                                else:
                                    self.x += self.square_width
                                    break
                            else:
                                self.attacked_pieces.append((self.x,self.y))
                    if direction == 2:
                        while self.x <= win_width-self.square_width:
                            self.x += self.square_width
                            if self.x == other.piece_x and self.x == other.piece_y:
                                if other.color != self.color:
                                    self.attacked_pieces.append((self.x,self.y))
                                    self.x -= self.square_width
                                else:
                                    self.x -= self.square_width
                                    break
                            else:
                                self.attacked_pieces.append((self.x,self.y))
                    if direction == 3:
                        while self.y >= 0:
                            self.y -= self.square_height
                            if self.x == other.piece_x and self.y == other.piece_y:
                                if other.color != self.color:
                                    self.attacked_pieces.append((self.x,self.y))
                                    self.y += self.square_height
                                else:
                                    self.y += self.square_height
                                    break
                            else:
                                self.attacked_pieces.append((self.x,self.y))
        self.x,self.y = self.piece_x,self.piece_y
        return (self.attacked_pieces,(self.piece_x,self.piece_y),pieces)