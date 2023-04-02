from typing import Any
from board_utils import Square

GamePosition = tuple[str, int]
WindowPosition = tuple[int, int]
Positions = list[GamePosition]
Squares = dict[GamePosition, Square]
PositionDict = dict[GamePosition, Any]
