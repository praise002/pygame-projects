import pygame
from sys import exit

pygame.init()

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Box')
icon = pygame.image.load('bluebird-upflap.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

#surface and rects
surface = pygame.Surface((50, 50))  #w,h
surface.fill('blue')
surface_rect = surface.get_rect()
surface_rect.bottomleft = (200, 300) #x, y

surface1 = pygame.Surface((50, 50))  #w,h
surface1.fill('purple')
surface1_rect = surface.get_rect()
surface1_rect.bottomleft = (250, 300)  #left,bottom

surface2 = pygame.Surface((50, 50))  #w,h
surface2.fill('pink')
surface2_rect = surface.get_rect()
surface2_rect.topleft = (200, 200)  #left,bottom

surface3 = pygame.Surface((50, 50))  #w,h
surface3.fill('yellow')
surface3_rect = surface.get_rect()
surface3_rect.topright = (300, 200)

x = 300
# surf = pygame.Rect(x, 400, 100, 100)  #left, top, width, height
surf = pygame.Rect(200, 200, 100, 100)
# surf = pygame.Rect(200, 220, 100, 100)

#text
text_font = pygame.font.Font('04B_19.TTF', 32)  #name, size
text = text_font.render("Box Game", True, (180, 40, 50))  #text, aa, color, bg
text_rect = text.get_rect(center=(300, 100))

font = pygame.font.get_fonts()[5]
print(font)
font2 = pygame.font.get_default_font()
print(font2)

#image
player_x = 100
player = pygame.image.load("player.png").convert_alpha()
player_rect = player.get_rect(bottomleft=(player_x, 500))
flip_player = pygame.transform.flip(player, True, True)
scale_player = pygame.transform.scale(player, (124, 124))
rotate_player = pygame.transform.rotate(player, 270)
scale2_player = pygame.transform.scale2x(player)
zoom_player = pygame.transform.rotozoom(player, 0, 2)
chop_player = pygame.transform.chop(player, player_rect)

#timers
OBSTACLE_TIMER = pygame.USEREVENT + 1
pygame.time.set_timer(OBSTACLE_TIMER, 500)  #events, millis, loops
start_timer = True

while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if player_rect.collidepoint(event.pos):
                print('collision')

        if event.type == OBSTACLE_TIMER and start_timer:
            player_rect.x += 5
            start_timer = False
            if start_timer is False:
                start_timer = True
            else:
                start_timer = False

        # keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            print('left')
        elif keys[pygame.K_RIGHT]:
            print('right')
        elif keys[pygame.K_UP]:
            print('up')
        elif keys[pygame.K_DOWN]:
            print('down')
        elif keys[pygame.K_BACKSPACE]:
            print('backspace')
        elif keys[pygame.K_DELETE]:
            print('delete')
        else:
            print('others')

    screen.fill((50, 50, 50))
    screen.blit(surface, surface_rect)
    screen.blit(surface1, surface1_rect)
    screen.blit(surface2, surface2_rect)
    screen.blit(surface3, surface3_rect)
    screen.blit(text, text_rect)
    screen.blit(player, player_rect)
    pygame.draw.rect(screen, "red", surf, 3)
    # pygame.draw.circle()
    # pygame.draw.rect(screen, "red", surf)

    #mouse pos
    # pygame.mouse.set_visible(False)
    # print(pygame.mouse.get_pos())  #returns a tuple
    # print(pygame.mouse.get_rel())  #returns d amount of mouse movement
    # pygame.mouse.set_pos([50, 100])
    # print(pygame.mouse.get_visible())
    # print(pygame.mouse.get_focused())
    # pygame.mouse.set_cursor()
    # print(pygame.mouse.get_cursor())

    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print('collide')

    clock.tick(60)
