import pygame
from sys import exit
from pygame import mixer

#basic setup
pygame.init()
screen_width = 300
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bouncing Ball')
icon = pygame.image.load('football-ball.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

#Ball
speed = [2, 2]
ball = pygame.image.load('football-ball.png').convert_alpha()
ball = pygame.transform.rotozoom(ball, 0, 2)
ball_rect = ball.get_rect(bottomleft=(100, 400))  #x, y

#intro screen
game_active = False
game_start_surface = pygame.image.load('play-button.png').convert_alpha()
game_start_surface = pygame.transform.rotozoom(game_start_surface, 0, 3)
width = game_start_surface.get_width()
height = game_start_surface.get_height()
game_start_rect = game_start_surface.get_rect(center=(70 + width, 200 + height))

text_font = pygame.font.Font('Pixeltype.ttf', 32)
text = text_font.render("Press space to play", True, (255, 255, 255), 'purple')
text_rect = text.get_rect(center=(150, 320))

#game over
# game_over = pygame.image.load('gameover.png').convert_alpha()
# game_over_rect = game_over.get_rect(center=((screen_width // 2) - 192, (screen_height // 2) - 42))
#
# game_over_timer = pygame.USEREVENT + 1
# pygame.time.set_timer(game_over_timer, 9000) #event, millis, loops
# start_timer = True

score = 0
high_score = 0

mixer.music.load("music.wav")
mixer.music.play(-1)  #loops, start, fade_ms


def score_display(game_state):
    if game_state == "main_game":
        score_surface = text_font.render(f"SCORE: {score // 10}", True, (255, 255, 255))  #text, aa, color, bg
        score_rect = score_surface.get_rect(topleft=(20, 20))
        screen.blit(score_surface, score_rect)
    if game_state == "intro_game":
        high_score_surface = text_font.render(f"SCORE: {high_score + score}", True, (255, 255, 255))  # text, aa, color, bg
        high_score_rect = high_score_surface.get_rect(topleft=(20, 20))
        screen.blit(high_score_surface, high_score_rect)


def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score


while True:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                exit()
            if event.key == pygame.K_SPACE:
                game_active = True

    #ball_rect
    if game_active:
        ball_rect = ball_rect.move(speed)  #moves d ball by d current speed
        if ball_rect.left < 0 or ball_rect.right > screen_width:
            speed[0] = -speed[0]  #reverse d ball

        if ball_rect.top < 0 or ball_rect.bottom > screen_height:
            speed[1] = -speed[1]

        screen.fill((180, 180, 180))
        screen.blit(ball, ball_rect)
        score += 1
        score_display("main_game")
        if score > 500:
            game_active = False
        else:
            game_active = True
        clock.tick(60)
    else:
        screen.fill((180, 180, 180))
        screen.blit(game_start_surface, game_start_rect)
        ball_rect.midtop = (screen_width // 2, (screen_height // 2) - 80)
        screen.blit(ball, ball_rect)
        screen.blit(text, text_rect)
        high_score = update_score(score, high_score)
        score_display("intro_game")
        score = 0

#give it a score, create timers and display game over, music: come back to update whenever i lean it