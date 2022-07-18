import pygame

from sys import exit


class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
        #adding all images to the sprite array
        self.images = []
        self.images.append(pygame.image.load("images_sprite/walk1.png").convert_alpha())
        self.images.append(pygame.image.load("images_sprite/walk2.png").convert_alpha())
        self.images.append(pygame.image.load("images_sprite/walk3.png").convert_alpha())
        self.images.append(pygame.image.load("images_sprite/walk4.png").convert_alpha())
        self.images.append(pygame.image.load("images_sprite/walk5.png").convert_alpha())
        self.images.append(pygame.image.load("images_sprite/walk6.png").convert_alpha())
        self.images.append(pygame.image.load("images_sprite/walk7.png").convert_alpha())
        self.images.append(pygame.image.load("images_sprite/walk8.png").convert_alpha())
        self.images.append(pygame.image.load("images_sprite/walk9.png").convert_alpha())
        self.images.append(pygame.image.load("images_sprite/walk10.png").convert_alpha())

        #index value to get the image from the array
        #initially it is 0
        self.index = 0

        #image to be displayed from the images array
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(bottomleft=(100, 400))

    def update(self):
        #when the update method is called it will increment the index
        self.index += 1

        #if the index is larger than the total images'
        if self.index >= len(self.images):
            self.index = 0

        #initially we will update the image that will be displayed
        self.image = self.images[self.index]


#General setup
pygame.init()
clock = pygame.time.Clock()

#Game screen
screen_w, screen_h = 600, 400
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Player Animation")
icon = pygame.image.load("images_sprite/girl.png")
pygame.display.set_icon(icon)

#sprites and groups
my_sprites = MySprite()
sprite_group = pygame.sprite.Group()
sprite_group.add(my_sprites)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((150, 250, 250))
    sprite_group.update()
    sprite_group.draw(screen)
    pygame.display.update()
    clock.tick(10)
