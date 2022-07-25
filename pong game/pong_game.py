import pygame
from sys import exit
from pygame import mixer


def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        # ball_speed_y = ball_speed_y * -1  #reverse it
        ball_speed_y = -ball_speed_y
    if ball.left <= 0 or ball.right >= screen_width:
        # ball_speed_x = ball_speed_x * -1
        ball_speed_x = -ball_speed_x

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x = ball_speed_x * -1


def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


#basic setup
pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong Game')
icon = pygame.image.load('Ball.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

#Game rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)  #left, right, top, bottom
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

ball_speed_x = 7
ball_speed_y = 7

player_speed = 0
opponent_speed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                exit()
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()
    opponent_ai()

    #Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    #updating the window
    pygame.display.update()
    clock.tick(60)


#opponents top above ball: move down
#opponents bottom below ball: move up
#speed of opponent determines difficulty