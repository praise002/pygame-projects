import pygame
from sys import exit
from pygame import mixer
from random import choice


def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 440))
    screen.blit(floor_surface, (floor_x_pos + 288, 440))  #second floor is next to 1st floor


def create_pipe():
    random_pipe_pos = choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(600, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(600, random_pipe_pos - 150))  #so space is btw d two
    return bottom_pipe, top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    visible_pipes = [pipe for pipe in pipes if pipe.right > -50]
    return visible_pipes  #instead of return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 512 or pipe.top > 0:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)


def check_collision(pipes):
    global can_score
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            death_sound.play()
            can_score = True
            return False

    #440 is the y_pos of d floor
    if bird_rect.top <= -100 or bird_rect.bottom >= 440:  #outside d screen or below d screen
        can_score = True
        return False

    return True  #if neither of this trigger


def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement*3, 1)  #surface, angle, scale
    return new_bird


def bird_animation():
    new_bird = bird_frames[bird_index]  #updates our bird
    new_bird_rect = new_bird.get_rect(center=(100, bird_rect.centery))  #take centery of d rect so we dont change d pos of d bird
    return new_bird, new_bird_rect


def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(screen_width/2, 50))
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(screen_width/2, 50))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'Score: {int(high_score)}', True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(screen_width/2, 425))
        screen.blit(high_score_surface, high_score_rect)


def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score


def pipe_score_check():
    global score, can_score
    #check for x and y pos of d bird
    if pipe_list:
        for pipe in pipe_list:
            if 95 < pipe.centerx < 105 and can_score:
                score += 1
                score_sound.play()
                can_score = False
            if pipe.centerx < 0:
                can_score = True


#basic setup
pygame.init()
screen_width = 288
screen_height = 512
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')
icon = pygame.image.load('assets/bluebird-upflap.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

game_font = pygame.font.Font('04B_19.TTF', 20)

bg_surface = pygame.image.load('assets/background-day.png').convert()
floor_surface = pygame.image.load('assets/base.png').convert()
floor_x_pos = 0

bird_downflap = pygame.image.load('assets/bluebird-downflap.png').convert_alpha()
bird_midflap = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
bird_upflap = pygame.image.load('assets/bluebird-upflap.png').convert_alpha()
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0  #to pick a specific surface from the list
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center=(100, 256))

BIRD_FLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRD_FLAP, 200)
# bird_surface = pygame.image.load("assets/bluebird-midflap.png").convert_alpha()
# bird_rect = bird_surface.get_rect(center=(100, 256))  #left, top

pipe_surface = pygame.image.load("assets/pipe-green.png")
pipe_list = []
SPAWN_PIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWN_PIPE, 1200)  #event, millis, loop
pipe_height = [256, 144, 190, 200]

#Game variables
gravity = 0.25
bird_movement = 0
game_active = True
score = 0
high_score = 0
can_score = True  #to avoid score increasing too much

game_over_surface = pygame.image.load('assets/message.png').convert_alpha()
game_over_rect = game_over_surface.get_rect(center=(screen_width/2, screen_height/2))

flap_sound = mixer.Sound('sound/sfx_wing.wav')
death_sound = mixer.Sound('sound/sfx_hit.wav')
score_sound = mixer.Sound('sound/sfx_point.wav')

score_sound_countdown = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                exit()
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0  #disable all d effects of gravity
                bird_movement -= 12
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active is False:
                game_active = True  #screen dissapears, do d below to fix it
                pipe_list.clear()
                bird_rect.center = (100, 256)
                bird_movement = 0   #clear bird movement
                score = 0  #reset the score
        if event.type == SPAWN_PIPE:
            pipe_list.extend(create_pipe())  #use instead of append to unpack d tuple

        if event.type == BIRD_FLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0

            bird_surface, bird_rect = bird_animation()

    screen.blit(bg_surface, (0, 0))
    if game_active:
        #Bird
        bird_movement += gravity  #increases at every frame
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(bird_surface, bird_rect)
        game_active = check_collision(pipe_list)

        #Pipes
        pipe_list = move_pipes(pipe_list)  #override existing lists
        draw_pipes(pipe_list)
        # score += 0.01  #100cycles to get to 1

        #Score
        pipe_score_check()
        score_display('main_game')
        score_sound_countdown -= 1
        # if score_sound_countdown <= 0:
        #     score_sound.play()
        #     score_sound_countdown = 100  #100cycles to get to 0

    else:
        screen.blit(game_over_surface, game_over_rect)
        high_score = update_score(score, high_score)
        score_display('game_over')

    #floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -288:
        floor_x_pos = 0  #reset the  floor when it goes too far to d left
    pygame.display.update()
    clock.tick(120)
