import pygame

class Racket:
    def __init__(self, initial_position: tuple[int, int], size: tuple[int, int], velocity: int, window: pygame.Surface):
        self.size = size
        self.velocity = velocity
        self.window = window
        self.x = initial_position[0]
        self.y = initial_position[1]
        self.score = 0

    def move(self, direction: str):
        if direction == 'up' and self.y - self.velocity >= 30:
            self.y -= self.velocity
        elif direction == 'down' and self.y + self.velocity <= (self.window.get_size()[1] - self.size[1] - 30):
            self.y += self.velocity

    def draw(self):
        pygame.draw.rect(
                self.window,
                (255, 255, 255),
                (
                    self.x,
                    self.y,
                    self.size[0],
                    self.size[1]
                )
            )

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size[0], self.size[1])
