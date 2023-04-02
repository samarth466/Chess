from typing import Coroutine
from pygame import Surface, transform, font


Color = tuple[int,int,int]
class Table:

    def __init__(self, surface: Surface, rows: int, columns: int, text: list[list[str]], conform: bool = True, width: int = None, height: int = None, x: int = 0, y: int = 0, buffer_right: int = 0, buffer_bottom: int = 0) -> None:
        self.destination = surface
        self.rows = rows
        self.columns = columns
        self.conform = conform
        self.width = width
        self.height = height
        self.text = text
        self.x = x
        self.y = y
        self.center = (x == None) and (y == None)
        self.screen = Surface((self.width, self.height))
        if not self.width:
            self.screen = Surface((self.destination.get_width(),self.height))
        if not self.height:
            self.screen = Surface((self.width,self.destination.get_height()))
        if not (self.width and self.height):
            self.screen = Surface((self.destination.get_width(), self.destination.get_height()))
        self.buffer_right = buffer_right
        self.buffer_bottom = buffer_bottom

    def draw(self) -> None:
        if self.conform:
            if len(self.text) != self.rows:
                raise ValueError(f"Text must contain {self.rows} number of sublists, not {len(self.text}.")
            error_messages = [f"Sublist at {i}th index of text must contain {self.columns} number of elements, not {len(self.text[i]}." for i in range(len(self.text))]
            for error_message in error_messages:
                raise ValueError(error_message)
        self.render_text()
        if (self.height and self.width):
            self._calc_screen()
        else:
            self.screen = transform.scale(
                self.screen, self.destination.get_size())
            self._calc_screen()
    
    def _calc_screen(self) -> None:
        if len(self.text) < self.rows:
            raise ValueError(f"Text is {self.rows-len(self.text} rows short.")
        for i in range(self.rows):
            if len(self.text[i]) < self.columns:
                raise ValueError(f"{i}th row of text is {self.columns-len(self.text[i]} columns short.")
            alt_x = self.destination.get_width()/2-self.screen.get_width()/2
            alt_y = self.destination.get_height()/2-self.screen.get_height()/2
            x, y = self.x, self.y if self.x and self.y else alt_x, alt_y
            deltay = 0
            for j in range(len(self.text[i])):
                self.screen.blit(self.text[i][j], (x, y))
                x += self.text[i][j].get_width()+self.buffer_right
                height = self.text[i][j].get_height() if self.text[i][j].get_height > height
            x = self.x if self.x else alt_x
            y += deltay+self.buffer_bottom
    
    def render_text(self,source: Surface,top: int,left: int,style: str = "comicsansms",foreground: Color = (255,255,255),background: Coroutine = (0,0,0),size: int = 62,bold: bool = False,italic: bool = False,underline: bool = False) -> None:
        font.init()
        textFont = font.SysFont("comicsansms",size,bold,italic)
        textFont.underline = underline
        height = 0
        x = left
        for row in self.text:
            for text in self.text[row]:
                rendered_text = textFont.render(text,True,foreground,background)
                source.blit(rendered_text,(left,top))
                left += rendered_text.get_width()+self.buffer_right
                height += rendered_text.get_width()
            left = x
            top += height+self.buffer_bottom
    
    def __str__(self) -> str:
        return f"{type(self)}({str(self.text)})"