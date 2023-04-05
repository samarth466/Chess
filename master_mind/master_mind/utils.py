from random import choice


class Player:

    TRIES = 10
    COLORS = {
        'G': 'Green',
        'B': 'Blue',
        'W': 'White',
        'O': 'Orange',
        'R': 'Red',
        'Y': 'Yellow'
    }
    CODE_LENGTH = 4

    def __init__(self, status: str) -> None:
        self.status = status

    def _generate_code(self) -> list[str]:
        code = []
        for _ in range(self.CODE_LENGTH):
            code.append(choice(list(self.COLORS.keys())))
        return code

    def _check_code(self, guess: list[str], code: list[str]) -> tuple[int, int]:
        color_counts = {
            'correct': 0,
            'incorrect': 0
        }
        for color in code:
            if color not in color_counts:
                color_counts[color] = 0
            color_counts[color] += 1
        for guess_color, code_color in zip(guess, code):
            if code_color == guess_color:
                color_counts['correct'] += 1
                color_counts[code_color] -= 1
        for color in guess:
            if color in color_counts and color_counts[color] > 0:
                color_counts['incorrect'] += 1
                color_counts[color] -= 1
        return color_counts['correct'], color_counts['incorrect']

    def reset(self):
        return Player(self.status)
