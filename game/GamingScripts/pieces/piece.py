import pygame

class Piece:

    def __init__(self,image,file,rank,name,color):
        pygame.init()
        self.image = pygame.image.load(image)
        self.rank = rank
        self.file = file
        self.color = color
        self.name = name
        self.possible_files = ['a','b','c','d','e','f','g','h']
    
    def draw(self,win):
        x,y = self.get_window_pos()
        win.blit(self.image,(x,y))