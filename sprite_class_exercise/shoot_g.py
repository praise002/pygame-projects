import pygame
from sys import exit
from random import choice, randint, randrange


class Duck(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super(Duck, self).__init__()
        self.image = ducks[0]
        self.image = choice([ducks[0], ducks[1], ducks[0], ducks[1], ducks[0], ducks[1]])
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.dx = 1

    def update(self):
        self.rect = self.rect.move(self.dx, 0)
        # if self.rect.left < 0 or self.rect.right > screen_w:
        #     self.dx = -self.dx
        self.rect.x += self.dx
        if self.rect.right >= screen_w + 100:
            self.rect.left = -100
        if self.rect.top <= 0:
            self.rect.bottom = 20
        if self.rect.bottom >= screen_h:
            self.rect.top = 20


     # def update(self, direction):
    #     self.rect.x += direction


#General setup
pygame.init()
clock = pygame.time.Clock()

#Game screen
screen_w, screen_h = 500, 600
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Shooting Game")
icon = pygame.image.load("bullseye.png")
pygame.display.set_icon(icon)
pygame.mouse.set_visible(False)

#duck setup
duck1 = pygame.image.load("duck_target_yellow.png")
duck2 = pygame.image.load("duck_target_brown.png")
ducks = [duck1, duck2]

# duck = Duck(200, 200)
duck_group = pygame.sprite.Group()
# duck_group.add(duck)

for i in range(10):
    new_duck = Duck(randrange(0, screen_w), randrange(32, screen_h - 5))  #randrange(start,stop,step)
    duck_group.add(new_duck)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((150, 150, 250))
    duck_group.draw(screen)
    duck_group.update()
    # new_duck.update()
    # new_duck.move()
    pygame.display.flip()
    clock.tick(60)

