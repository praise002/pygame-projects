import pygame
from sys import exit


#basic setup
pygame.init()
screen_width = 400
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Timers')
icon = pygame.image.load('chronometer.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

current_time = 0
button_pressed_time = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            button_pressed_time = pygame.time.get_ticks()  #static time unless button is pressed
            print(f"button_pressed_time{button_pressed_time}")
            screen.fill((255, 255, 255))
            if event.key == pygame.K_q:
                exit()

    current_time = pygame.time.get_ticks()  #in millisecond
    print(current_time)
    if current_time - button_pressed_time > 2000:
        screen.fill((100, 100, 200))

    pygame.display.flip()
    clock.tick(60)


#press any key on the keyboard to change color