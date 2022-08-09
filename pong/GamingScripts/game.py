import pygame
from paddle import Paddle

pygame.init()
pygame.display.init()
WIDTH, HEIGHT = 700, 500
WINDOW = pygame.display.set_mode(
    (WIDTH, HEIGHT), pygame.SHOWN | pygame.HWSURFACE | pygame.SCALED)
pygame.display.set_caption("Pong")
FPS = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def draw(window: pygame.Surface, paddles: list[Paddle]):
    window.fill(BLACK)
    for paddle in paddles:
        paddle.draw(WINDOW, WHITE)
    pygame.display.update()


def move_paddle(keys, left_paddle, right_paddle) -> None:
    if keys[pygame.K_w] and left_paddle.y > 0:
        left_paddle.move()
    if keys[pygame.K_s] and left_paddle < HEIGHT:
        left_paddle.move(False)
    if keys[pygame.K_UP] and right_paddle.y > 0:
        right_paddle.move()
    if keys[pygame.K_DOWN] and right_paddle.y < HEIGHT:
        right_paddle.move(False)


def main():
    paddle_width, paddle_height = 20, 100
    left_paddle = Paddle(10, HEIGHT//2-paddle_height //
                         2, paddle_width, paddle_height)
    right_paddle = Paddle(WIDTH-10-paddle_width, HEIGHT //
                          2-paddle_height//2, paddle_width, paddle_height)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        draw(WINDOW, [left_paddle, right_paddle])
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run = False
        move_paddle(keys, left_paddle, right_paddle)
    pygame.quit()


if __name__ == "__main__":
    main()
