from typing import Sequence
import string

import pygame
from .flatten import flatten


def get_string_from_sequence(seq: Sequence) -> str:
    flattened_list = flatten(seq)
    return ''.join(flattened_list)


def get_window_pos(file: str, rank: int, possible_files: list[str], width: int, height: int) -> tuple[int, int]:
    assert len(possible_files) == 8 and possible_files == [
        letter for letter in string.ascii_uppercase[:8]], f"The 'possible_files' argument must be equivalent to {str([letter for letter in string.ascii_lowercase[:8]])}, not {possible_files}"
    if file == None or rank == None:
        return None, None
    x = (rank-1)*width
    y = possible_files.index(file)*height
    return x, y


def get_game_pos(x: int, y: int, possible_files: list[str], width: int, height: int) -> tuple[str, int]:
    assert len(possible_files) == 8 and possible_files == [letter for letter in string.ascii_uppercase[
        :8]], f"The 'possible_files' argument must be equivalent to {[letter for letter in string.ascii_uppercase[:8]]}"
    rank = x//width+1
    file = possible_files[y//height]
    return file, rank


def toggle_full_screen(screen: pygame.Surface, expand: bool = True, add_boxes: list[pygame.Rect] = None, main_window_top_position: int = None, main_window_bottom_position: int = None, main_window: pygame.Surface = None) -> pygame.Surface:
    if expand:
        if not add_boxes:
            raise NotImplemented(
                "We cannot expand the window if nothing is passed to add to the screen.")
        else:
            for box in add_boxes:
                if not (main_window_top_position and main_window and main_window_bottom_position):
                    arguments = str([str(i) for i in filter(lambda i: not i, [
                                    main_window_top_position, main_window, main_window_bottom_position])])[1:-2]
                    msg = arguments + \
                        ' arguments' if len(
                            arguments) > 1 else arguments + ' argument'
                    raise ValueError(
                        f"The 'toggle_full_screen' function is missing an Argument. Did you forgot the {msg}")
                else:
                    if main_window_top_position <= box.y+box.height <= main_window_bottom_position or main_window_top_position <= box.y <= main_window_bottom_position:
                        raise ValueError(
                            "The 'box' shouldn't overlap 'main_window'")
                    else:
                        if box.y+box.height <= main_window_top_position:
                            screen.blit(box, (0, box.y))
                        elif box.y > main_window_top_position:
                            screen.blit(
                                main_window, (0, main_window_top_position))
                        else:
                            screen.blit(box, (0, box.y))
    else:
        main_window = pygame.Surface((screen.get_width(), screen.get_height()))
        screen.blit(main_window, (0, 0))
