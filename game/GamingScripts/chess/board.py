from pathlib import Path
from os.path import join
from typing import Any, Tuple
import pygame
from ..pieces import Bishop,Pawn,Knight,Rook
from ..board_utils.square import Square
from ..chess.CONSTANTS import (WHITE,BLACK,GREY)
from .player import Player

class Board(object):

    def __init__(self,size: Tuple[int,int],square_width: int,square_height: int,player1: Player,player2: Player,window: pygame.Surface,upper_offset: int = 0,lower_offset: int = 0) -> Any:
        """
        Initialize the Board class.
        """
        pygame.init()
        self.win_width,self.win_height = size
        self.square_width = square_width
        self.square_height = square_height
        self.player1 = player1
        self.player2 = player2
        self.window = window
        self.upper_offset = upper_offset
        self.lower_offset = lower_offset
        self.captured_pieces = []
        self.possible_files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#        self.file,self.rank = self.get_game_pos(x=column,y=row)
        self.path = Path("C:/Users/samar/OneDrive/Desktop/Python Programming/Chess/game/GamingScripts/Chessmen")
        self.images = {
            'BLACK': {
                'Bishop': join(self.path,'B_Bishop.png'),
                'King': join(self.path,'B_King.png'),
                'Knight': join(self.path,'B_Knight.png'),
                'Pawn': join(self.path,'B_Pawn.png'),
                'Queen': join(self.path,'B_Queen.png'),
                'Rook': join(self.path,'B_Rook.png')
            },
            'WHITE': {
                'Bishop': join(self.path,'W_Bishop.png'),
                'King': join(self.path,'W_King.png'),
                'Knight': join(self.path,'W_Knight.png'),
                'Pawn': join(self.path,'W_Pawn.png'),
                'Queen': join(self.path,'W_Queen.png'),
                'Rook': join(self.path,'W_Rook.png')
            }
        }
        self.matterial = {
            'BLACK': {
                'Bishop': [
                    Bishop(self.image['BLACK']['Bishop'],'C',8,BLACK,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height),
                    Bishop(self.image['BLACK']['Bishop'],'F',8,BLACK,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height)
                ],
                'King': None,
                'Knight': [
                    Knight(self.images['BLACK']['Knight'],'B',8,BLACK,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height),
                    Knight(self.images['BLACK']['Knight'],'G',8,BLACK,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height)
                ],
                'Pawn': [
                    Pawn(self.images['BLACK']['Pawn'],'A',7,BLACK,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height),
                    Pawn(self.images['BLACK']['Pawn'],'B',7,BLACK,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height),
                    Pawn(self.images['BLACK']['Pawn'],'C',7,BLACK,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height),
                    Pawn(self.images['BLACK']['Pawn'],'D',7,BLACK,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height),
                    Pawn(self.images['BLACK']['Pawn'],'E',7,BLACK,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height),
                    Pawn(self.images['BLACK']['Pawn'],'F',7,BLACK,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height),
                    Pawn(self.images['BLACK']['Pawn'],'G',7,BLACK,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height),
                    Pawn(self.images['BLACK']['Pawn'],'H',7,BLACK,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height)
                ],
                'Queen': None,
                'Rook': [
                    Rook(self.images['BLACK']['Rook'],'A',8,BLACK,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height),
                    Rook(self.images['BLACK']['Rook'],'H',8,BLACK,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height)
                ]
            },
            'WHITE': {
                'Bishop': [
                    Bishop(self.image['WHITE']['Bishop'],'C',2,BLACK,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height),
                    Bishop(self.image['WHITE']['Bishop'],'F',2,WHITE,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height)
                ],
                'King': None,
                'Knight': [
                    Knight(self.images['WHITE']['Knight'],'B',2,WHITE,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height),
                    Knight(self.images['WHITE']['Knight'],'G',2,WHITE,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height)
                ],
                'Pawn': [
                    Pawn(self.images['WHITE']['Pawn'],'A',2,WHITE,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height),
                    Pawn(self.images['WHITE']['Pawn'],'B',2,WHITE,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height),
                    Pawn(self.images['WHITE']['Pawn'],'C',2,WHITE,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height),
                    Pawn(self.images['WHITE']['Pawn'],'D',2,WHITE,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height),
                    Pawn(self.images['WHITE']['Pawn'],'E',2,WHITE,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height),
                    Pawn(self.images['WHITE']['Pawn'],'F',2,WHITE,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height),
                    Pawn(self.images['WHITE']['Pawn'],'G',2,WHITE,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height),
                    Pawn(self.images['WHITE']['Pawn'],'H',2,WHITE,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height)
                ],
                'Queen': None,
                'Rook': [
                    Rook(self.images['WHITE']['Rook'],'A',1,WHITE,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height),
                    Rook(self.images['WHITE']['Rook'],'H',1,WHITE,0,self.win_width,0,self.win_height,self.square_width,self.square_height,self.win_width,self.win_height)
                ]
            }
        }
    
    def get_window_pos(self, rank: int, file: str) -> Tuple[int,int]:
        x = self.possible_files.index(file.lower())*self.square_width
        y = (rank-1)*self.square_height
        return (x, y)

    def get_game_pos(self, x: int, y: int) -> Tuple[str,int]:
        file = self.possible_files[x*self.square_width]
        rank = y/self.square_height+1
        return (file, rank)
    
    def move(self):
        squares = {}
        for rank in range(1,9):
            for file in self.possible_files:
                for piece in self.matterial['BLACK'].values()+[None for _ in range(32)]+self.matterial['WHITE'].values():
                    squares[self.get_window_pos(rank,file.upper())] = Square(rank,file,WHITE if rank%2 == 1 and file.lower() in self.possible_files[::2] else BLACK,piece,self.square_width,self.square_height)
        for color in self.matterial.values():
            for piece_list in color.values():
                if piece_list:
                    for piece in piece_list:
                        piece.move(self.window,squares,self)
    
    def create_board(self):
        self.board = pygame.Surface((self.win_width,self.win_height))
        self.offset_box_1 = pygame.Surface((self.win_width,self.upper_offset))
        self.offset_box_2 = pygame.Surface((self.win_width,self.lower_offset))
        pygame.draw.rect(self.window,GREY,self.board)
        pygame.draw.rect(self.window,GREY,self.offset_box_1)
        pygame.draw.rect(self.window,GREY,self.offset_box_2)
        for row in range(self.win_height/self.square_height):
            for column in range(self.win_width/self.square_width):
                s = Square(self.rank,self.file,WHITE if row%2 == 0 and column%2 == 0 else BLACK,None,self.square_width,self.square_height)
                if row == 0:
                    if collumn == 0:
                        s.piece = self.matterial['WHITE']['Rook'][0]
                    elif column == 1:
                        s.piece = self.matterial['WHITE']['Knight'][0]
                    elif column == 2:
                        s.piece = self.matterial['WHITE']['Bishop'][0]
                    elif column == 5:
                        s.piece = self.matterial['WHITE']['Bishop'][1]
                    elif column == 6:
                        s.piece = self.matterial['WHITE']['Knight'][1]
                    elif column == 7:
                        s.piece = self.matterial['WHITE']['Rook'][1]
                elif row == 1:
                    s.piece = self.matterial['WHITE']['Pawn'][column]
                elif row == 6:
                    s.piece = self.matterial['BLACK']['Pawn'][column]
                elif row == 7:
                    if column == 0:
                        s.piece = self.matterial['BLACK']['Rook'][0]
                    elif column == 1:
                        s.piece = self.matterial['BLACK']['Knight'][0]
                    elif column == 2:
                        s.piece = self.matterial['BLACK']['Bishop'][0]
                    elif column == 5:
                        s.piece = self.matterial['BLACK']['Bishop'][1]
                    elif column == 6:
                        s.piece = self.matterial['BLACK']['Knight'][1]
                    elif column == 7:
                        s.piece = self.matterial['BLACK']['Rook'][1]
                self.board.blit(s,(column,row))
    
    def capture_piece(self,x,y):
        for color,color_pieces in self.matterial.values:
            for piece,piece_list in color_pieces:
                if piece_list:
                    for i,piece in enumerate(piece_list):
                        if piece.x == x and piece.y == y:
                            captured_piece = self.matterial[color][piece].pop(i)
                            self.captured_pieces.append(captured_piece)
                            self.draw_captured_pieces(captured_piece)
    
    def draw_captured_pieces(self,captured_piece):
        if self.player1.color != captured_piece.color:
            for x in range(0,self.win_width,100):
                for y in range(0,self.upper_offset,100):
                    pixel_color = self.offset_box_1.get_at((x,y))
                    if (pixel_color.r,pixel_color.g,pixel_color.b) == GREY:
                        self.offset_box_1.blit(captured_piece,(x,y))
        if self.player2.color != captured_piece.color:
            for x in range(0,self.win_width,100):
                for y in range(0,self.lower_offset,100):
                    pixel_color = self.offset_box_2.get_at((x,y))
                    if (pixel_color.index(0),pixel_color.index(1),pixel_color.index(3)) == GREY:
                        self.offset_box_2.blit(captured_piece,(x,y))