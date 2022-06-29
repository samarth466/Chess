from ast import Str
from distutils import text_file
from turtle import st
import pygame
from queue import Queue
from random import randint
import time

# Initializations
pygame.init()
pygame.display.init()
pygame.font.init()
WIDTH, HEIGHT = (800, 800)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mine Sweeper")
ROWS = COLUMNS = 8
MINES = MAX_FLAGS = 10
NUMBER_FONT = pygame.font.SysFont("ComicSans",20)
clicks = 0


# Colors
covered_color = (140,140,140)
background_color = (200,200,200)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PINK = (255, 192, 203)
ORANGE = (255, 165, 0)
BROWN = (150, 77, 0)
PURPLE = (160, 32, 240)
BLACK = (0,0,0)
game_colors = {
    1: BLUE,
    2: GREEN,
    3: RED,
    4: YELLOW,
    5: ORANGE,
    6: PINK,
    7: PURPLE,
    8: BROWN
}


def get_neighbors(row: int,column: int,rows: int,columns: int,field: list[list[int]]) -> list[tuple[int,int]]:
    neighbors = []
    if row > 0:
        neighbors.append((row-1,column))
    if column > 0:
        neighbors.append((row,column-1))
    if row < rows-1:
        neighbors.append((row+1,column))
    if column < columns-1:
        neighbors.append((row,column+1))
    if row > 0 and column > 0:
        neighbors.append((row-1,column-1))
    if row > 0 and column < columns-1:
        neighbors.append((row-1, column+1))
    if row < rows-1 and column > 0:
        neighbors.append((row+1, column-1))
    if row < rows-1 and column < columns:
        neighbors.append((row+1, column+1))
    return neighbors


def create_field(rows: int, columns: int, mines: int) list[list[int]]:
    field = [[0 for _ in range(columns)] for _ in range(rows)]
    mine_positions = set()
    while len(mine_positions) < mines:
        row = randint(0,rows-1)
        column = randint(0,columns-1)
        mine_positions.add((row,column))
        field[row][column] = -2
        for r,c in get_neighbors(row,column):
            field[r][c] += 1
    return field


def draw(window: pygame.Surface, field: list[list[int]], cover_field: list[list[int]],width: int, rows: int,columns: int):
    window.fill(BLACK)
    size = width//row
    for i,row in enumerate(field):
        for j,value in enumerate(row):
            x = size*j
            y = size*i
            pygame.draw.rect(window,background_color,(x,y,size,size))
            if value == -2:
                pygame.draw.circle(window,RED,(i+size//2,j+size//2),size/4)
            elif value == 0:
                continue
            else:
                text = NUMBER_FONT.render(str,1,game_colors[value])
                window.blit(text,(x+size//2+text.get_width()//2,y+size//2-text.get_height()/2))


def main():
    cover_field = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]
    run = True
    while run:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run = False
    pygame.quit()


if __name__ == "__main__":
    main()
