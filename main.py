import pygame
from Racket import Racket
from Ball import Ball

FPS = 60
WINDOW_SIZE = (1280, 720)
RACKET_SIZE = (20, 120)
BALL_SIZE = 10


pygame.init()
window = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))

def handle_keypress(racket1: Racket, racket2: Racket):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]: 
        racket1.move('up')
    if keys[pygame.K_s]:
        racket1.move('down')
    if keys[pygame.K_UP]: 
        racket2.move('up')
    if keys[pygame.K_DOWN]:
        racket2.move('down')

def handle_collisions(racket1: Racket, racket2: Racket, ball: Ball):
    if ball.y + ball.velocity['y'] >= window.get_size()[1] or ball.y + ball.velocity['y'] <= 0: 
        ball.bounce('vertical')

    if ball.get_rect().colliderect(racket1.get_rect()) or ball.get_rect().colliderect(racket2.get_rect()):
        ball.bounce('horizontal')
        ball.velocity['x'] += int(abs(ball.velocity['x']) / ball.velocity['x'])
        ball.velocity['y'] += int(abs(ball.velocity['y']) / ball.velocity['y'])

    if ball.x + ball.velocity['x'] >= window.get_size()[0]:
        racket1.score += 1
        ball.reset()

    if ball.x + ball.velocity['x'] <= 0:
        racket2.score += 1
        ball.reset()

def draw(entities: list):
    window.fill((0, 0, 0))
    for entity in entities:
        entity.draw()

    font = pygame.font.Font(None, 74)

    text = font.render(str(racket1.score), True, (255, 255, 255))
    window.blit(text, (250, 30))
    
    text = font.render(str(racket2.score), True, (255, 255, 255))
    window.blit(text, (window.get_size()[0] - 270, 30))
    
    pygame.display.update();


racket1 = Racket((30, int(window.get_size()[1] / 2)), RACKET_SIZE, 10, window)
racket2 = Racket((window.get_size()[0] - RACKET_SIZE[0] - 30, int(window.get_size()[1] / 2)), RACKET_SIZE, 10, window)
ball = Ball(BALL_SIZE, (2, 4), window)

entities = [racket1, racket2, ball]


clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)

    handle_keypress(racket1, racket2)
    handle_collisions(racket1, racket2, ball)
    ball.move()
    
    draw(entities)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
