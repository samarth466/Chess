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
    
    def get_window_pos(self,file: str = None,rank: int = None):
        if file and rank:
            piece_x = (rank-1)*100
            piece_y = self.possible_files.index(file)*100
        else:
         piece_x = (self.rank-1)*100
         piece_y = self.possible_files.index(self.file)*100
        return piece_x,piece_y
    
    def get_game_pos(self,x: int = None, y: int = None):
        if file and rank:
            rank = x/100+1
            file = self.possible_files[y/100]
        else:
            rank = self.piece_x/100+1
            file = self.possible_files[self.piece_y/100]
        return file,rank
    
    def draw(self,win):
        x,y = self.get_window_pos()
        win.blit(self.image,(x,y))