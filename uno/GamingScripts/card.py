import pathlib
import pygame

class Card:

    def __init__(self,image: pathlib.Path,width: int,height: int,name: str,number: int = None,color: pygame.Color = None,role: str = None) -> None:
        self.width = width
        self.height = height
        self.name = name
        self.color = color
        self.number = number
        self.role = role
        pygame.init()
        self.image = pygame.image.load(image)
    
    def __eq__(self, __o: object) -> bool:
        if type(self) != type(__o):
            return NotImplemented()
        else:
            return self.name.split(' ')[1:] == __o.name.split()[1:] or self.color == __o.color or self.number == __o.number
    
    def draw(self, window: pygame.Surface,x: int,y: int) -> None:
        window.blit(self.image,(x,y))