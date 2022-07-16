"""
Get input from the player
Draw the games images on the screen
Update the game based off the players actions
"""
import pygame
import game


class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100

    def draw_cursor(self):
        self.game.draw_text("*", 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.screen.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()