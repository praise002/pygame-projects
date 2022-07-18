import pygame
from sys import exit

"""A simple player jump. Work in progress"""

#General setup
pygame.init()
clock = pygame.time.Clock()

#Game screen
screen_w, screen_h = 300, 400
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Player Animation")
icon = pygame.image.load("girl.png")
pygame.display.set_icon(icon)

#surface and rects
surf = pygame.Surface((50, 50))
surf.fill("blue")
surf_rect = surf.get_rect()
surf_rect.bottomleft = (100, 350)

velocity_y = 10
gravity = 0
jump = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        jump = True
        surf_rect.y = surf_rect.y - velocity_y*4
        pygame.time.delay(10)
        velocity_y = velocity_y - 1
        if velocity_y < -10:
            jump = False
            velocity_y = 10

    screen.fill((90, 90, 90))
    screen.blit(surf, surf_rect)
    pygame.display.update()
    clock.tick(60)

#still work on the jumping
