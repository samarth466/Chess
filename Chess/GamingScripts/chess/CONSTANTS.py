#from pygame_gui import UIManager
from pygame import Color

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
SQUARE_WIDTH = 100
SQUARE_HEIGHT = 100
#MANAGER = UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))
# This snippet of code goes in ..pieces.knight.Knight.move() upon the completion of potential bugfix in pygame_gui.ui_manager.UI_Manager()
"""
            if ((keys[pygame.K_RALT] and keys[pygame.K_k]) or (keys[pygame.K_LALT] and keys[pygame.K_k])) and not ((keys[pygame.K_RALT] and keys[pygame.K_k]) and (keys[pygame.K_LALT] and keys[pygame.K_k])):
                active = False
                text_input_line = UITextEntryLine(pygame.pygame.Rect(
                    self.x, self.y, self.square_width, self.square_height), manager=MANAGER)
                text_input_line.disable()
                text_input_line.set_allowed_characters(
                    [d for d in string.digits[1:9]] + [l for l in string.ascii_lowercase[:8]])
                text_input_line.set_text_length_limit(2)
                if active:
                    text_input_line.enable()
                    text_input_line.focus()
                                        if keys[pygame.K_RETURN]:
                        text = text_input_line.get_text()
                        file = text[0]
                        rank = int(text[1])
                        move_set = self.get_possible_positions(
                            text[0]+str(text[1]), squares)
                        piece = self.find_piece_from_move_set(
                            move_set, squares)
                        if piece:
                            self.x, self.y = get_window_pos(
                                self.file, self.rank, self.possible_files)
                            original_x, original_y = self.x, self.y
                        else:
                            text = font.render(
                                "You can't move there. There is no knight nearby.")
                            win.blit(text, (self.x, self.y))
                else:
                    text_input_line.disable()
                    text_input_line.unfocus()
"""
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
RED = (255, 0, 0)
BLUE_GREEN = (13, 152, 186)
