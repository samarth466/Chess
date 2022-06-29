class Player:

    def __init__(self, username: str, color: tuple[int, int, int], multiplier: int):
        self.color = color
        self.username = username
        self.multiplier = multiplier
