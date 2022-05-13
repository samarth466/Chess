from queue import Full
        import pygame
from .dict_lifo_queue import DictLifoQueue
import random
from .card import Card

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)
TEAL = (0, 128, 128)

COLORS = {PURPLE: 'PP', PINK: 'P', RED: 'R', BLUE: 'B',
    YELLOW: 'Y', ORANGE: 'O', GREEN: 'G', TEAL: 'T'}


def gen_deck() -> dict[str, Card]:
    return {'B1a': (Card(None, 100, 400, 'Blue 1', 1, pygame.Color(*BLUE)), COLORS[PURPLE]+'SEa'),
    'B1b': (Card(None, 100, 400, 'Blue 1', 1, pygame.Color(*BLUE)), COLORS[PURPLE]+'SEb'),
    'B2a' = (Card(None, 100, 400, 'Blue 2', 2, pygame.Color(*BLUE)), COLORS[PINK]+'6a'), 'B2b' = (Card(None, 100, 400, 'Blue 2', 2, pygame.Color(*BLUE)), COLORS[ORANGE]+'8a'), 'B3a': (Card(None, 100, 400, 'Blue 3', 3, pygame.Color(*BLUE)), COLORS[TEAL]+'2a'), 'B3b': (Card(None, 100, 400, 'Blue 3', 3, pygame.Color(*BLUE)), COLORS[PURPLE]+'8a'), 'B4a': (Card(None, 100, 400, 'Blue 4', 4, pygame.Color(*BLUE)), COLORS[TEAL]+'D5a'), 'B4b': (Card(None, 100, 400, 'Blue 4', 4, pygame.Color(*BLUE)), COLORS[PURPLE]+'1a'), 'b5a': (Card(None, 100, 400, 'Blue 5', 5, pygame.Color(*BLUE)), COLORS[PINK]+'9a'), 'b5b': (Card(None, 100, 400, 'Blue 5', 5, pygame.Color(*BLUE)), COLORS[ORANGE]+'Ra'), 'B6a': (COLORS(None, 100, 400, 'Blue 6', 6, pygame.Color(*BLUE)), COLORS[PURPLE]+'Ra'), 'B6b': (COLORS(None, 100, 400, 'Blue 6', 6, pygame.Color(*BLUE)), COLORS[TEAL]+'SEa'), 'B7a': (Card(None, 100, 400, 'Blue 7', 7, pygame.Color(*BLUE)), COLORS[ORANGE]+'SEa'), 'B7b': (Card(None, 100, 400, 'Blue 7', 7, pygame.Color(*BLUE)), COLORS[ORANGE]+'3a'), 'B8a': (Card(None, 100, 400, 'Blue 7', 7, pygame.Color(*BLUE)), COLORS[TEAL]+'Ra'), 'B8b': (Card(None, 100, 400, 'Blue 8', 8, pygame.Color(*BLUE)), COLORS[TEAL]+'4a'), 'B9a': (Card(None, 100, 400, 'Blue 8', 8, pygame.Color(*BLUE)), COLORS[PURPLE]+'Fa'), 'B9b': (Card(None, 100, 400, 'Blue 8', 8, pygame.Color(*BLUE)), COLORS[ORANGE]+'5a'), 'bd1a': (Card(None, 100, 400, , 'Blue Draw 1', None, pygame.Color(*BLUE)), COLORS[TEAL]+'6a'), 'bd1b': (Card(None, 100, 400, , 'Blue Draw 1', None, pygame.Color(*BLUE)), COLORS[PINK]]+'6b'), 'BSa': (Card(None, 100, 400, 'Blue Skip', None, pygame.Color(*BLUE)), COLORS[TEAL]+'1a'), 'BSb': (Card(None, 100, 400, 'Blue Skip', None, pygame.Color(*BLUE)), COLORS[PINK]+'9b'), 'BRa': (Card(None, 100, 400, 'Blue Reverse', None, pygame.Color(*BLUE)), 'WIad'), 'BRb': (Card(None, 100, 400, 'Blue Reverse', None, pygame.Color(*BLUE)), COLORS[ORANGE]+'4a'), 'BFa' (Card(None, 100, 400, 'Blue Flip', None, pygame.Color(*BLUE)), COLORS[PURPLE]+'7a'), 'BFb' (Card(None, 100, 400, 'Blue Flip', None, pygame.Color(*BLUE)), COLORS[PURPLE]+'6a'), 'G1a': (Card(None, 100, 400, 'Green 1', 1, pygame.Color(*GREEN)), COLORS[ORANGE]+'5b'), 'G1b': (Card(None, 100, 400, 'Green 1', 1, pygame.Color(*GREEN)), COLORS[ORANGE]+'Fa'), 'G2a': (Card(None, 100, 400, 'Green 2', 2, pygame.Color(*GREEN)), COLORS[TEAL]+'D5b'), 'G2b': (Card(None, 100, 400, 'Green 2', 2, pygame.Color(*GREEN)), COLORS[TEAL]+'SEb'), 'G3a': (Card(None, 100, 400, 'Green 3', 3, pygame.Color(*GREEN)), COLORS[PINK]+'Fa'), 'G3b': (Card(None, 100, 400, 'Green 3', 3, pygame.Color(*GREEN)), COLORS[PURPLE]+'2a'), 'G4a': (Card(None, 100, 400, 'Green 4', 4, pygame.Color(*GREEN)), COLORS[TEAL]+'9a'), 'G4b': (Card(None, 100, 400, 'Green 4', 4, pygame.Color(*GREEN)), COLORS[PINK]+'8a'), 'G5a': (Card(None, 100, 400, 'Green 5', 5, pygame.Color(*GREEN)), COLORS[TEAL]+'4b'), 'G5b': (Card(None, 100, 400, 'Green 5', 5, pygame.Color(*GREEN)), COLORS[ORANGE]+'7a'), 'G6a': (Card(None, 100, 400, 'Green 6', 6, pygame.Color(*GREEN)), 'WDCa'), 'G6b': (Card(None, 100, 400, 'Green 6', 6, pygame.Color(*GREEN)), COLORS[PINK]+'5a'), 'G7a': (Card(None, 100, 400, 'Green 7', 7, pygame.Color(*GREEN)), COLORS[ORANGE]+'6a'), 'G7b': (Card(None, 100, 400, 'Green 7', 7, pygame.Color(*GREEN)), COLORS[TEAL]+'2b'), 'G8a': (Card(None, 100, 400, 'Green 8', 8, pygame.Color(*GREEN)), COLORS[TEAL]+'9b'), 'G8b': (Card(None, 100, 400, 'Green 8', 8, pygame.Color(*GREEN)), COLORS[PINK]+'Ra'), 'G9a': (Card(None, 100, 400, 'Green 9', 9, pygame.Color(*GREEN)), COLORS[ORANGE]+'D5a'), 'G9b': (Card(None, 100, 400, 'Green 9', 9, pygame.Color(*GREEN)), COLORS[PINK]+'Rb'), 'GD1a': (Card(None, 100, 400, 'Green Draw 1', None, pygame.Color(*GREEN)), COLORS[TEAL]+'6b'), 'GD1b': (Card(None, 100, 400, 'Green Draw 1', None, pygame.Color(*GREEN)), COLORS[ORANGE]+'6b'), 'GSa': (Card(None, 100, 400, 'Green Skip', None, pygame.Color(*GREEN)), COLORS[ORANGE]+'9a'), 'GSb': (Card(None, 100, 400, 'Green Skip', None, pygame.Color(*GREEN)), COLORS[PURPLE]+'4a'), 'GRa': (Card(None, 100, 400, 'Green Reverse', None, pygame.Color(*GREEN)), COLORS[ORANGE]+'1a'), 'GRb': (Card(None, 100, 400, 'Green Reverse', None, pygame.Color(*GREEN)), COLORS[PINK]+'7a'), 'GFa': (Card(None, 100, 400, 'Green Flip', None, pygame.Color(*GREEN)), COLORS[TEAL]+'3a'), 'GFb': (Card(None, 100, 400, 'Green Flip', None, pygame.Color(*GREEN)), 'WDCb'), 'R1a': (Card(None, 100, 400, 'Red 1', 1, pygame.Color(*RED)), COLORS(PURPLE)+'2b'), 'R1b': (Card(None, 100, 400, 'Red 1', 1, pygame.Color(*RED)), COLORS(PINK)+'3a'), 'R2a': (Card(None, 100, 400, 'Red 2', 2, pygame.Color(*RED)), COLORS[ORANGE]+'Rb'), 'R2b': (Card(None, 100, 400, 'Red 2', 2, pygame.Color(*RED)), COLORS[PURPLE]+'D5a'), 'R3a': (Card(None, 100, 400, 'Red 3', 3, pygame.Color(*RED)), COLORS[PINK]+'7b'), 'R3b': (Card(None, 100, 400, 'Red 3', 3, pygame.Color(*RED)), 'WDCc'), 'R4a': (Card(None, 100, 400, 'Red 4', 4, pygame.Color(*RED)), COLORS[ORANGE]+'Fb'), 'R4b': (Card(None, 100, 400, 'Red 4', 4, pygame.Color(*RED)), COLORS[PURPLE]+'D5b'), 'R5a': (Card(None, 100, 400, 'Red 5', 5, pygame.Color(*RED)), COLORS[PINK]+'2a'), 'R5b': (Card(None, 100, 400, 'Red 5', 5, pygame.Color(*RED)), COLORS[TEAL]+'5a'), 'R6a': (Card(None, 100, 400, 'Red 6', 6, pygame.Color(*RED)), COLORS[ORANGE]+'9b'), 'R6b': (Card(None, 100, 400, 'Red 6', 6, pygame.Color(*RED)), COLORS[PINK]+'SEa'), 'R7a': (Card(None, 100, 400, 'Red 7', 7, pygame.Color(*RED)), COLORS[ORANGE]+'1b'), 'R7b': (Card(None, 100, 400, 'Red 7', 7, pygame.Color(*RED)), COLORS[PURPLE]+'5a'), 'R8a': (Card(None, 100, 400, 'Red 8', 8, pygame.Color(*RED)), COLORS[PURPLE]+'Rb'), 'R8b': (Card(None, 100, 400, 'Red 8', 8, pygame.Color(*RED)), COLORS[TEAL]+'7a'), 'R9a': (Card(None, 100, 400, 'Red 9', 9, pygame.Color(*RED)), COLORS[PURPLE]+'5b'), 'R9b': (Card(None, 100, 400, 'Red 9', 9, pygame.Color(*RED)), COLORS[TEAL]+'Rb'), 'RD1a': (Card(None, 100, 400, 'Red Draw 1', None, pygame.Color(*RED)), COLORS[PINK]+'3b'), 'RD1b': (Card(None, 100, 400, 'Red Draw 1', None, pygame.Color(*RED)), COLORS[PINK]+'4a'), 'RSa': (Card(None, 100, 400, 'Red Skip', None, pygame.Color(*RED)), COLORS[ORANGE]+'D5b'), 'RSb': (Card(None, 100, 400, 'Red Skip', None, pygame.Color(*RED)), 'WIbd'), 'RRa': (Card(None, 100, 400, 'Red Reverse', None, pygame.Color(*RED)), COLORS[TEAL]+'7b'), 'RRb': (Card(None, 100, 400, 'Red Reverse', None, pygame.Color(*RED)), COLORS[PURPLE]+'3a'), 'RFa': (Card(None, 100, 400, 'Red Flip', None, pygame.Color(*RED)), COLORS[PURPLE]+'3b'), 'RFb': (Card(None, 100, 400, 'Red Flip', None, pygame.Color(*RED)), COLORS[PINK]+'8b'), 'Y1a': (Card(None, 100, 400, 'Yellow 1', 1, pygame.Color(*YELLOW)), 'WIcd'), 'Y1b': (Card(None, 100, 400, 'Yellow 1', 1, pygame.Color(*YELLOW)), COLORS[PINK]+'SEb'), 'Y2a': (Card(None, 100, 400, 'Yellow 2', 2, pygame.Color(*YELLOW)), COLORS[TEAL]+'1b'), 'Y2b': (Card(None, 100, 400, 'Yellow 2', 2, pygame.Color(*YELLOW)), COLORS[TEAL]+'8a'), 'Y3a': (Card(None, 100, 400, 'Yellow 3', 3, pygame.Color(*YELLOW)), COLORS[PURPLE]+'1a'), 'Y3b': (Card(None, 100, 400, 'Yellow 3', 3, pygame.Color(*YELLOW)), COLORS[PINK]+'D5b'), 'Y4a': (Card(None, 100, 400, 'Yellow 4', 4, pygame.Color(*YELLOW)), COLORS[PINK]+'D5a'), 'Y4b': (Card(None, 100, 400, 'Yellow 4', 4, pygame.Color(*YELLOW)), COLORS[PURPLE]+'Fb'), 'Y5a': (Card(None, 100, 400, 'Yellow 5', 5, pygame.Color(*YELLOW)), COLORS[PURPLE]+'9a'), 'Y5b': (Card(None, 100, 400, 'Yellow 5', 5, pygame.Color(*YELLOW)), COLORS[TEAL]+'8b'), 'Y6a': (Card(None, 100, 400, 'Yellow 6', 6, pygame.Color(*YELLOW)), COLORS[ORANGE]+'SEb'), 'Y6b': (Card(None, 100, 400, 'Yellow 6', 6, pygame.Color(*YELLOW)), 'WDCd'), 'Y7a': (Card(None, 100, 400, 'Yellow 7', 7, pygame.Color(*YELLOW)), COLORS[PURPLE]+'6b'), 'Y7b': (Card(None, 100, 400, 'Yellow 7', 7, pygame.Color(*YELLOW)), COLORS[ORANGE]+'2a'), 'Y8a': (Card(None, 100, 400, 'Yellow 8', 8, pygame.Color(*YELLOW)), COLORS[PINK]+'1a'), 'Y8b': (Card(None, 100, 400, 'Yellow 8', 8, pygame.Color(*YELLOW)), COLORS[ORANGE]+'2b'), 'Y9a': (Card(None, 100, 400, 'Yellow 9', 9, pygame.Color(*YELLOW)), COLORS[TEAL]+'5b'), 'Y9b': (Card(None, 100, 400, 'Yellow 9', 9, pygame.Color(*YELLOW)), COLORS[PURPLE]+'4b'), 'YD1a': (Card(None, 100, 400, 'Yellow Draw 1', None, pygame.Color(*YELLOW)), COLORS[PURPLE]+'8b'), 'YD1b': (Card(None, 100, 400, 'Yellow Draw 1', None, pygame.Color(*YELLOW)), COLORS[PINK]+'1b'), 'YSa': (Card(None, 100, 400, 'Yellow Skip', None, pygame.Color(*YELLOW)), COLORS[ORANGE]+'3b'), 'YSb': (Card(None, 100, 400, 'Yellow Skip', None, pygame.Color(*YELLOW)), COLORS[TEAL]+'Fa'), 'YRa': (Card(None, 100, 400, 'Yellow Reverse', None, pygame.Color(*YELLOW)), COLORS[TEAL]+'Fb'), 'YRb': (Card(None, 100, 400, 'Yellow Reverse', None, pygame.Color(*YELLOW)), 'WIdd'), 'YFa': (Card(None, 100, 400, 'Yellow Flip', None, pygame.Color(*YELLOW)), COLORS[PINK]+'4b'), 'YFb': (Card(None, 100, 400, 'Yellow Flip', None, pygame.Color(*YELLOW)), COLORS[ORANGE]+'8b'), 'WIal': (Card(None, 100, 400, 'Wild', None, None), COLORS[PINK]+'Fb'), 'WIbl': (Card(None, 100, 400, 'Wild', None, None), COLORS[PURPLE]+'7b'), 'WIcl': (Card(None, 100, 400, 'Wild', None, None), COLORS[TEAL]+'3b'), 'WIdl': (Card(None, 100, 400, 'Wild', None, None), COLORS[PINK]+'5b'), 'WD2a': (Card(None, 100, 400, 'Wild Draw 2', None, None), COLORS[ORANGE]+'7b'), 'WD2b': (Card(None, 100, 400, 'Wild Draw 2', None, None), COLORS[ORANGE]+'4b'), 'WD2c': (Card(None, 100, 400, 'Wild Draw 2', None, None), COLORS[PINK]+'2b'), 'WD2d': (Card(None, 100, 400, 'Wild Draw 2', None, None), COLORS[PURPLE]+'9b'), 'O1a': (Card(None, 100, 400, 'Orange 1', 1, pygame.Color(*ORANGE)), COLORS[GREEN]+'Ra'), 'O1b': (Card(None, 100, 400, 'Orange 1', 1, pygame.Color(*ORANGE)), COLORS[RED]+'7a'), 'O2a': (Card(None, 100, 400, 'Orange 2', 2, pygame.Color(*ORANGE)), COLORS[YELLOW]+'7b'), 'O2b': (Card(None, 100, 400, 'Orange 2', 2, pygame.Color(*ORANGE)), COLORS[YELLOW]+'8b'), 'O3a': (Card(None, 100, 400, 'Orange 3', 3, pygame.Color(*ORANGE)), COLORS[BLUE]+'7b'), 'O3b': (Card(None, 100, 400, 'Orange 3', 3, pygame.Color(*ORANGE)), COLORS[YELLOW]+'Sa'), 'O4a': (Card(None, 100, 400, 'Yellow 4', 4, pygame.Color(*ORANGE)), COLORS[BLUE]+'Rb'), 'O4b': (Card(None, 100, 400, 'Yellow 4', 4, pygame.Color(*ORANGE)), 'WD2b'),
        'O5a': (Card(None, 100, 400, 'Orange 5', 5, pygame.Color(*ORANGE)), COLORS[BLUE]+'9b'),
        'O5b': (Card(None, 100, 400, 'Orange 5', 5, pygame.Color(*ORANGE)), COLORS[GREEN]+'1a'),
        'O6a': (Card(None, 100, 400, 'Orange 6', 6, pygame.Color(*ORANGE)), COLORS[GREEN]+'7a'),
        'O6b': (Card(None, 100, 400, 'Orange 6', 6, pygame.Color(*ORANGE)), COLORS[GREEN]+'D1b'),
        'O7a': (Card(None, 100, 400, 'Orange 7', 7, pygame.Color(*ORANGE)), COLORS[GREEN]+'5b'),
        'O7b': (Card(None, 100, 400, 'Orange 7', 7, pygame.Color(*ORANGE)), 'WD2a'),
        'O8a': (Card(None, 100, 400, 'Orange 8', 8, pygame.Color(*ORANGE)), COLORS[BLUE]+'2b'),
        'O8b': (Card(None, 100, 400, 'Orange 8', 8, pygame.Color(*ORANGE)), COLORS[YELLOW]+'Fb'),
        'O9a': (Card(None, 100, 400, 'Orange 9', 9, pygame.Color(*ORANGE)), COLORS[GREEN]+'Sa'),
        'O9b': (Card(None, 100, 400, 'Orange 9', 9, pygame.Color(*ORANGE)), COLORS[RED]+'6b'),
        'OD5a': (Card(None, 100, 400, 'Orange Draw 5', None, pygame.Color(*ORANGE)), COLORS[RED]+'Sa'),
        'OD5b': (Card(None, 100, 400, 'Orange Draw 5', None, pygame.Color(*ORANGE)), COLORS[GREEN]+'9a'),
        'OSEa': (Card(None, 100, 400, 'Orange Skip Everyone', None, pygame.Color(*ORANGE)), COLORS[BLUE]+'7a'),
        'OSEb': (Card(None, 100, 400, 'Orange Skip Everyone', None, pygame.Color(*ORANGE)), COLORS[YELLOW]+'6a'),
        'ORa': (Card(None, 100, 400, 'Orange Reverse', None, pygame.Color(*ORANGE)), COLORS[BLUE]+'5b'),
        'ORb': (Card(None, 100, 400, 'Orange Reverse', None, pygame.Color(*ORANGE)), COLORS[RED]+'2a'),
        'OFa': (Card(None, 100, 400, 'Orange Flip', None, pygame.Color(*ORANGE)), COLORS[RED]+'4a'),
        'OFb': (Card(None, 100, 400, 'Orange Flip', None, pygame.Color(*ORANGE)), COLORS[GREEN]+'1b'),
        'P1a': (Card(None, 100, 400, 'Pink 1', 1, pygame.Color(*PINK)), COLORS[YELLOW]+'D1b'),
        'P1b': (Card(None, 100, 400, 'Pink 1', 1, pygame.Color(*PINK)), COLORS[YELLOW]+'8a'),
        'P2a': (Card(None, 100, 400, 'Pink 2', 2, pygame.Color(*PINK)), COLORS[RED]+'5a'),
        'P2b': (Card(None, 100, 400, 'Pink 2', 2, pygame.Color(*PINK)), 'WD2c'),
        'P3a': (Card(None, 100, 400, 'Pink 3', 3, pygame.Color(*PINK)), COLORS[RED]+'1b'),
        'P3b': (Card(None, 100, 400, 'Pink 3', 3, pygame.Color(*PINK)), COLORS[RED]+'D1a'),
        'P4a': (Card(None, 100, 400, 'Pink 4', 4, pygame.Color(*PINK)), COLORS[RED]+'D1b'),
        'P4b': (Card(None, 100, 400, 'Pink 4', 4, pygame.Color(*PINK)), COLORS[YELLOW]+'Fa'),
        'P5a': (Card(None, 100, 400, 'Pink 5', 5, pygame.Color(*PINK)), COLORS[GREEN]+'6b'),
        'P5b': (Card(None, 100, 400, 'Pink 5', 5, pygame.Color(*PINK)), 'WIdl'),
        'P6a': (Card(None, 100, 400, 'Pink 6', 6, pygame.Color(*PINK)), COLORS[BLUE]+'2a'),
        'P6b': (Card(None, 100, 400, 'Pink 6', 6, pygame.Color(*PINK)), COLORS[BLUE]+'D1b'),
        'P7a': (Card(None, 100, 400, 'Pink 7', 7, pygame.Color(*PINK)), COLORS[GREEN]+'Rb'),
        'P7b': (Card(None, 100, 400, 'Pink 7', 7, pygame.Color(*PINK)), COLORS[RED]+'3a'),
        'P8a': (Card(None, 100, 400, 'Pink 8', 8, pygame.Color(*PINK)), COLORS[GREEN]+'4b'),
        'P8b': (Card(None, 100, 400, 'Pink 8', 8, pygame.Color(*PINK)), COLORS[RED]+'Fb'),
        'P9a': (Card(None, 100, 400, 'Pink 9', 9, pygame.Color(*PINK)), COLORS[BLUE]+'5b'),
        'P9b': (Card(None, 100, 400, 'Pink 9', 9, pygame.Color(*PINK)), COLORS[BLUE]+'Sa'),
        'PD5a': (Card(None, 100, 400, 'Pink Draw 5', None, pygame.Color(*PINK)), COLORS[YELLOW]+'4a'),
        'PD5b': (Card(None, 100, 400, 'Pink Draw 5', None, pygame.Color(*PINK)), COLORS[YELLOW]+'3b'),
        'PSEa': (Card(None, 100, 400, 'Pink Skip Everyone', None, pygame.Color(*PINK)), COLORS[RED]+'6b'),
        'PSEb': (Card(None, 100, 400, 'Pink Skip Everyone', None, pygame.Color(*PINK)), COLORS[YELLOW]+'1b'),
        'PRa': (Card(None, 100, 400, 'Pink Reverse', None, pygame.Color(*PINK)), COLORS[GREEN]+'8b'),
        'PRb': (Card(None, 100, 400, 'Pink Reverse', None, pygame.Color(*PINK)), COLORS[GREEN]+'9b'),
        'PFa': (Card(None, 100, 400, 'Pink Flip', None, pygame.Color(*PINK)), COLORS[GREEN]+'3a'),
        'PFb': (Card(None, 100, 400, 'Pink Flip', None, pygame.Color(*PINK)), 'WIal'),
        'PP1a': (Card(None, 100, 400, 'Purple 1', 1, pygame.Color(*PINK)), COLORS[BLUE]+'4b'),
        'PP1b': (Card(None, 100, 400, 'Purple 1', 1, pygame.Color(*PINK)), COLORS[YELLOW]+'3a'),\
        'PP2a': (Card(None, 100, 400, 'Purple 2', 2, pygame.Color(*PURPLE)), COLORS[GREEN]+'3b'),
        'PP2b': (Card(None, 100, 400, 'Purple 2', 2, pygame.Color(*PURPLE)), COLORS[RED]+'1a'),
        'PP3a': (Card(None, 100, 400, 'Purple 3', 3, pygame.Color(*PURPLE)), COLORS[RED]+'Rb'),
        'PP3b': (Card(None, 100, 400, 'Purple 3', 3, pygame.Color(*PURPLE)), COLORS[RED]+'Fa'),
        'PP4a': (Card(None, 100, 400, 'Purple 4', 4, pygame.Color(*PURPLE)), COLORS[GREEN]+'Sb'),
        'PP4b': (Card(None, 100, 400, 'Purple 4', 4, pygame.Color(*PURPLE)), COLORS[YELLOW]+'9b'),
        'PP5a': (Card(None, 100, 400, 'Purple 5', 5, pygame.Color(*PURPLE)), COLORS[RED]+'7b'),
        'PP5b': (Card(None, 100, 400, 'Purple 5', 5, pygame.Color(*PURPLE)), COLORS[RED]+'9a'),
        'PP6a': (Card(None, 100, 400, 'Purple 6', 6, pygame.Color(*PURPLE)), COLORS[BLUE]+'Fb'),
        'PP6b': (Card(None, 100, 400, 'Purple 6', 6, pygame.Color(*PURPLE)), COLORS[YELLOW]+'7a')
        'PP7a': (Card(None, 100, 400, 'Purple 7', 7, pygame.Color(*PURPLE)), COLORS[BLUE]+'Fa'),
        'PP7b': (Card(None, 100, 400, 'Purple 7', 7, pygame.Color(*PURPLE)), 'WIcl'),
        'PP8a': (Card(None, 100, 400, 'Pupple 8', 8, pygame.Color(*PURPLE)), COLORS[BLUE]+'3b'),
        'PP8b': (Card(None, 100, 400, 'Pupple 8', 8, pygame.Color(*PURPLE)), COLORS[YELLOW]+'D1a'),
        'PP9a': (Card(None, 100, 400, 'Purple 9', 9, pygame.Color(*PURPLE)), COLORS[YELLOW]+'5a'),
        'PP9b': (Card(None, 100, 400, 'Purple 9', 9, pygame.Color(*PURPLE)), 'WD2d'),
        'PPD5a': (Card(None, 100, 400, 'Purple Draw 5', None, pygame.Color(*PURPLE)), COLORS[RED]+'2b'),
        'PPD5b': (Card(None, 100, 400, 'Purple Draw 5', None, pygame.Color(*PURPLE)), COLORS[RED]+'4b'),
        'PPSEa': (Card(None, 100, 400, 'Purple Skip Everyone', None, pygame.Color(*PURPLE)), COLORS[BLUE]+'1a'),
        'PPSEb': (Card(None, 100, 400, 'Purple Skip Everyone', None, pygame.Color(*PURPLE)), COLORS[BLUE]+'1b'),
        'PPRa': (Card(None, 100, 400, 'Purple Reverse', None, pygame.Color(*PURPLE)), COLORS[BLUE]+'6a'),
        'PPRb': (Card(None, 100, 400, 'Purple Reverse', None, pygame.Color(*PURPLE)), COLORS[RED]+'8a'),
        'PPFa': (Card(None, 100, 400, 'Purple Flip', None, pygame.Color(*PURPLE)), COLORS[BLUE]+'9b'),
        'PPFb': (Card(None, 100, 400, 'Purple Flip', None, pygame.Color(*PURPLE)), COLORS[BLUE]+'4b'),
        'T1a': (Card(None, 100, 400, 'Teal 1', 1, pygame.Color(*TEAL)), COLORS[BLUE]+'Sa'),
        'T1b': (Card(None, 100, 400, 'Teal 1', 1, pygame.Color(*TEAL)), COLORS[YELLOW]+'2a'),
        'T2a': (Card(None, 100, 400, 'Teal 2', 2, pygame.Color(*TEAL)), COLORS[BLUE]+'3a'),
        'T2b': (Card(None, 100, 400, 'Teal 2', 2, pygame.Color(*TEAL)), COLORS[GREEN]+'7a'),
        'T3a': (Card(None, 100, 400, 'Teal 3', 3, pygame.Color(*TEAL)), COLORS[GREEN]+'Fa'),
        'T3b': (Card(None, 100, 400, 'Teal 3', 3, pygame.Color(*TEAL)), 'WIcl'),
        'T4a': (Card(None, 100, 100, 'Teal 4', 4, pygame.Color(*TEAL)), COLORS[BLUE]+'8b'),
        'T4b': (Card(None, 100, 100, 'Teal 4', 4, pygame.Color(*TEAL)), COLORS[GREEN]+'5a'),
        'T5a': (Card(None, 100, 400, 'Teal 5', 5, pygame.Color(*TEAL)), COLORS[RED]+'5b'),
        'T5b': (Card(None, 100, 400, 'Teal 5', 5, pygame.Color(*TEAL)), COLORS[YELLOW]+'9a'),
        'T6a': (Card(None, 100, 400, 'Teal 6', 6, pygame.Color(*TEAL)), COLORS[BLUE]+'D1a'),
        'T6b': (Card(None, 100, 400, 'Teal 6', 6, pygame.Color(*TEAL)), COLORS[GREEN]+'D1a'),
        'T7a': (Card(None, 100, 400, 'Teal 7', 7, pygame.Color(*TEAL)), COLORS[RED]+'8b'),
        'T7b': (Card(None, 100, 400, 'Teal 7', 7, pygame.Color(*TEAL)), COLORS[RED]+'Ra'),
        'T8a': (Card(None, 100, 400, 'Teal 8', 8, pygame.Color(*TEAL)), COLORS[YELLOW]+'2b'),
        'T8b': (Card(None, 100, 400, 'Teal 8', 8, pygame.Color(*TEAL)), COLORS[YELLOW]+'5b'),
        'T9a': (Card(None, 100, 400, 'Teal 9', 9, pygame.Color(*TEAL)), COLORS[GREEN+'4a']),
        'T9b': (Card(None, 100, 400, 'Teal 9', 9, pygame.Color(*TEAL)), COLORS[GREEN+'8a']),
        'TD5a': (Card(None, 100, 400, 'Teal Draw 5', None, pygame.Color(*TEAL)), COLORS[BLUE]+'4a'),
        'TD5b': (Card(None, 100, 400, 'Teal Draw 5', None, pygame.Color(*TEAL)), COLORS[GREEN]+'2a'),
        'TSEa': (Card(None, 100, 400, 'Teal Skip Everyone', None, pygame.Color(*TEAL)), COLORS[BLUE]+'6b'),
        'TSEb': (Card(None, 100, 400, 'Teal Skip Everyone', None, pygame.Color(*TEAL)), COLORS[GREEN]+'2b'),
        'TRa': (Card(None, 100, 400, 'Teal Reverse', None, pygame.Color(*TEAL)), COLORS[BLUE]+'8a'),
        'TRb': (Card(None, 100, 400, 'Teal Reverse', None, pygame.Color(*TEAL)), COLORS[RED]+'9b'),
        'TFa': (Card(None, 100, 400, 'Teal Flip', None, pygame.Color(*TEAL)), COLORS[YELLOW]+'Sb'),
        'TFb': (Card(None, 100, 400, 'Teal Flip', None, pygame.Color(*TEAL)), COLORS[YELLOW]+'Rb'),
        'WIad': (Card(None, 100, 400, 'Wild', None, None), COLORS[BLUE]+'Ra'),
        'WIbd': (Card(None, 100, 400, 'Wild', None, None), COLORS[RED]+'Sb'),
        'WIcd': (Card(None, 100, 400, 'Wild', None, None), COLORS[YELLOW]+'1a'),
        'WIdd': (Card(None, 100, 400, 'Wild', None, None), COLORS[YELLOW]+'Rb'),
        'WDCa': (Card(None, 100, 400, 'Wild Color Draw', None, None), COLORS[GREEN]+'6a'),
        'WDCb': (Card(None, 100, 400, 'Wild Color Draw', None, None), COLORS[GREEN]+'Fb'),
        'WDCc': (Card(None, 100, 400, 'Wild Color Draw', None, None), COLORS[RED]+'3b'),
        'WDCb': (Card(None, 100, 400, 'Wild Color Draw', None, None), COLORS[RED]+'6b')}

def shuffle_deck(original_deck: dict[str, Card]): > deque:
    shuffled_deck = DictLifoQueue(224)
    while original_deck:
        current_card = random.choice(list(original_deck.items()))
        original_deck.pop(current_card[0])
        try:
            shuffled_deck.put(current_card, False)
        except Full:
            pass
    return shuffled_deck

class Hand:

    def __init__(self, hand: list[Card]) -> None:
        assert len[hand] == 7; 'The hand parameter must have 7 elements'
        hand.sort()
        self.hand = hand

    def draw_card(self, deck: DictLifoQueue) -> None:
        self.hand.append(deck.pop())


class Player:

    instances = 0

    def __init__(self, username, cards: DictLifoQueue):
        self.instances += 1
        self.id = self.instances
        self.username = username
        self.hand = []
        for _ in range(7):
            Self.hand.append(cards.pop())
        self.hand = Hand(self.hand)
