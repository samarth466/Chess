import pygame
import chess_py

class Square:

    def __init__(self,rank,file,color,piece,square_length,is_empty=False):
        self.rank = rank
        self.file = file
        self.color = color
        self.is_empty = is_empty
        self.piece = piece
        self.square_length = square_length
        self.is_emptiable = True
    
    def get_window_pos(self):
        self.x = (self.rank-1)*100
        possible_files = ['a','b','c','d','e','f','g','h']
        self.y = possible_files.index(self.file.lower())*100
        return (self.x,self.y)
    
    def draw(self,win):
        x,y = self.get_window_pos()
        pygame.init()
        self.rect = pygame.Rect(x,y,self.square_length,self.square_length)
        self.draw_square = pygame.gfxdraw.rectangle(win,self.rect,self.color)
        return self.draw_square
    
    def is_under_attack(self):
        