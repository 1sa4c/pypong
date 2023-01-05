import pygame

class Ball:
    def __init__(self, size: int, initial_velocity: tuple[int, int], window: pygame.Surface):
        self.size = size
        self.velocity = {'x': initial_velocity[0], 'y': initial_velocity[1]}
        self.initial_velocity = {'x': initial_velocity[0], 'y': initial_velocity[1]}
        self.window = window
        self.x = window.get_size()[0] / 2
        self.y = window.get_size()[1] / 2

    def move(self):
        self.x += int(self.velocity['x'])
        self.y += int(self.velocity['y'])

    def draw(self):
        pygame.draw.circle(
                self.window,
                (255, 255, 255),
                (self.x, self.y),
                self.size
                )

    def get_rect(self):
        return pygame.Rect(self.x - self.size, self.y - self.size, self.size*2, self.size*2)

    def bounce(self, direction: str):
        if direction == 'horizontal':
            self.velocity['x'] *= -1
        if direction == 'vertical':
            self.velocity['y'] *= -1
            
    def reset(self):
        self.velocity['x'] = -int(abs(self.velocity['x']) / self.velocity['x']) * self.initial_velocity['x']
        self.velocity['y'] = self.initial_velocity['y']
        self.x = int(self.window.get_size()[0] / 2)
        self.y = int(self.window.get_size()[1] / 2)
        
