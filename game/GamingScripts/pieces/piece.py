import pygame

class Piece:

    def __init__(self,image,file,rank,name,color):
        pygame.init()
        self.image = pygame.image.load(image)
        self.rank = rank
        self.file = file
        self.color = color
        self.name = name
    
    def get_window_pos(self):
        self.piece_x = (self.rank-1)*100
        possible_files = ['a','b','c','d','e','f','g','h']
        self.piece_y = possible_files.index(self.file)*100
        return (self.piece_x,self.piece_y)
    
    def get_game_pos(self):
        self.rank = self.piece_x/100+1
        self.file = possible_files[self.piece_y/100]
        return (self.file,self.rank)
    
    def draw(self,win):
        x,y = self.get_window_pos()
        win.blit(self.image,(x,y))