from .utils import Player
from random import choice


class Person(Player):

    def _make_guess(self) -> list[str]:
        while True:
            guess = input(
                "What do you think the code is?: ").upper().split(' ')
            if len(guess) != self.CODE_LENGTH:
                print(
                    f"Your guess was not the correct length. The guess must have {self.CODE_LENGTH} items.")
                continue
            for color in guess:
                if color not in self.COLORS:
                    print(f"{color} is not a valid color. Please try again.")
                    break
            else:
                return guess

    def play(self, code: list[str] = None, message: str = "") -> tuple[list[str], str]:
        if self.status == 'code maker':
            pass
        elif self.status == 'code breaker':
            if message:
                print(message)
            guess = self._make_guess()
            return guess
