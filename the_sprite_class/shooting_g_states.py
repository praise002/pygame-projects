import pygame
from sys import exit
from random import randint, randrange


class Crosshair(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        super(Crosshair, self).__init__()
        self.image = pygame.image.load("images/crosshair_blue_large.png")
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def shoot(self):
        pygame.sprite.spritecollide(crosshair, target_group, True)  # sprite, gp, dokill

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super(Target, self).__init__()
        self.image = pygame.image.load(picture_path).convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 2)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


class GameState:
    def __init__(self):
        self.state = "intro"

    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = "main_game"

        screen.fill((50, 50, 50))
        screen.blit(ready_text, (screen_w / 2 - 115, screen_h / 2 - 33))
        pygame.display.flip()

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                crosshair.shoot()

        screen.fill((50, 50, 50))
        target_group.draw(screen)
        crosshair_group.draw(screen)
        crosshair_group.update()
        pygame.display.flip()

    def state_manager(self):
        if self.state == "intro":
            self.intro()
        if self.state == "main_game":
            self.main_game()


#General setup
pygame.init()
clock = pygame.time.Clock()
game_state = GameState()

#Game screen
screen_w, screen_h = 800, 600
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Shooting Game")
icon = pygame.image.load("images/sprite.png")
pygame.display.set_icon(icon)
pygame.mouse.set_visible(False)

ready_text = pygame.image.load("images/text_ready.png")

#crosshair
crosshair = Crosshair(50, 50, 100, 100, (255, 255, 255))
crosshair_group = pygame.sprite.Group()  #first create a group
crosshair_group.add(crosshair)

#target
# target = Target("images/sprite.png", screen_w // 2, screen_h // 2)
# target_group = pygame.sprite.Group()
# target_group.add(target)

target_group = pygame.sprite.Group()
for target in range(21):
    new_target = Target("images/bullseye.png", randint(0, screen_w), randint(0, screen_h))
    target_group.add(new_target)

while True:
    game_state.state_manager()
    clock.tick(60)

