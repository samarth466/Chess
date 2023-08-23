import pygame


class Paddle:

    vel = 4

    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, window: pygame.Surface, color: tuple[int, int, int]) -> None:
        pygame.draw.rect(
            window, color, (self.x, self.y, self.width, self.height))

    def move(self, up: bool = True) -> None:
        self.y -= self.vel if up else -self.vel
