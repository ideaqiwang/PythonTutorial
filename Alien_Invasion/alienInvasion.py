import sys
import pygame
from settings import Settings


class AlienInvasion:
    # instance variable
    # e.g. self.screen, self.bg_color

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width, 
                                               self.settings.height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        # Start the main loop for the game.
        while True:
        # Watch for keyboard and mouse events.
        # event queue: FIFO
        # [ q, w, e, mouse left click, mouse right click ]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        # Make the most recently drawn screen visible.
            self.screen.fill(self.settings.bgcolor)
            pygame.display.flip()