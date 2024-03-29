from typing import Sequence
import string
from ..flatten import flatten


def get_string_from_sequence(seq: Sequence) -> str:
    flattened_list = flatten(seq)
    return ''.join(flattened_list)


def get_window_pos(file: str, rank: int, possible_positions: list[str]) -> tuple[int, int]:
    assert len(possible_positions) == 8 and possible_positions == [
        letter for letter in string.ascii_lowercase[:8]], f"The 'possible_files' argument must be equivalent to {str([letter for letter in string.ascii_lowercase[:8]])}, not {possible_positions}"
    x = (rank-1)*100
    y = possible_positions.index(file)*100
    return x, y


def get_game_pos(x: int, y: int, possible_files: list[str]):
    assert len(possible_positions) == 8 and possible_positions == [
        letter for letter in string.ascii_lowercase[:8]], "The 'possible_files' argument must be equivalent to " + str([letter for letter in string.ascii_lowercase[:8]])
    rank = x/100+1
    file = possible_files[y/100]
    return file, rank
