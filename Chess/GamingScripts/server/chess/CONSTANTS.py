from pygame import Color
from pygame.display import Info, init

init()
WINDOW_WIDTH = WINDOW_HEIGHT = min(Info().current_w, Info().current_h)
SQUARE_WIDTH = WINDOW_WIDTH//8
SQUARE_HEIGHT = WINDOW_HEIGHT//8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
#RED = (255, 0, 0)
