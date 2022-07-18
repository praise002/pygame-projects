import pygame
from sys import exit

#debug after downloading wing
#work on self.standing

"""A player animating in the same position"""


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super(Player, self).__init__()
        self.walk_count = 0
        self.walk_count_left = 9
        self.images = []
        #right movement
        self.images.append(pygame.image.load("images/R1.png").convert_alpha())
        self.images.append(pygame.image.load("images/R2.png").convert_alpha())
        self.images.append(pygame.image.load("images/R3.png").convert_alpha())
        self.images.append(pygame.image.load("images/R4.png").convert_alpha())
        self.images.append(pygame.image.load("images/R5.png").convert_alpha())
        self.images.append(pygame.image.load("images/R6.png").convert_alpha())
        self.images.append(pygame.image.load("images/R7.png").convert_alpha())
        self.images.append(pygame.image.load("images/R8.png").convert_alpha())
        self.images.append(pygame.image.load("images/R9.png").convert_alpha())
        #left movement
        self.images.append(pygame.image.load("images/L1.png").convert_alpha())
        self.images.append(pygame.image.load("images/L2.png").convert_alpha())
        self.images.append(pygame.image.load("images/L3.png").convert_alpha())
        self.images.append(pygame.image.load("images/L4.png").convert_alpha())
        self.images.append(pygame.image.load("images/L5.png").convert_alpha())
        self.images.append(pygame.image.load("images/L6.png").convert_alpha())
        self.images.append(pygame.image.load("images/L7.png").convert_alpha())
        self.images.append(pygame.image.load("images/L8.png").convert_alpha())
        self.images.append(pygame.image.load("images/L9.png").convert_alpha())

        self.image = self.images[self.walk_count]
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(bottomleft=[pos_x, pos_y])
        self.left, self.right = False, False

        self.standing = pygame.image.load("Images/standing.png")
        self.standing_rect = self.standing.get_rect(bottomleft=(100, 400))

    def update(self):
        while True:
        #     if self.left:
        #         self.walk_count = 0
        #     else:
        #         self.walk_count = 9  #character only faces left and right
            self.walk_count += 0.2
            if self.right is True:
                if self.walk_count >= len(self.images[0:9]):
                    self.walk_count = 0
                    # self.right = False  #sprite stops moving when i release arrow key
                self.image = self.images[int(self.walk_count)]
                self.image = pygame.transform.scale2x(self.image)

            elif self.left is True:  #try to understand this
                self.walk_count_left += 0.2
                if self.images[int(self.walk_count_left)] == self.images[16]:
                    self.walk_count_left = 9
                self.image = self.images[int(self.walk_count_left)]
                self.image = pygame.transform.scale2x(self.image)
            # self.image = self.images[self.walk_count]
            # self.image = pygame.transform.scale2x(self.image)

            self.get_events()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.left, self.right = True, False

                if event.key == pygame.K_RIGHT:
                    self.left, self.right = False, True

        screen.blit(bg, (0, 0))
        player_group.draw(screen)
        pygame.display.update()
        clock.tick(60)


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

#sprites and groups
player = Player(100, 400)
player_group = pygame.sprite.Group()
player_group.add(player)

while True:
    screen.blit(standing, standing_rect)
    player_group.update()


