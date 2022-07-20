import pygame
from sys import exit

#intro screen, main game, game over screen
"""
You can alternate between scenes
Press space to go to main_game
Press tab to go to game_over
KEYS IN INTRO SCREEN
-space
KEYS IN MAIN_GAME
tab
k_1
KEYS IN GAME_OVER_SCREEN
k_2, k_3
"""


class Game:
    def __init__(self):
        pygame.init()
        self.state = "intro"
        self.screen_w, self.screen_h = 600, 600
        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))
        self.font_name = "8-BIT WONDER.TTF"
        self.font = pygame.font.Font(self.font_name, 32)
        self.image = pygame.image.load("beach-ball.png")
        self.clock = pygame.time.Clock()

    def display(self):
        pygame.display.set_icon(self.image)
        pygame.display.set_caption("Game States")
        self.font.render("Game States", True, (255, 255, 255))
        self.clock.tick(60)

    def update(self):
        self.game_states()
        pygame.display.update()

    def intro_screen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:  # use left and right key
                if event.key == pygame.K_SPACE:
                    self.state = "main_game"

        self.screen.fill((50, 50, 50))
        intro_text = self.font.render("Play", True, (255, 255, 255))
        intro_rect = intro_text.get_rect(center=(300, 300))
        self.screen.blit(intro_text, intro_rect)

    def main_screen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    self.state = "game_over"
                if event.key == pygame.K_1:
                    self.state = "intro"

        self.screen.fill((50, 50, 150))
        main_text = self.font.render("Main", True, (255, 255, 255))
        main_rect = main_text.get_rect(center=(300, 300))
        self.screen.blit(main_text, main_rect)

    def game_over_screen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    self.state = "main_game"
                if event.key == pygame.K_3:
                    self.state = "intro"

        self.screen.fill((150, 50, 150))
        game_over_img = pygame.image.load("gameover.png").convert_alpha()
        game_over_rect = game_over_img.get_rect(center=(300, 300))
        self.screen.blit(game_over_img, game_over_rect)

    def game_states(self):
        if self.state == "intro":
            self.intro_screen()
        if self.state == "main_game":
            self.main_screen()
        if self.state == "game_over":
            self.game_over_screen()
