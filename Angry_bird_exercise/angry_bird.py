"""
It is not a fancy game, just playing around with pygame
It was kinda difficult but its okay
"""
import pygame
from sys import exit
from random import choice


def display_background():
    screen.blit(bg, (0, 0))


def draw_floor():
    global floor_x_pos
    floor_x_pos -= 1
    screen.blit(floor_surface, (floor_x_pos, 440))
    screen.blit(floor_surface, (floor_x_pos + 288, 440))
    if floor_x_pos <= -288:
        floor_x_pos = 0


def create_pipe():
    random_pipe_pos = choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(144, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(600, random_pipe_pos - 100))
    return bottom_pipe, top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 512 or pipe.top > 0:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)


def draw_bird():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center=(100, 256))
    screen.blit(new_bird, new_bird_rect)
    return new_bird, new_bird_rect


pygame.init()
screen_w = 288
screen_h = 512
screen = pygame.display.set_mode((screen_w, screen_h))
clock = pygame.time.Clock()

pygame.display.set_caption('Angry Bird')
icon = pygame.image.load('images/angry-birds.png')
pygame.display.set_icon(icon)

#Background
bg = pygame.image.load('assets/background-day.png')
floor_surface = pygame.image.load('assets/base.png')
floor_x_pos = 0

#pipes
pipe_list = []
pipe_height = [256, 144, 190, 200]
pipe_surface = pygame.image.load('assets/pipe-red.png')

SPAWN_PIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWN_PIPE, 1200)

#Bird
angry_bird_surface = pygame.image.load('images/angry-birds.png').convert_alpha()
bird1_surface = pygame.image.load('images/bird.png').convert_alpha()
bird_frames = [angry_bird_surface, bird1_surface]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center=(144, 256))


SPAWN_BIRD = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_BIRD, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == SPAWN_PIPE:
            pipe_list.extend(create_pipe())

        if event.type == SPAWN_PIPE:
            if bird_index < 1:
                bird_index += 1
            else:
                bird_index = 0
            bird_surface, bird_rect = draw_bird()

    display_background()
    #Pipes
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

    draw_floor()
    screen.blit(bird_surface, bird_rect)
    pygame.display.flip()
    clock.tick(120)
