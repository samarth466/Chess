import pygame
from game.gaming_scripts.pieces.piece import Piece

class Bishop(Piece):

    def __init__(self,image,file,rank,color,min_x,max_x,min_y,max_y,square_width,square_height,win_width,win_height):
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
        self.x, self.y = self.piece_x, self.piece_y
        self.attacked_pieces = []
        super().__init__(self.image,self.file,self.rank,self.name,self.color)
    
    def move(self,squares,win):
        