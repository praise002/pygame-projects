import pygame
from sys import exit

"""Player walking"""

#General setup
pygame.init()
clock = pygame.time.Clock()

#Game screen
screen_w, screen_h = 852, 480
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Player Animation")
icon = pygame.image.load("Images/standing.png")
pygame.display.set_icon(icon)

bg = pygame.image.load("Images/bg.jpg").convert_alpha()
standing = pygame.image.load("Images/standing.png")
standing_rect = standing.get_rect(bottomleft=(100, 400))

#image list
walk_right = [pygame.image.load("Images/R1.png"), pygame.image.load("Images/R2.png"),
              pygame.image.load("Images/R3.png"), pygame.image.load("Images/R4.png"),
              pygame.image.load("Images/R5.png"), pygame.image.load("Images/R6.png"),
              pygame.image.load("Images/R7.png"), pygame.image.load("Images/R8.png"),
              pygame.image.load("Images/R9.png")]

walk_left = [pygame.image.load("Images/L1.png"), pygame.image.load("Images/L2.png"),
             pygame.image.load("Images/L3.png"), pygame.image.load("Images/L4.png"),
             pygame.image.load("Images/L5.png"), pygame.image.load("Images/L6.png"),
             pygame.image.load("Images/L7.png"), pygame.image.load("Images/L8.png"),
             pygame.image.load("Images/L9.png")]


#image
left, right = False, False
walk_count = 0
width = walk_right[walk_count].get_width()

#position of image on screen
x = 70
y = 400

velocity = 5  #speed
is_jump = False
jump_count = 10


#try 18 frames
def redraw_screen():
    global walk_count
    screen.blit(bg, (0, 0))
    if walk_count + 1 >= 18:  #27 or 18 frames, display 3 frames
        walk_count = 0
    if left:
        screen.blit(walk_left[walk_count // 3], (x, y))
        walk_count += 1
    elif right:
        screen.blit(walk_right[walk_count // 3], (x, y))
        walk_count += 1
    else:
        screen.blit(standing, (x, y))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > velocity: #70>5
        x = x - velocity
        left, right = True, False

    elif keys[pygame.K_RIGHT] and x < screen_w - width - velocity:  #70<852-64-5
        x = x + velocity
        left, right = False, True

    else:
        left, right = False, False
        walk_count = 0

    redraw_screen()
    pygame.display.flip()
    clock.tick(60)
