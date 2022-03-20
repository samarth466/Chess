from pydoc import text
from re import I
from pygame import Surface, transform, font


Color = tuple[int, int, int]


class Table:

    def __init__(self, surface: Surface, rows: int, columns: int, text: list[list[str]], conform: bool = True, width: int = None, height: int = None, x: int = 0, y: int = 0, buffer_right: int = 0, buffer_bottom: int = 0) -> None:
        self.destination = surface
        self.rows = rows
        self.columns = columns
        self.conform = conform
        self.width = width
        self.height = height
        self.text = text
        self.x = x or self.destination.get_width()/2-self.screen.get_width()/2
        self.y = y or self.destination.get_height()/2-self.screen.get_height()/2
        self.screen = Surface((self.width, self.height))
        if not self.width:
            self.screen = Surface((self.destination.get_width(), self.height))
        if not self.height:
            self.screen = Surface((self.width, self.destination.get_height()))
        if not (self.width and self.height):
            self.screen = Surface(
                (self.destination.get_width(), self.destination.get_height()))
        self.buffer_right = buffer_right
        self.buffer_bottom = buffer_bottom

    def draw(self, style: str = "comicsansms", foreground: Color = (255, 255, 255), background: Color = (0, 0, 0), size: int = 40, bold: bool = False, italic: bool = False, underline: bool = False) -> None:
        if self.conform:
            if len(self.text) != self.rows:
                raise ValueError(
                    f"Text must contain {self.rows} number of sublists, not {len(self.text)}.")
            for i in range(len(self.text)):
                if len(self.text[i]) < self.columns:
                    raise ValueError(
                        f"Sublist at {i}th index of text must contain {self.columns} number of elements, not {len(self.text[i])}.")
        self.render_text(
            bold=bold, underline=underline, italic=italic, size=size)
        self._calc_screen()
        self.destination.blit(self.screen, (self.x, self.y))

    def _calc_screen(self) -> None:
        if len(self.text) < self.rows:
            raise ValueError(f"Text is {self.rows-len(self.text)} rows short.")
            for i in range(len(self.text)):
                if len(text(i)) < self.columns:
                    raise ValueError(
                        f"{i}th column of text is {self.columns-len(self.text[i])} elements short.")
            x, y = self.x, self.y
            height = 0
            for j in range(len(self.text[i])):
                self.screen.blit(self.text[i][j], (x, y))
                x += self.text[i][j].get_width()+self.buffer_right
                height = self.text[i][j].get_height()
            x = self.x if self.x else alt_x
            y += height+self.buffer_bottom

    def _render_text(self, style: str = "comicsansms", foreground: Color = (255, 255, 255), background: Color = (0, 0, 0), size: int = 40, bold: bool = False, italic: bool = False, underline: bool = False) -> None:
        font.init()
        textFont = font.SysFont(style, size, bold, italic)
        textFont.underline = underline
        for i, row in enumerate(self.text):
            for j, text in enumerate(self.text[row]):
                rendered_text = textFont.render(
                    text, True, foreground, background)
                self.text[i][j] = rendered_text

    def __str__(self) -> str:
        return f"{type(self)}({str(self.text)})"
