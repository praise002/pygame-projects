import pygame
from sys import exit

"""Girl walk left and reverse to the right once a key is pressed"""

#General setup
pygame.init()
clock = pygame.time.Clock()

#Game screen
screen_w, screen_h = 500, 500
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Girl Animation")
icon = pygame.image.load("images_girl/girl.png")
pygame.display.set_icon(icon)

#image list
walk_right = [pygame.image.load("images_girl/walk1.png"), pygame.image.load("images_girl/walk2.png"),
             pygame.image.load("images_girl/walk3.png"), pygame.image.load("images_girl/walk4.png"),
             pygame.image.load("images_girl/walk5.png"), pygame.image.load("images_girl/walk6.png"),
             pygame.image.load("images_girl/walk7.png"), pygame.image.load("images_girl/walk8.png"),
             pygame.image.load("images_girl/walk9.png"), pygame.image.load("images_girl/walk10.png")]

walk_left = [pygame.image.load("images_girl/walk1.png"), pygame.image.load("images_girl/walk2.png"),
             pygame.image.load("images_girl/walk3.png"), pygame.image.load("images_girl/walk4.png"),
             pygame.image.load("images_girl/walk5.png"), pygame.image.load("images_girl/walk6.png"),
             pygame.image.load("images_girl/walk7.png"), pygame.image.load("images_girl/walk8.png"),
             pygame.image.load("images_girl/walk9.png"), pygame.image.load("images_girl/walk10.png")]


#image right
right = False
walk_count = 0
width = walk_right[walk_count].get_width()

#image left
left = False
# walk_left_flip = pygame.transform.flip(walk_left[walk_count], True, False)

#position of image  on screen
x = 70
y = 300

velocity = 5 #speed


#try 18 frames
def redraw_screen():
    global walk_count, walk_left
    screen.fill((200, 200, 200))
    if walk_count + 1 >= 12:  #27 or 18 frames, display 3 frames
        walk_count = 0

    if right:
        screen.blit(walk_right[walk_count // 3], (x, y))
        walk_count += 1
    elif left:
        screen.blit(walk_left[walk_count // 3], (x, y))
        walk_count += 1
    else:
        walk_count = 0
        screen.blit(walk_right[walk_count], (x, y))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and x < screen_w - width - velocity:  #70<400-32-5
        x = x + velocity
        right = True
        left = False

    elif keys[pygame.K_LEFT] and x > velocity: #70>5
        x = x - velocity
        left = True
        right = False

    else:
        right = False
        left = False
        walk_count = 0

    redraw_screen()
    pygame.display.flip()
    clock.tick(60)
