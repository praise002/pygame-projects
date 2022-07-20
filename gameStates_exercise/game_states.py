import pygame
from sys import exit

#basic setup
pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Game states')
# icon = pygame.image.load('football-ball.png')
# pygame.display.set_icon(icon)
clock = pygame.time.Clock()
text_font = pygame.font.Font('8-BIT WONDER.TTF', 32)


class GameState:
    def __init__(self):
        self.state = "intro"

    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = "main_game"

        screen.fill((50, 50, 50))
        intro_text = text_font.render("Play", True, (255, 255, 255))
        intro_rect = intro_text.get_rect(center=(300, 300))
        screen.blit(intro_text, intro_rect)
        pygame.display.flip()

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.fill((150, 50, 150))
        main_text = text_font.render("Main", True, (255, 255, 255))
        main_rect = main_text.get_rect(center=(300, 300))
        screen.blit(main_text, main_rect)
        pygame.display.flip()

    def state_manager(self):
        if self.state == "intro":
            self.intro()
        if self.state == "main_game":
            self.main_game()


g = GameState()


if __name__ == "__main__":
    while True:
        g.state_manager()
        # g.main_game()