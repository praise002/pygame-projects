#a frog animating
import pygame
from sys import exit

"""A frog animating in the same position"""


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super(Player, self).__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load("img_frog/attack_1.png").convert_alpha())
        self.sprites.append(pygame.image.load("img_frog/attack_2.png").convert_alpha())
        self.sprites.append(pygame.image.load("img_frog/attack_3.png").convert_alpha())
        self.sprites.append(pygame.image.load("img_frog/attack_4.png").convert_alpha())
        self.sprites.append(pygame.image.load("img_frog/attack_5.png").convert_alpha())
        self.sprites.append(pygame.image.load("img_frog/attack_6.png").convert_alpha())
        self.sprites.append(pygame.image.load("img_frog/attack_7.png").convert_alpha())
        self.sprites.append(pygame.image.load("img_frog/attack_8.png").convert_alpha())
        self.sprites.append(pygame.image.load("img_frog/attack_9.png").convert_alpha())
        self.sprites.append(pygame.image.load("img_frog/attack_10.png").convert_alpha())
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale2x(self.image)

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self):
        self.is_animating = True

    def update(self, speed):
        if self.is_animating is True:
            self.current_sprite += speed  #increase d sprite slightly
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0  #go back to index 0
                self.is_animating = False  #stop the animation
            self.image = self.sprites[int(self.current_sprite)]  #convert it to int
            self.image = pygame.transform.scale2x(self.image)

#General setup
pygame.init()
clock = pygame.time.Clock()

#Game screen
screen_w, screen_h = 400, 400
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Frog Animation")
icon = pygame.image.load("img_frog/frog.png")
pygame.display.set_icon(icon)

#creating the sprites and groups
moving_sprite = pygame.sprite.Group()
player = Player(10, 10)
moving_sprite.add(player)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            player.animate()

    screen.fill((150, 250, 150))
    moving_sprite.draw(screen)
    moving_sprite.update(0.2)
    pygame.display.update()
    clock.tick(60)
